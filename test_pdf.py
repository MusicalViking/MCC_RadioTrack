#!/usr/bin/env python3
"""
Test script to verify PDF generation works correctly
"""
import sys
import os
sys.path.append('.')

def test_pdf_generation():
    """Test basic PDF generation functionality"""
    try:
        from pdf_generator import generate_inventory_pdf
        print("✓ PDF generator imported successfully")

        # Test minimal PDF generation
        buffer = generate_inventory_pdf('complete')
        pdf_data = buffer.getvalue()

        print(f"✓ PDF generated successfully! Size: {len(pdf_data)} bytes")

        # Check PDF validity
        if pdf_data.startswith(b'%PDF'):
            print("✓ Valid PDF format detected")
        else:
            print("✗ Invalid PDF format")
            return False

        # Save for manual inspection
        with open('test_output.pdf', 'wb') as f:
            f.write(pdf_data)
        print("✓ PDF saved as test_output.pdf")

        return True

    except Exception as e:
        print(f"✗ Error during PDF generation: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_minimal_pdf():
    """Test with a minimal PDF structure"""
    try:
        from reportlab.lib import colors
        from reportlab.lib.pagesizes import letter, landscape
        from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        import io

        buffer = io.BytesIO()
        doc = SimpleDocTemplate(
            buffer,
            pagesize=landscape(letter),
            leftMargin=0.42*inch,
            rightMargin=0.42*inch,
            topMargin=0.5*inch,
            bottomMargin=0.5*inch,
            author='RadioTrack',
            title='Test Report'
        )

        styles = getSampleStyleSheet()
        elements = []

        # Add title
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            alignment=1,
        )

        elements.append(Paragraph('Test PDF Report', title_style))
        elements.append(Spacer(1, 20))

        # Create simple table
        table_data = [['Test', 'Data'], ['Item 1', 'Value 1']]
        table = Table(table_data, colWidths=[2 * inch, 2 * inch])

        table.setStyle(
            TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ])
        )

        elements.append(table)

        # Build PDF
        doc.build(elements)
        pdf_data = buffer.getvalue()

        print(f"✓ Minimal test PDF generated! Size: {len(pdf_data)} bytes")

        if pdf_data.startswith(b'%PDF'):
            print("✓ Valid PDF format")
        else:
            print("✗ Invalid PDF format")
            return False

        with open('test_minimal.pdf', 'wb') as f:
            f.write(pdf_data)
        print("✓ Minimal test PDF saved")

        return True

    except Exception as e:
        print(f"✗ Error in minimal PDF test: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("=== PDF Generation Test ===")
    print()

    # Test 1: Basic PDF generation
    print("Test 1: Basic PDF generation")
    test1_success = test_pdf_generation()
    print()

    # Test 2: Minimal PDF structure
    print("Test 2: Minimal PDF structure")
    test2_success = test_minimal_pdf()
    print()

    # Summary
    print("=== Test Summary ===")
    print(f"Basic PDF generation: {'✓ PASS' if test1_success else '✗ FAIL'}")
    print(f"Minimal PDF structure: {'✓ PASS' if test2_success else '✗ FAIL'}")

    if test2_success:
        print()
        print("✅ PDF generation appears to be working correctly!")
        print("The issue might be with empty database or specific data conditions.")
    else:
        print()
        print("❌ There are still issues with PDF generation.")
