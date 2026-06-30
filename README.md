
# 🎓 Campus Events Dashboard

A full-stack web application that enables colleges to efficiently manage campus events through a centralized platform. Students can explore, register for, and track upcoming events, while club organizers can create and manage events, monitor registrations, generate QR-based attendance, and issue participation certificates.

---

## 📌 Project Overview

Campus Events Dashboard is a role-based event management system developed using **Flask**, **MySQL**, **HTML**, **CSS**, **JavaScript**, and **Bootstrap**. It provides a complete workflow for organizing, managing, and participating in college events.

The platform supports two primary user roles:

- **Students**
- **Club Organizers**

An optional **Admin Panel** can be used for managing users and approving club organizers.

---

## 🚀 Features

### 👤 Authentication & Authorization

- Student Registration & Login
- Club Organizer Registration & Login
- Password Hashing
- Session Management using Flask-Login
- Role-Based Access Control
- Logout Functionality

---

### 📅 Event Management

### -> Club Organizers

- Create Events
- Edit Events
- Delete Events
- Upload Event Images
- Add Event Description
- Set Event Venue
- Set Event Date & Time
- Select Event Category
- Publish Upcoming Events

### -> Students

- Browse Upcoming Events
- View Event Details
- Register for Events
- Search Events
- Filter Events by
  - Club
  - Category
  - Date

---

### 📖 Event Details

Each event contains:

- Event Title
- Description
- Venue
- Date & Time
- Organizer Details
- Event Image
- Registration Button
- Google Calendar Integration
- Event Status

---

### 📆 Calendar Integration

Students can directly add events to:

- Google Calendar
- iCal Compatible Applications

---

### 📝 Event Registration

Students can

- Register for Events
- View Registered Events
- Cancel Registration
- Receive Registration Confirmation

Organizers can

- View Registered Participants
- Export Participant Lists

---

### 📱 QR Code Attendance

For every registered participant

- Generate Unique QR Code
- Scan QR Code During Event
- Automatically Mark Attendance
- Prevent Duplicate Attendance

---

### 🏆 Certificate Generation

After attendance verification

- Generate Participation Certificate
- PDF Certificate
- Student Name
- Event Name
- Organizer Signature
- Download Certificate

---

### 🖼 Past Events

- Past Event Gallery
- Uploaded Event Images
- Event Summary
- Event Statistics

---

### 💬 Comments & Feedback

Students can

- Comment on Events
- Like/Dislike Comments
- Reply to Comments
- Submit Suggestions

---

### 🔔 Notifications

Email Notifications for

- Registration Confirmation
- Event Reminder
- Certificate Availability
- New Event Announcements

In-App Notifications

- Upcoming Events
- New Comments
- Event Updates

---

### 📊 Student Dashboard

Students can

- View Registered Events
- View Upcoming Events
- Track Attendance
- Download Certificates
- Calendar View
- Notification Center

---

### 🛠 Organizer Dashboard

Organizers can

- Manage Events
- Create/Edit/Delete Events
- Upload Event Media
- View Registrations
- Track Attendance
- Generate Certificates
- View Event Analytics

---

### 👨‍💼 Admin Panel 

- Manage Users
- Approve Club Organizers
- Manage Clubs
- Remove Events
- View System Statistics

---

## 🏗 Tech Stack

### Backend

- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-Mail
- Flask-Migrate

### Database

- MySQL

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Additional Libraries

- PyMySQL
- ReportLab
- QRCode
- Pillow
- Pandas
- OpenPyXL

---

## 📂 Project Structure

```
Campus_Events_Dashboard/
│
├── app.py
├── config.py
├── extensions.py
├── requirements.txt
│
├── models/
│   ├── user.py
│   ├── event.py
│   ├── registration.py
│   ├── attendance.py
│   ├── certificate.py
│
├── routes/
│   ├── auth.py
│   ├── student.py
│   ├── organizer.py
│   ├── admin.py
│   ├── events.py
│
├── utils/
│   ├── calendar_utils.py
│   ├── qr_utils.py
│   ├── email_utils.py
│   ├── certificate_utils.py
│   └── reminder_scheduler.py
│
├── templates/
├── static/
├── uploads/
└── certificates/
```

---

## Highlights

- Designed and developed a role-based campus event management platform using Flask and MySQL.
- Implemented secure authentication, event registration, QR-based attendance, and automated certificate generation.
- Integrated email notifications and Google Calendar support for event reminders.
- Built responsive dashboards for students and organizers with complete event lifecycle management.
- Developed a scalable modular architecture using Flask Blueprints, SQLAlchemy ORM, and Bootstrap.

---

## ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/campus-events-dashboard.git
cd campus-events-dashboard
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure MySQL

Create Database

```sql
CREATE DATABASE campus_events_db;
```

Update `config.py`

```python
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@localhost/campus_events_db"
```

---

### Run Application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

### Database Tables

- Users
- Events
- Registrations
- Attendance
- Certificates
- Comments
- Notifications

---

# License

This project is intended for educational and academic purposes.

---

## 👩‍💻 Author

**Jyotshna Devi Gavireddy**

Developed as a comprehensive Full Stack Web Development project using Flask, MySQL, Bootstrap, HTML, CSS, and JavaScript.
### 👨‍🎓 Student Module

* Secure login and registration
* Browse upcoming and past events
* Search and filter events
* Register for events
* View detailed event information
* Participate in event discussions through comments and replies
* Like and dislike comments
* View notifications
* Access registered events dashboard
* Download participation certificates
* Verify certificates

---

### 👨‍💼 Club Organizer Module

* Organizer dashboard
* Create new events
* Edit existing events
* Delete events
* Upload event banner images
* Manage event registrations
* Generate QR codes for attendance
* View attendance reports

---

### 👨‍💻 Admin Module

* Admin dashboard
* View platform statistics
* Manage users
* Approve or reject organizer requests
* Manage campus events
* Delete users and events

---

## 🚀 Technologies Used

### Backend

* Python
* Flask
* SQLAlchemy
* MySQL

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript

### Database

* MySQL

### Tools

* Git
* GitHub

---

## 📂 Project Structure

```
Campus-Events-Dashboard/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── models/
├── routes/
├── templates/
├── static/
└── utils/
```

---

## 📊 User Roles

### Student

* Register and log in
* Explore campus events
* Register for events
* Participate in discussions
* Receive notifications
* Download certificates

### Club Organizer

* Create and manage events
* Upload event banners
* View registrations
* Generate attendance QR codes
* Monitor attendance reports

### Administrator

* Approve organizer requests
* Manage users
* Manage events
* Monitor platform activity

---

## 📷 Screens Included

* Home Page
* Login
* Signup
* Student Dashboard
* Organizer Dashboard
* Admin Dashboard
* Event Details
* Event Registration
* Notifications
* Certificates
* Attendance Report
* Event Management

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/jyotshna068/campus-events-Dashboard.git
cd campus-events-Dashboard
```

---

### Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure MySQL

Create a MySQL database:

```sql
CREATE DATABASE campus_events_db;
```

Update your `config.py` with your MySQL credentials.

Example:

```python
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@localhost/campus_events_db"
```

---

### Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 👩‍💻 Author

**Jyotshna Devi Gavireddy**

---

## 📄 License

This project is developed for educational and portfolio purposes.
