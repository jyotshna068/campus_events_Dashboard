# 🎓 Campus Events Dashboard

A full-stack **Campus Events Dashboard** built using **Flask, MySQL, Bootstrap, HTML, CSS, and JavaScript** that streamlines campus event management through dedicated dashboards for **Students**, **Club Organizers**, and **Administrators**. The platform enables event discovery, registrations, event management, QR-based attendance support, certificate management, notifications, and an interactive feedback system within a responsive web interface.

---

## 📌 Features

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
