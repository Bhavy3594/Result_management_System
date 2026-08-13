# 🎓 Student Result Management & GPA Analytics System

> **Automated Academic Grade Computation, Student Mark Sheet Generation, and Record Management System built in Python & SQLite**

A desktop application built in **Python** featuring a **Tkinter** graphical user interface and an **SQLite** database backend. Designed to streamline academic course registration, record student evaluation scores, compute grade point averages (GPA), and generate official student mark sheets.

---

## 📌 Overview

Educational institutions require reliable grade management systems to eliminate manual score calculation errors and maintain centralized academic history logs. **Result Management System** provides an all-in-one desktop administration workspace:
- **Student & Course Management:** Add, update, or remove student profiles (`student.py`) and academic courses (`course.py`).
- **Automated Score & GPA Processor:** Calculate student percentage scores, grade assignments, and Cumulative Grade Point Average (CGPA) automatically (`result.py`).
- **Mark Sheet Viewer & Export:** Search student roll numbers (`report.py`) to generate instant formatted academic mark sheets.

---

## ✨ Key Features

- 👤 **Student Registration Portal:** Record student roll number, full name, email, gender, date of birth, contact details, and admission date.
- 📚 **Course Management System:** Create new courses, set credit hours, specify course descriptions, and update course parameters.
- 🧮 **Automated Grade Computation:** Automatically converts raw exam marks into percentage ratios and standard letter grades (A+, A, B, C, F).
- 📜 **Instant Mark Sheet Generator:** Search by student ID/Roll Number to display a complete report card showing all enrolled courses, individual marks, total scores, and percentage summary.
- 📊 **Administrative Dashboard:** real-time statistics widget (`dashboard.py`) tracking total students, enrolled courses, and processed results.
- 💾 **Local Relational Storage:** Embedded SQLite database (`create_db.py`) storing transactional relational tables with foreign key integrity.

---

## 🛠️ Tech Stack & Architecture

### **Technology Stack**
- **Language:** Python (v3.10+)
- **UI Framework:** Tkinter GUI, `ttk` themed widgets, Pillow (PIL) image processing
- **Database Engine:** SQLite3 (Python Built-in `sqlite3` library)

### **Software Architecture**
The application implements a modular component architecture:
```
[ Tkinter Desktop UI (dashboard.py) ]  <--->  [ Logic Modules (student, course, result) ]  <--->  [ SQLite Database Engine (create_db.py) ]
```

---

## 📂 Project Structure

```
Result_management_System/
├── course.py            # Course registration and management interface
├── student.py           # Student profile management interface
├── result.py            # Grade entry and GPA computation module
├── report.py            # Mark sheet search and report card viewer
├── dashboard.py         # Main application navigation dashboard
├── login.py             # Admin login authentication screen
├── create_db.py         # SQLite database schema initializer
├── images/              # Dashboard icons and background graphic assets
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🚀 Setup & Execution Guide

### Prerequisites
- [Python 3.8 or higher](https://www.python.org/downloads/)
- Python PIL / Pillow library

### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Bhavy3594/Result_management_System.git
   cd Result_management_System
   ```
2. **Install Required Python Package:**
   ```bash
   pip install pillow
   ```
3. **Initialize the SQLite Database:**
   ```bash
   python create_db.py
   ```
4. **Launch Application Dashboard:**
   ```bash
   python dashboard.py
   ```

---

## 📄 License

This project is open-source software licensed under the **MIT License** — see the [LICENSE](LICENSE) file.
