# 🎓 Student Result Management System

A Python-based Student Result Management System built using Object-Oriented Programming (OOP). This application allows users to manage student records, calculate grades, and store data permanently using JSON.

## 📌 Project Overview

This project is a console-based application developed in Python. It helps users perform basic student record management operations such as adding, viewing, searching, updating, and deleting student records. Student data is automatically saved to and loaded from a JSON file, ensuring data is preserved between program runs.

## ✨ Features

- Add new student records
- Display all student records
- Search students by roll number
- Update student marks
- Delete student records
- Calculate total marks automatically
- Calculate percentage automatically
- Generate grades based on percentage
- Save student data to a JSON file
- Load student data automatically when the program starts
- Handle missing data files using exception handling

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON (for data storage)
- File Handling
- Git
- GitHub

## 📂 Project Structure

```text
student-result-management-system/
│
├── main.py           # Main program with menu and CRUD operations
├── student.py        # Student class and methods
├── students.json     # Stores student records
├── .gitignore        # Ignores unnecessary files
└── README.md         # Project documentation
```

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/radhapaswan0625/student-result-management-system.git
```

2. Navigate to the project folder:

```bash
cd student-result-management-system
```

3. Run the program:

```bash
python main.py
```