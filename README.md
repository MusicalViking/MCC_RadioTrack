# 📡 RadioTrack - Radio Inventory Management System

**Maine Department of Corrections - Professional Radio Equipment Management**

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com/)

---

## 🎯 **What is RadioTrack?**

**RadioTrack** is a comprehensive radio equipment inventory management system specifically designed for the **Maine Department of Corrections**. This professional-grade application provides corrections officers and supervisors with powerful tools to track, manage, and maintain radio equipment inventory with military-grade precision and accountability.

### **Mission-Critical Features**
- ✅ **Tool Control Compliance** - Maintain strict inventory control of all radio equipment
- ✅ **Operational Readiness** - Ensure all radio equipment is properly maintained and available
- ✅ **Accountability Tracking** - Monitor equipment assignment, location, and condition
- ✅ **Maintenance Scheduling** - Track equipment condition and schedule maintenance
- ✅ **Compliance Reporting** - Generate comprehensive reports for auditing and compliance

---

## 🚀 **Quick Start Guide**

### **Option 1: Instant Launch (Recommended)**
```bash
# 1. Download/Clone the repository
git clone <repository-url>
cd radiotrack

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the application
streamlit run app.py
```

### **Option 2: Docker Deployment**
```bash
# 1. Download/Clone the repository
git clone <repository-url>
cd radiotrack

# 2. Start with Docker Compose
docker-compose up -d --build
```

### **Access Your Application**
🌐 **Open your browser to:** `http://localhost:8501`

---

## 🔐 **First Login Credentials**

> ⚠️ **IMPORTANT SECURITY NOTICE**
> Change these credentials immediately after first login!

**Default Administrator Account:**
- **Username:** `admin`
- **Password:** `Admin@123!`

**After Login:**
1. Click your profile in the sidebar
2. Navigate to "Change Password"
3. Set a strong, unique password
4. Add additional employee accounts as needed

---

## ✨ **Key Features**

### **👥 User Management System**
- **Dual-Role Architecture**: Employee and Corrections Supervisor roles
- **Secure Authentication**: bcrypt password hashing with strength requirements
- **Role-Based Access Control**: Granular permissions for different user types
- **Employee Lifecycle Management**: Complete user account administration

### **📦 Advanced Inventory Management**
- **Comprehensive Equipment Tracking**: Detailed information for all radio assets
- **Smart Categorization**: 12 predefined categories (Portable, Base Station, Mobile, etc.)
- **Location Intelligence**: 18 predefined locations with real-time tracking
- **Condition Monitoring**: 5-tier condition system (Excellent → Poor → Need for Order)

### **🚨 Intelligent Alert System**
- **Real-Time Notifications**: Instant alerts for equipment needing attention
- **Visual Status Indicators**: Color-coded condition displays
- **Maintenance Intelligence**: Automated tracking of service requirements
- **Critical Alerts**: Highlight equipment requiring immediate action

### **📊 Analytics & Business Intelligence**
- **Executive Dashboard**: Visual summary of inventory health
- **Advanced Analytics**: Equipment distribution and utilization analysis
- **Professional Reporting**: PDF reports with charts and graphs
- **System Health Monitoring**: Database and application performance metrics

### **🔧 Enterprise Administration**
- **Automated Backups**: Scheduled database backups with retention policies
- **Schema Management**: Seamless database updates and migrations
- **Backup Recovery**: Point-in-time restore capabilities
- **System Monitoring**: Real-time performance and resource tracking

---

## 📋 **Detailed Installation Guide**

### **System Requirements**
- **Operating System**: Windows 10/11, macOS 10.15+, or Linux (Ubuntu 18.04+)
- **Python Version**: 3.8 or higher (3.11 recommended)
- **RAM**: 1GB minimum, 2GB recommended
- **Storage**: 500MB available space
- **Network**: Internet connection for initial setup

### **Method 1: Standard Python Installation**

#### **Step 1: Environment Setup**
```bash
# Verify Python installation
python --version
# Should show: Python 3.8.0 or higher

# Verify pip installation
pip --version
# Should show: pip 22.0 or higher
```

#### **Step 2: Download & Setup**
```bash
# Clone the repository
git clone <repository-url>
cd radiotrack

# Create virtual environment (recommended)
python -m venv radiotrack-env
source radiotrack-env/bin/activate  # On Windows: radiotrack-env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### **Step 3: Database Initialization**
```bash
# Initialize the database
python -c "from db_manager import initialize_db; initialize_db()"
```

#### **Step 4: Launch Application**
```bash
# Start the application
streamlit run app.py

