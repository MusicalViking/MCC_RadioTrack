# 📡 RadioTrack - Radio Inventory Management System

**Maine Department of Corrections - MCC Windham Tool Control System**

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org/)

## 📋 Overview

**RadioTrack** is a comprehensive radio equipment inventory management system specifically designed for the **Maine Department of Corrections** at the **MCC Windham facility**. This application provides corrections officers and supervisors with a powerful tool to track, manage, and maintain radio equipment inventory, ensuring operational readiness and accountability.

### 🎯 Purpose

- **Tool Control Compliance**: Maintain strict inventory control of radio equipment
- **Operational Readiness**: Ensure all radio equipment is properly maintained and available
- **Accountability**: Track equipment assignment, location, and condition
- **Maintenance Scheduling**: Monitor equipment condition and schedule maintenance
- **Reporting**: Generate comprehensive reports for compliance and auditing

## ✨ Features

### 🔐 **User Management**

- **Multi-level Authentication**: Employee and Corrections Supervisor roles
- **Secure Login System**: Password-based authentication with strength requirements
- **Role-based Access Control**: Different permissions for different user types
- **Employee Management**: Add, edit, and manage staff accounts

### 📊 **Inventory Management**

- **Complete Equipment Tracking**: Track all radio equipment with detailed information
- **Category Organization**: Organize equipment by type (Portable, Base Station, Mobile, etc.)
- **Location Tracking**: Monitor where equipment is stored or assigned
- **Condition Monitoring**: Track equipment condition (Excellent, Good, Fair, Poor)

### 🚨 **Alert System**

- **Poor Condition Alerts**: Immediate notifications for equipment needing attention
- **Visual Indicators**: Color-coded status displays
- **Maintenance Reminders**: Track when equipment needs service
- **Urgent Notifications**: Highlight critical maintenance needs

### 📈 **Analytics & Reporting**

- **Dashboard Overview**: Visual summary of inventory status
- **Statistical Analysis**: Equipment distribution and condition analysis
- **PDF Report Generation**: Exportable reports for compliance
- **Health Reports**: System status and database health monitoring

### 🔧 **System Administration**

- **Database Management**: Automatic backups and maintenance
- **Schema Updates**: Seamless database structure updates
- **Backup Management**: Create and restore database backups
- **System Monitoring**: Track system performance and resources

## 🛠️ Installation

### Prerequisites

- **Python 3.8+**
- **pip** package manager
- **Git** for version control
- **Docker & Docker Compose** (for containerized deployment)

### Quick Start

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd radiotrack
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize Database**

   ```bash
   python -c "from db_manager import initialize_db; initialize_db()"
   ```

4. **Run the Application**

   ```bash
   streamlit run app.py
   ```

5. **Access the Application**

   - Open your browser to `http://localhost:8501`
   - **Default admin credentials** (⚠️ **Change immediately after first login**):
     - **Username**: `admin`
     - **Password**: `RadioTrack2025!`

   **🚨 SECURITY NOTICE**: These are temporary default credentials for initial setup only. Change the admin password immediately after first login for security!

### Docker Deployment

For production deployment, use Docker:

```bash
# Clone the repository
git clone <repository-url>
cd radiotrack

# Configure environment variables in .env file
# (See DEPLOYMENT.md for details)

# Start with Docker Compose
docker-compose up -d --build
```

Access the application at `http://localhost:8501`

## 🚀 Usage

### **First Time Setup**

1. Login with default admin credentials
2. Change the admin password immediately
3. Add employee accounts as needed
4. Configure categories and locations if needed

### **Daily Operations**

1. **Login** with your assigned credentials
2. **Check Dashboard** for overview of equipment status
3. **Review Alerts** for equipment needing attention
4. **Update Inventory** as equipment is moved or serviced
5. **Generate Reports** as needed for compliance

### **For Corrections Supervisors**

- **Access Admin Dashboard** for system management
- **Manage Employee Accounts** and permissions
- **Generate Compliance Reports**
- **Oversee Equipment Maintenance** schedules
- **Monitor System Health** and backups

## 📱 User Interface

### **Dashboard Views**

- **Employee Dashboard**: Standard operational view
- **Admin Dashboard**: Management and oversight view
- **Inventory Page**: Detailed equipment listing
- **Reports**: Exportable documentation

### **Navigation**

- **Sidebar Navigation**: Easy access to all features
- **Responsive Design**: Works on desktop and mobile
- **Intuitive Controls**: User-friendly interface

## 🔒 Security Features

