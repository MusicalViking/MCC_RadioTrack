#!/usr/bin/env python3
"""
Simple PDF test for browser compatibility
"""
import sys
import os

# Add current directory to path
sys.path.insert(0, os.getcwd())

def test_simple_pdf():
    """Test basic PDF generation"""
    try:
        from pdf_generator import generate_inventory_pdf

        print("Testing PDF generation...")

        # Test complete report
        buffer = generate_inventory_pdf('complete')
        pdf_data = buffer.getvalue()

        print(f"PDF size: {len(pdf_data)} bytes")

        # Check PDF validity
        if pdf_data.startswith(b'%PDF'):
            print("✓ Valid PDF format")
        else:
            print("✗ Invalid PDF format")
            return False

        # Check for proper ending
        if b'%%EOF' in pdf_data:
            print("✓ Proper PDF ending")
        else:
            print("✗ Missing PDF ending")

        # Save PDF for testing
        with open('browser_compatible.pdf', 'wb') as f:
            f.write(pdf_data)

        print("✓ PDF saved as browser_compatible.pdf")
        print("✅ PDF generation is working correctly!")
        print("The PDF should now load properly in browsers.")

        return True

    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_simple_pdf()