# Alternative: Run in background
nohup streamlit run app.py > radiotrack.log 2>&1 &
```

### **Method 2: Docker Deployment**

#### **Prerequisites**
- Docker Desktop 4.0+
- Docker Compose 2.0+

#### **Quick Docker Setup**
```bash
# Clone repository
git clone <repository-url>
cd radiotrack

# Configure environment (optional)
cp .env.example .env
# Edit .env with your settings

# Deploy with Docker Compose
docker-compose up -d --build

# View logs
docker-compose logs -f radiotrack

# Stop the application
docker-compose down
```

### **Method 3: Production Deployment**
See `DEPLOYMENT.md` for detailed production deployment instructions including:
- Load balancing configuration
- SSL/TLS setup
- Database optimization
- Monitoring and logging

---

## 📱 **User Interface Overview**

### **Dashboard Views**

#### **Employee Dashboard**
- **Post Box**: Internal messaging system for team communication
- **Quick Stats**: Real-time inventory overview
- **Distribution Charts**: Visual equipment analysis
- **Recent Activity**: Latest equipment updates

#### **Admin Dashboard**
- **System Overview**: Comprehensive system health metrics
- **Employee Management**: Complete user administration
- **Database Maintenance**: Backup and system management tools
- **Advanced Reporting**: Professional compliance reports

#### **Inventory Management**
- **Advanced Search**: Filter by category, location, condition
- **Bulk Operations**: Multi-item updates and exports
- **Export Capabilities**: PDF, Excel, and CSV formats
- **Audit Trail**: Complete change history

### **Navigation System**
- **Responsive Sidebar**: Intuitive navigation for all screen sizes
- **Role-Based Menus**: Context-sensitive menu options
- **Quick Actions**: Fast access to common tasks
- **Breadcrumb Navigation**: Clear location awareness

---

## 🔒 **Security & Compliance**

### **Authentication Security**
- **bcrypt Hashing**: Industry-standard password encryption
- **Session Management**: Secure session handling with timeout
- **Rate Limiting**: Protection against brute force attacks
- **Password Policies**: Enforced complexity requirements

### **Data Protection**
- **SQL Injection Prevention**: Parameterized queries throughout
- **Input Validation**: Comprehensive data validation
- **Access Control**: Role-based permission system
- **Audit Logging**: Complete activity tracking

### **Operational Security**
- **Automatic Backups**: Regular database snapshots
- **Data Integrity**: Foreign key constraints and validation
- **Error Handling**: Secure error reporting without data leakage
- **Environment Configuration**: Secure credential management

---

## 📊 **Database Architecture**

### **Core Data Model**
```
employees (👥 Users & Authentication)
├── id, username, password_hash, role
├── first_name, last_name, position
├── email, phone, created_date
└── last_login, password_change_required

items (📦 Radio Equipment Inventory)
├── id, name, category, location
├── condition, notes, created_date
├── last_modified, created_by
└── assigned_to, serial_number

posts (📌 Internal Communications)
├── id, author_username, content
├── created_date, last_modified
└── priority, category

locations & categories (📍 Reference Data)
├── id, name, description
├── active, created_date
└── last_modified
```

### **Key Relationships**
- **Users** manage **Items** with full audit trail
- **Locations** and **Categories** provide structured organization
- **Posts** enable team communication and announcements
- **All changes** are tracked with timestamps and user attribution

---

## 🛠️ **Development & Customization**

### **Project Structure**
```
radiotrack/
├── app.py                    # Main Streamlit application
├── auth.py                   # Authentication & authorization
├── db_manager.py             # Database operations & management
├── models.py                 # Data models & business logic
├── ui_components.py          # Reusable UI components
├── ui_dialogs.py             # Modal dialogs & notifications
├── config.py                 # Configuration management
├── logging_config.py         # Logging configuration
├── pdf_generator.py          # PDF report generation
├── simple_backup.py          # Database backup system
├── static/                   # Images, CSS, and assets
├── backups/                  # Database backup files
├── logs/                     # Application log files
├── data/                     # Database and data files
├── .env                      # Environment configuration
├── requirements.txt          # Python dependencies
├── Dockerfile               # Docker container definition
└── docker-compose.yml       # Docker Compose configuration
```

### **Customization Options**
- **Categories & Locations**: Modify `config.py` for your facility
- **Security Policies**: Adjust password and session settings
- **UI Branding**: Customize colors and styling in `ui_components.py`
- **Reporting**: Extend PDF reports in `pdf_generator.py`
- **Authentication**: Enhance security in `auth.py`

---

## 🔧 **Troubleshooting Guide**

### **Common Issues & Solutions**

#### **Application Won't Start**
```bash
# Check Python version
python --version

# Verify dependencies
pip list | grep streamlit

