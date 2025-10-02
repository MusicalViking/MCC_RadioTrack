# PyInstaller Guide for RadioTrack Application

## Overview
This guide provides detailed instructions for packaging the RadioTrack radio inventory management system into a standalone executable using PyInstaller. RadioTrack is a Streamlit-based application that manages radio equipment inventory for the Maine Department of Corrections.

## Application Structure
- **Main Entry Point**: `app.py` (contains `main()` function)
- **Database**: SQLite database (`inventory.db`)
- **Dependencies**: Streamlit, pandas, reportlab, bcrypt, pyotp, cryptography, etc.
- **Data Files**: Configuration files, logs, backups, and static assets

## Prerequisites

### 1. Python Environment
- **Python Version**: 3.8 or higher (recommended: 3.9+)
- **Architecture**: 64-bit Windows
- **Virtual Environment**: Highly recommended

### 2. Required Software
- [Python](https://python.org/downloads/) (3.8+)
- [Git](https://git-scm.com/downloads) (for cloning if needed)
- [PyInstaller](https://pyinstaller.org/) (install via pip)

### 3. System Dependencies
- Microsoft Visual C++ 14.0 or greater (required for some packages)
- Windows 10/11 (64-bit)

## Installation Steps

### Step 1: Set Up Python Environment

```bash
# Create and activate virtual environment
python -m venv radiotrack_env
radiotrack_env\Scripts\activate

# Upgrade pip
python -m pip install --upgrade pip
```

### Step 2: Install Application Dependencies

```bash
# Install all required packages
pip install -r requirements.txt

# Additional packages needed for PyInstaller
pip install pyinstaller==6.3.0
pip install pywin32==306
```

### Step 3: Verify Installation

```bash
# Test that the application runs
python app.py --help
# or
python -c "import streamlit, pandas, reportlab; print('All imports successful')"
```

## PyInstaller Configuration

### Basic PyInstaller Command

```bash
pyinstaller --onefile --windowed ^
    --name "RadioTrack" ^
    --icon "static/favicon.ico" ^
    --add-data "inventory.db;." ^
    --add-data ".env;." ^
    --hidden-import="streamlit.runtime.scriptrunner.magic_funcs" ^
    --hidden-import="sqlite3" ^
    --hidden-import="bcrypt" ^
    --hidden-import="cryptography" ^
    --hidden-import="pyotp" ^
    --collect-all="reportlab" ^
    --collect-all="pandas" ^
    --collect-all="streamlit" ^
    app.py
```

### Advanced PyInstaller Spec File

Create a file named `radiotrack.spec` in the project root:

```python
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Application info
app_name = 'RadioTrack'
app_version = '1.0.0'
main_script = 'app.py'

# Analysis
a = Analysis(
    [main_script],
    pathex=[],
    binaries=[],
    datas=[
        ('inventory.db', '.'),
        ('.env', '.'),
        ('static', 'static'),
        ('data', 'data'),
        ('backups', 'backups'),
        ('logs', 'logs'),
        ('config.py', '.'),
        ('models.py', '.'),
        ('auth.py', '.'),
        ('db_manager.py', '.'),
        ('pdf_generator.py', '.'),
        ('ui_components.py', '.'),
        ('ui_dialogs.py', '.'),
        ('logging_config.py', '.'),
    ],
    hiddenimports=[
        'streamlit.runtime.scriptrunner.magic_funcs',
        'streamlit.runtime.legacy_caching',
        'streamlit.runtime.secrets',
        'sqlite3',
        'bcrypt',
        'bcrypt._bcrypt',
        'cryptography',
        'cryptography.hazmat',
        'cryptography.hazmat.primitives',
        'pyotp',
        'reportlab',
        'reportlab.lib',
        'pandas',
        'pandas.io',
        'streamlit',
        'streamlit.components',
        'streamlit.runtime',
        'PIL',
        'PIL.Image',
        'openpyxl',
        'schedule',
        'psutil',
        'appdirs',
        'dotenv',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# Pyz
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# EXE
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=app_name,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Windowed mode for GUI
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version_file='version_info.txt',
    icon='static/favicon.ico',
)

# COLLECT
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=app_name,
)
```

### Version Information File

Create `version_info.txt`:

```text
# UTF-8

VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=(1, 0, 0, 0),
    prodvers=(1, 0, 0, 0),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
    ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        u'040904B0',
        [StringStruct(u'CompanyName', u'Maine Department of Corrections'),
        StringStruct(u'FileDescription', u'RadioTrack - Radio Inventory Management System'),
        StringStruct(u'FileVersion', u'1.0.0'),
        StringStruct(u'InternalName', u'RadioTrack'),
        StringStruct(u'LegalCopyright', u'Copyright (c) 2025 Arthur Belanger'),
        StringStruct(u'OriginalFilename', u'RadioTrack.exe'),
        StringStruct(u'ProductName', u'RadioTrack'),
        StringStruct(u'ProductVersion', u'1.0.0')])
      ]),
    VarFileInfo(
      [VarStruct(u'Translation', [1033, 1200])])
  ]
)
```

## Building the Executable

### Method 1: Using Command Line

```bash
# Activate virtual environment
radiotrack_env\Scripts\activate

# Build with basic options
pyinstaller --onefile --windowed ^
    --name "RadioTrack" ^
    --icon "static/favicon.ico" ^
    --add-data "inventory.db;." ^
    --add-data ".env;." ^
    app.py
```

### Method 2: Using Spec File

```bash
# Build using spec file
pyinstaller radiotrack.spec
```

### Method 3: Advanced Build with All Features

```bash
# Comprehensive build command
pyinstaller --onefile --windowed ^
    --name "RadioTrack" ^
    --icon "static/favicon.ico" ^
    --add-data "inventory.db;." ^
    --add-data ".env;." ^
    --add-data "static;static" ^
    --add-data "data;data" ^
    --add-data "backups;backups" ^
    --add-data "logs;logs" ^
    --hidden-import="streamlit.runtime.scriptrunner.magic_funcs" ^
    --hidden-import="sqlite3" ^
    --hidden-import="bcrypt" ^
    --hidden-import="cryptography" ^
    --hidden-import="pyotp" ^
    --collect-all="reportlab" ^
    --collect-all="pandas" ^
    --collect-all="streamlit" ^
    --upx-dir="C:\upx\upx.exe" ^
    --version-file="version_info.txt" ^
    app.py
```

## Post-Build Steps

### 1. Test the Executable

```bash
# Navigate to dist folder
cd dist

# Run the executable
RadioTrack.exe
```

### 2. Create Portable Package

```bash
# Create a portable folder
mkdir RadioTrack_Portable
cd RadioTrack_Portable

# Copy executable and required files
copy ..\dist\RadioTrack.exe .
copy ..\inventory.db .
copy ..\.env .
xcopy /E /I ..\static static
xcopy /E /I ..\data data
xcopy /E /I ..\backups backups
xcopy /E /I ..\logs logs

# Create startup batch file
echo @echo off > start.bat
echo title RadioTrack - Radio Inventory Management System >> start.bat
echo echo Starting RadioTrack... >> start.bat
echo RadioTrack.exe >> start.bat
echo pause >> start.bat
```

### 3. Create Installer (Optional)

For distribution, consider creating an installer using:
- [Inno Setup](https://jrsoftware.org/isinfo.php)
- [NSIS](https://nsis.sourceforge.io/)
- [Advanced Installer](https://www.advancedinstaller.com/)

## Troubleshooting

### Common Issues

#### 1. Import Errors
**Problem**: `ModuleNotFoundError` for hidden modules
**Solution**:
```bash
# Add missing hidden imports to spec file
hiddenimports=[
    'sqlite3',
    'bcrypt',
    'cryptography.hazmat.primitives',
    # ... other missing modules
]
```

#### 2. Database Connection Issues
**Problem**: SQLite database not found or accessible
**Solution**:
- Ensure `inventory.db` is included in `--add-data`
- Check file permissions
- Verify database path in application

#### 3. Missing DLL Errors
**Problem**: `DLL load failed` errors
**Solution**:
```bash
# Install missing system dependencies
pip install pywin32
# or manually install Microsoft Visual C++ Redistributables
```

#### 4. Large Executable Size
**Problem**: Executable is too large (>500MB)
**Solutions**:
- Use `--upx` for compression
- Remove unnecessary packages from requirements.txt
- Use virtual environment for building

#### 5. Streamlit-Specific Issues
**Problem**: Streamlit runtime errors
**Solution**:
```python
# Add to spec file hidden imports
hiddenimports=[
    'streamlit.runtime.scriptrunner.magic_funcs',
    'streamlit.runtime.legacy_caching',
    'streamlit.runtime.secrets',
]
```

### Debug Mode

For troubleshooting, build in debug mode:

```bash
pyinstaller --debug=all ^
    --windowed ^
    --name "RadioTrack" ^
    app.py
```

## Distribution Considerations

### 1. File Structure for Distribution

```
RadioTrack/
├── RadioTrack.exe          # Main executable
├── inventory.db           # Database file
├── .env                   # Configuration
├── static/                # Static assets
├── data/                  # Data files
├── backups/               # Backup files
├── logs/                  # Log files
├── README.txt             # User instructions
└── start.bat              # Startup script
```

### 2. System Requirements for End Users

**Minimum Requirements:**
- Windows 10/11 (64-bit)
- 4 GB RAM
- 500 MB free disk space
- Internet connection (for initial setup)

**Recommended Requirements:**
- Windows 10/11 (64-bit)
- 8 GB RAM
- 1 GB free disk space
- Reliable internet connection

### 3. Security Considerations

1. **Database Security**: SQLite database is portable but not encrypted
2. **Environment Variables**: Store sensitive data securely
3. **Code Signing**: Consider code signing for distribution
4. **Antivirus**: Some antivirus may flag PyInstaller executables

### 4. User Instructions

Create a `README.txt` for end users:

```text
RadioTrack - Radio Inventory Management System
=============================================

Installation:
1. Extract all files to a folder
2. Double-click start.bat or RadioTrack.exe
3. The application will open in your default browser

First Time Setup:
1. Create an admin account when prompted
2. Configure database location if needed
3. Set up backup preferences

Support:
- Check logs folder for error details
- Contact system administrator for issues

Version: 1.0.0
Copyright (c) 2025 Arthur Belanger
```

## Performance Optimization

### Build Optimizations

```bash
# Optimized build command
pyinstaller --onefile ^
    --windowed ^
    --upx-dir="C:\upx\upx.exe" ^
    --exclude-module="tkinter" ^
    --exclude-module="unittest" ^
    --name "RadioTrack" ^
    app.py
```

### Runtime Optimizations

1. **Lazy Loading**: Import heavy modules only when needed
2. **Database Optimization**: Add indexes for large datasets
3. **Caching**: Implement proper caching strategies

## Advanced Features

### 1. Auto-Updater

For production deployment, consider adding an auto-updater:

```python
# Example update check (implement securely)
def check_for_updates():
    # Check version against server
    # Download and install updates
    pass
```

### 2. Configuration Management

```python
# Centralized configuration
def load_config():
    config = {
        'database_path': 'inventory.db',
        'backup_path': 'backups',
        'log_level': 'INFO',
    }
    return config
```

## Support and Maintenance

### Regular Tasks

1. **Backup Database**: Regular database backups
2. **Update Dependencies**: Keep packages updated
3. **Monitor Logs**: Check application logs regularly
4. **User Training**: Train users on new features

### Troubleshooting Resources

1. **Log Files**: Check `logs/` directory for errors
2. **Configuration**: Verify `.env` file settings
3. **Dependencies**: Ensure all required packages are installed
4. **Permissions**: Check file and directory permissions

## Conclusion

This PyInstaller configuration will create a standalone executable of the RadioTrack application that can be distributed and run on Windows systems without requiring Python installation. The executable includes all necessary dependencies, data files, and configurations for complete functionality.

For production deployment, consider additional steps like code signing, installer creation, and automated update mechanisms based on your specific requirements.
```

## Summary

I have created a comprehensive markdown file (`pyinstaller_guide.md`) that provides detailed instructions for packaging your RadioTrack application using PyInstaller. The guide covers:

1. **Prerequisites** - Python environment setup and required software
2. **Installation Steps** - Virtual environment creation and dependency installation  
3. **PyInstaller Configuration** - Multiple build methods with spec file examples
4. **Building Process** - Step-by-step build instructions with various options
5. **Post-Build Tasks** - Testing, packaging, and distribution preparation
6. **Troubleshooting** - Common issues and solutions
7. **Advanced Features** - Performance optimizations and deployment considerations

The guide is specifically tailored to your RadioTrack application, taking into account:
- Streamlit framework requirements
- SQLite database dependency
- PDF generation with ReportLab
- Authentication modules (bcrypt, pyotp, cryptography)
- Static files and data directories
- Windows-specific optimizations

You can now use this guide to create a standalone executable that can be distributed to users without requiring Python installation on their systems.