- **Password Hashing**: Secure password storage
- **Session Management**: Automatic logout and session control
- **Input Validation**: Comprehensive data validation
- **SQL Injection Protection**: Parameterized queries
- **Role-Based Access**: Appropriate permissions for each user type

## 📊 Database Structure

### **Core Tables**

- **employees**: User accounts and permissions
- **items**: Radio equipment inventory
- **locations**: Storage and assignment locations
- **categories**: Equipment classification
- **posts**: Internal announcements

### **Key Features**

- **Automatic Backups**: Regular database backups
- **Data Integrity**: Foreign key constraints
- **Audit Trail**: Track all changes and updates
- **Searchable**: Full-text search capabilities

## 🛠️ Development

### **Project Structure**

```
radiotrack/
├── app.py              # Main application
├── auth.py             # Authentication system
├── db_manager.py       # Database operations
├── models.py           # Data models
├── ui_components.py    # UI components
├── config.py           # Configuration
├── static/             # Images and assets
├── backups/            # Database backups
└── logs/               # Application logs
```

### **Key Technologies**

- **Frontend**: Streamlit
- **Backend**: Python
- **Database**: SQLite
- **Authentication**: Custom implementation
- **Reporting**: ReportLab (PDF generation)
- **Analytics**: Plotly (charts and graphs)

## 📋 Requirements

### **System Requirements**

- **Operating System**: Windows, macOS, or Linux
- **RAM**: 512MB minimum, 1GB recommended
- **Storage**: 100MB available space
- **Network**: Internet connection for initial setup

### **Python Dependencies**

```
streamlit==1.29.0
pandas==2.1.3
plotly==5.18.0
Pillow==10.1.0
reportlab==4.0.7
openpyxl==3.1.2
python-dotenv==1.0.0
bcrypt==4.1.1
pyotp==2.9.0
cryptography==41.0.7
schedule==1.2.0
psutil==5.9.6
requests==2.31.0
appdirs==1.4.4
```

## 📖 Documentation

### **User Manual**

- Detailed instructions available in the application
- Context-sensitive help throughout the interface
- Video tutorials (when available)

### **API Documentation**

- RESTful API endpoints (if web service enabled)
- Database schema documentation
- Integration guides

## 🤝 Contributing

### **For Maine DOC Staff**

1. Report issues through official channels
2. Suggest improvements for operational efficiency
3. Participate in user acceptance testing
4. Provide feedback on usability

### **Development Contributions**

- Fork the repository
- Create feature branches
- Submit pull requests
- Follow coding standards

## 📄 License

This software is proprietary to the **Maine Department of Corrections**. All rights reserved.

## 📞 Support

### **Technical Support**

- **Primary Contact**: Tool Control Sergeant, MCC Windham
- **IT Support**: Maine DOC IT Department
- **Emergency**: Follow established incident response procedures

### **Training**

- **Initial Training**: Provided during system rollout
- **Refresher Training**: Available as needed
- **Documentation**: Available through internal systems

## 🏆 Acknowledgments

### **Developed For**

**Maine Department of Corrections**
**MCC Windham Facility**
**Tool Control Program**

### **Special Thanks**

- Corrections Officers and Staff who provided operational requirements
- IT Department for technical infrastructure support
- Development team for creating this specialized solution

## 👨‍💻 Developer Background

### **From Resident to Developer**

This application was conceived and developed by an individual who learned programming while incarcerated in the Maine Department of Corrections education program. What began as a journey of rehabilitation and skill-building has evolved into a successful career in software development.

### **MIT's Brave Behind Bars Initiative**

The developer is now a **full-time software engineer** with **MIT's Brave Behind Bars** program - a groundbreaking initiative that provides technology education, mentorship, and employment opportunities to formerly incarcerated individuals. This program recognizes that talent exists everywhere and provides pathways to meaningful careers in technology.

### **Connect with the Developer**

- **GitHub**: ![GitHub Logo](static/12.png) [github.com/MusicalViking](https://github.com/MusicalViking)
- **LinkedIn**: Available through MIT Brave Behind Bars network
- **Portfolio**: Showcasing projects developed during incarceration and beyond

### **Mission Alignment**

RadioTrack exemplifies how **education and technology** can transform lives and create solutions that benefit correctional facilities while providing meaningful work opportunities. This project demonstrates the potential for **second chances** and the value of **investing in human potential** regardless of background.

---

**RadioTrack** - Ensuring operational excellence through comprehensive equipment management.

_Last Updated: September 2025_
