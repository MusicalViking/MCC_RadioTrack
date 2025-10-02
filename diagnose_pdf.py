#!/usr/bin/env python3
"""
Diagnostic script for PDF generation issues
"""
import sys
import os
import io

# Add current directory to path
sys.path.insert(0, os.getcwd())

def diagnose_pdf_generation():
    """Diagnose PDF generation step by step"""
    print("=== PDF Generation Diagnostics ===")

    # Step 1: Test imports
    print("\n1. Testing imports...")
    try:
        from models import get_items, get_locations
        print("   ✓ Models imported successfully")
    except Exception as e:
        print(f"   ✗ Models import failed: {e}")
        return False

    # Step 2: Test database access
    print("\n2. Testing database access...")
    try:
        items = get_items()
        locations = get_locations()
        print(f"   ✓ Retrieved {len(items)} items and {len(locations)} locations")
    except Exception as e:
        print(f"   ✗ Database access failed: {e}")
        return False

    # Step 3: Test PDF generator import
    print("\n3. Testing PDF generator import...")
    try:
        from pdf_generator import generate_inventory_pdf
        print("   ✓ PDF generator imported successfully")
    except Exception as e:
        print(f"   ✗ PDF generator import failed: {e}")
        return False

    # Step 4: Test PDF generation
    print("\n4. Testing PDF generation...")
    try:
        buffer = generate_inventory_pdf('complete')
        pdf_data = buffer.getvalue()
        print(f"   ✓ PDF generated successfully! Size: {len(pdf_data)} bytes")

        # Validate PDF structure
        if pdf_data.startswith(b'%PDF'):
            print("   ✓ Valid PDF header")
        else:
            print("   ✗ Invalid PDF header")
            return False

        if b'%%EOF' in pdf_data:
            print("   ✓ Valid PDF ending")
        else:
            print("   ✗ Missing PDF ending")

        # Save PDF
        with open('diagnostic_test.pdf', 'wb') as f:
            f.write(pdf_data)
        print("   ✓ PDF saved as diagnostic_test.pdf")

        return True

    except Exception as e:
        print(f"   ✗ PDF generation failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def check_pdf_structure():
    """Check the structure of a generated PDF"""
    print("\n5. Checking PDF structure...")

    try:
        with open('diagnostic_test.pdf', 'rb') as f:
            pdf_data = f.read()

        print(f"   PDF file size: {len(pdf_data)} bytes")

        # Check basic structure
        lines = pdf_data.split(b'\n')[:10]  # First 10 lines
        print("   First few lines:")
        for i, line in enumerate(lines):
            print(f"     {i+1}: {line[:50]}...")

        # Check for key PDF elements
        pdf_str = pdf_data.decode('latin-1', errors='ignore')
        print(f"   Contains 'RadioTrack': {'RadioTrack' in pdf_str}")
        print(f"   Contains 'endobj': {pdf_str.count('endobj')} objects")
        print(f"   Contains 'endstream': {pdf_str.count('endstream')} streams")

        return True

    except Exception as e:
        print(f"   ✗ PDF structure check failed: {e}")
        return False

if __name__ == "__main__":
    print("Starting PDF generation diagnostics...")

    # Run diagnostics
    success = diagnose_pdf_generation()

    if success:
        check_pdf_structure()
        print("\n✅ PDF generation appears to be working correctly!")
        print("The PDF should load properly in browsers.")
    else:
        print("\n❌ PDF generation has issues that need to be addressed.")
