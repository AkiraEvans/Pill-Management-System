# 💊 Pill-Management-System
A Python-based medication management system that allows users to manage pills, track intake times, and maintain medication logs.

## 🧩 Features

- Add new pills to your medication list
- Remove pills from your list
- View currently stored pills
- Log when a pill is taken
- Store medication history
- View recent pill activity
- Remove the most recent time log

## 🛠️ Technologies Used

- Python
- Object-Oriented Programming (OOP)
- File Handling

## 🏗️ Project Structure

```text
Pill-Management-System/
│
├── PillTracker.py
│   └── Main program and user interface
│
├── PillManagement.py
│   └── Handles adding, removing, and viewing pills
│
├── TimeManagement.py
│   └── Handles medication time logging and history
│
├── pills.txt
│   └── Stores saved medications
│
├── times.txt
│   └── Stores medication intake records
│
└── README.md
    └── Project documentation
```

## 📋 Requirements

- Python 3 installed on your computer

No external libraries are required.

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Pill-Management-System.git
```

### 2. Navigate into the project folder

```bash
cd Pill-Management-System
```

### 3. Run the program

### macOS / Linux

```bash
python3 PillTracker.py
```

### Windows

```bash
python PillTracker.py
```

---

## ▶️ Usage

After launching the program, use the menu options:

### Pill Management

Allows users to:
- Add pills
- Remove pills
- View current pills

### Time Management

Allows users to:
- Log when a pill was taken
- Remove the most recent log
- View medication history
- View the latest medication entry

The application stores data using text files:

- `pills.txt` → Stores saved medications
- `times.txt` → Stores medication history

---

## 📚 What I Learned

Through building this project, I gained experience with:

- Object-Oriented Programming (OOP) concepts such as classes, inheritance, and methods
- Organizing a project into multiple Python files and separating responsibilities
- Reading and writing data using file handling
- Working with user input and creating menu-driven programs
- Using Python's `datetime` module to format and manage dates and times
- Improving code structure by breaking features into separate components

## 🚀 How It Can Be Improved

Future improvements for this project could include:

- Adding a graphical user interface (GUI) for a better user experience
- Replacing text file storage with a database for better data management
- Adding user accounts and personalized medication profiles
- Including medication dosage and prescription information
- Adding automatic reminders and notifications
- Improving error handling and input validation
- Adding search and filtering options for medication history