# Check for port conflicts
netstat -an | grep 8501

# Try alternative port
streamlit run app.py --server.port 8502
```

#### **Database Connection Issues**
```bash
# Check database file exists
ls -la data/inventory.db

# Verify permissions
chmod 644 data/inventory.db

# Reinitialize database
python -c "from db_manager import initialize_db; initialize_db()"
```

#### **Login Problems**
```bash
# Reset admin password
python -c "
from auth import hash_password
from db_manager import DatabaseManager
import sqlite3

# Connect to database
conn = sqlite3.connect('data/inventory.db')
cursor = conn.cursor()

# Update admin password
hashed = hash_password('Admin@123!')
cursor.execute('UPDATE employees SET password_hash = ? WHERE username = ?', (hashed, 'admin'))
conn.commit()
conn.close()
print('Admin password reset to: Admin@123!')
"
```

#### **Permission Errors**
```bash
# Fix file permissions (Linux/macOS)
chmod -R 755 radiotrack/
chmod -R 644 radiotrack/data/
chmod -R 644 radiotrack/logs/

# Fix file permissions (Windows)
# Right-click folder → Properties → Security → Edit permissions
```

#### **Docker Issues**
```bash
# Check Docker status
docker ps -a

# Clean up containers
docker-compose down
docker system prune -f

# Rebuild containers
docker-compose build --no-cache
docker-compose up -d
```

### **Getting Help**
1. **Check Logs**: `tail -f logs/radiotrack.log`
2. **Docker Logs**: `docker-compose logs -f radiotrack`
3. **Database Status**: Check `data/inventory.db` file size and modification date
4. **System Resources**: Monitor memory and disk usage

---

## 📈 **Performance & Monitoring**

### **System Health Checks**
- **Database Size**: Monitor growth in `data/inventory.db`
- **Log Files**: Regular review of `logs/` directory
- **Backup Status**: Verify backup creation in `backups/` directory
- **Memory Usage**: Monitor application resource consumption

### **Optimization Tips**
- **Regular Backups**: Configure automated backup schedules
- **Log Rotation**: Implement log file rotation for long-term deployments
- **Database Maintenance**: Regular VACUUM operations for SQLite
- **Cache Management**: Clear Streamlit cache periodically

---

## 📚 **Advanced Configuration**

### **Environment Variables**
```bash
# Create .env file
cp .env.example .env

# Configure key settings
DEBUG_MODE=True
LOG_LEVEL=INFO
SESSION_EXPIRY_HOURS=2
PASSWORD_EXPIRY_DAYS=60
```

### **Custom Categories & Locations**
Edit `config.py` to customize:
- Equipment categories specific to your facility
- Location names relevant to your operations
- Security policies and timeouts
- Branding and appearance settings

---

## 🤝 **Support & Contributing**

### **For Maine DOC Staff**
- **Primary Support**: Tool Control Sergeant, MCC Windham
- **IT Support**: Maine DOC IT Department
- **Training**: Available through internal training programs
- **Documentation**: Comprehensive user guides available

### **Technical Contributions**
- Fork the repository for custom modifications
- Submit issues for bug reports and feature requests
- Follow development best practices for code contributions
- Maintain security standards for all changes

---

## 📄 **License & Compliance**

This software is **proprietary to the Maine Department of Corrections**.

- **Copyright**: © 2025 Maine Department of Corrections
- **All Rights Reserved**
- **Authorized Use Only**: Licensed for official DOC use
- **Security Classification**: Internal Use Only

---

## 🏆 **Acknowledgments**

### **Developed For**
**Maine Department of Corrections**  
**MCC Windham Facility**  
**Tool Control Program**

### **Special Recognition**
- **Corrections Officers** who provided operational requirements
- **IT Department** for infrastructure and technical support
- **Development Team** for creating this specialized solution

### **Developer Story**
This application was conceived and developed by an individual who learned programming while incarcerated in the Maine Department of Corrections education program. What began as a journey of rehabilitation and skill-building has evolved into a successful career in software development.

The developer is now a **full-time software engineer** with **MIT's Brave Behind Bars** program - a groundbreaking initiative providing technology education, mentorship, and employment opportunities to formerly incarcerated individuals.

---

## 📞 **Contact Information**

### **Technical Support**
- **Primary Contact**: Tool Control Sergeant, MCC Windham
- **IT Support**: Maine DOC IT Department
- **Emergency Support**: Follow established incident response procedures

### **Training & Documentation**
- **Initial Training**: Provided during system rollout
- **Refresher Training**: Available as needed
- **Documentation**: Available through internal DOC systems

---

**RadioTrack** - Professional radio equipment management for corrections professionals.

_Last Updated: January 2025_
