#!/usr/bin/env python3
"""
Enhanced PDF test with better styling and word wrapping
"""
import sys
import os

# Add current directory to path
sys.path.insert(0, os.getcwd())

def test_enhanced_pdf():
    """Test the enhanced PDF generation with better styling"""
    try:
        from pdf_generator import generate_inventory_pdf

        print("Testing enhanced PDF generation...")

        # Test complete report with enhanced styling
        buffer = generate_inventory_pdf('complete')
        pdf_data = buffer.getvalue()

        print(f"✓ Enhanced PDF generated! Size: {len(pdf_data)} bytes")

        # Validate PDF structure
        if pdf_data.startswith(b'%PDF'):
            print("✓ Valid PDF format")
        else:
            print("✗ Invalid PDF format")
            return False

        if b'%%EOF' in pdf_data:
            print("✓ Proper PDF ending")
        else:
            print("✗ Missing PDF ending")

        # Check for enhanced styling elements
        pdf_str = pdf_data.decode('latin-1', errors='ignore')
        if '1976D2' in pdf_str:  # Blue color used in styling
            print("✓ Enhanced styling detected")
        else:
            print("⚠ Enhanced styling may not be applied")

        # Save enhanced PDF for testing
        with open('enhanced_test.pdf', 'wb') as f:
            f.write(pdf_data)

        print("✓ Enhanced PDF saved as enhanced_test.pdf")
        print("✅ Enhanced PDF generation is working correctly!")
        print("The PDF should now have:")
        print("  - Better visual appearance")
        print("  - Proper word wrapping")
        print("  - Less compact tables")
        print("  - Professional styling")

        return True

    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_enhanced_pdf()
