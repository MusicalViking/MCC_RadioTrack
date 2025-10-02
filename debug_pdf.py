#!/usr/bin/env python3
"""
Debug script for PDF generation issues
"""

import sys
import os
import traceback

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pdf_generator import generate_inventory_pdf

def debug_pdf_generation():
    """Debug PDF generation to identify issues"""
    print("Debugging PDF generation...")

    try:
        # Test with complete report type
        print("1. Testing complete report generation...")
        pdf_buffer = generate_inventory_pdf(report_type="complete")
        print(f"   ✅ PDF generated successfully, size: {len(pdf_buffer.getvalue())} bytes")

        # Write to file for inspection
        with open("debug_complete.pdf", "wb") as f:
            f.write(pdf_buffer.getvalue())
        print("   📄 Saved to: debug_complete.pdf")

        # Test with filtered report
        print("2. Testing filtered report generation...")
        pdf_buffer2 = generate_inventory_pdf(report_type="category", filter_value="Test")
        print(f"   ✅ Filtered PDF generated successfully, size: {len(pdf_buffer2.getvalue())} bytes")

        with open("debug_filtered.pdf", "wb") as f:
            f.write(pdf_buffer2.getvalue())
        print("   📄 Saved to: debug_filtered.pdf")

    except Exception as e:
        print(f"❌ Error during PDF generation: {e}")
        print("Full traceback:")
        traceback.print_exc()
        return False

    return True

if __name__ == "__main__":
    success = debug_pdf_generation()
    if success:
        print("\n🎉 Debug completed successfully!")
    else:
        print("\n💥 Debug revealed issues that need to be fixed!")
