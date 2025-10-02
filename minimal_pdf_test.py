#!/usr/bin/env python3
"""
Minimal PDF test - no database dependency
"""
import sys
import os
import io
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def test_minimal_pdf():
    """Create a minimal PDF without database dependency"""
    print("Creating minimal test PDF...")

    try:
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(
            buffer,
            pagesize=landscape(letter),
            leftMargin=0.5*inch,
            rightMargin=0.5*inch,
            topMargin=0.5*inch,
            bottomMargin=0.5*inch,
            author="RadioTrack",
            title="Test Report"
        )

        styles = getSampleStyleSheet()
        elements = []

        # Add title
        title_style = ParagraphStyle(
            "CustomTitle",
            parent=styles["Heading1"],
            fontSize=20,
            spaceAfter=20,
            alignment=1,
        )

        elements.append(Paragraph("RadioTrack Test Report", title_style))
        elements.append(Paragraph(f"Generated on {__import__('datetime').datetime.now().strftime('%B %d, %Y')}", styles["Normal"]))
        elements.append(Spacer(1, 20))

        # Create simple test table
        table_data = [
            ["Item Name", "Category", "Condition"],
            ["Test Radio 1", "Handheld", "Good"],
            ["Test Radio 2", "Mobile", "Excellent"],
            ["Test Radio 3", "Base Station", "Fair"]
        ]

        table = Table(table_data, colWidths=[2 * inch, 1.5 * inch, 1.2 * inch])
        table.splitByRow = 1

        table.setStyle(
            TableStyle([
                # Header styling
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#4A90E2")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("ALIGN", (0, 0), (-1, 0), "CENTER"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, 0), 10),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
                # Content styling
                ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#F8F9FA")),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#DEE2E6")),
                ("VALIGN", (0, 1), (-1, -1), "TOP"),
            ])
        )

        elements.append(table)

        # Build PDF
        doc.build(elements)
        pdf_data = buffer.getvalue()

        print(f"✓ Test PDF generated! Size: {len(pdf_data)} bytes")

        # Validate PDF
        if pdf_data.startswith(b'%PDF'):
            print("✓ Valid PDF header")
        else:
            print("✗ Invalid PDF header")
            return False

        if b'%%EOF' in pdf_data:
            print("✓ Valid PDF ending")
        else:
            print("✗ Missing PDF ending")

        # Save PDF
        with open('minimal_test.pdf', 'wb') as f:
            f.write(pdf_data)

        print("✓ Test PDF saved as minimal_test.pdf")
        print("✅ Minimal PDF generation is working!")

        return True

    except Exception as e:
        print(f"✗ Error creating minimal PDF: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_minimal_pdf()
