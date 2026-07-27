# Student Result Management System

A Desktop Application built with Python and Tkinter for managing student records, course details, exam results, and generating student performance reports.

Developed by **Atkotiya Bhavy (92300527183)**.

---

## 🌟 Features

- **Login & Authentication**: Secure admin login system.
- **Dashboard**: Interactive summary view showing total courses, total students, and total results along with a dynamic live clock.
- **Course Management**: Add, update, delete, and view course details (duration, charges, description).
- **Student Management**: Register new students, update records, and search student details by roll number.
- **Result Management**: Add and manage student marks and calculate overall percentages.
- **View Results**: Search and view detailed student result cards.

---

## 🛠️ Technology Stack

- **GUI Framework**: Python `tkinter`
- **Database**: `sqlite3`
- **Image Processing**: `Pillow` (`PIL`)

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3 installed. You will also need Pillow:

```bash
pip install Pillow
```

### Database Setup

Initialize the SQLite database (`rms.db`) by running:

```bash
python create_db.py
```

### Running the Application

To launch the login screen:

```bash
python login.py
```

Or to launch the main dashboard directly:

```bash
python dashboard.py
```

---

## 📁 Project Structure

```
Result_management_System/
├── create_db.py     # Database initialization script
├── login.py         # Login GUI interface
├── dashboard.py     # Main application dashboard
├── course.py        # Course management module
├── student.py       # Student management module
├── result.py        # Result entry & management module
├── report.py        # Result search & report module
├── rms.db           # SQLite database
├── images/          # Application icons and background assets
└── Report Files/    # Project documentation (RMS.docx, RMS.pptx)
```

---

## 📜 License

This project is open-source and available for educational purposes.
