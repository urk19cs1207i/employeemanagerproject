# Employee Management System

A full-stack web application for managing employees — built with **Python using Django Framework**, **HTML/CSS**, and **SQLite3**.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The Employee Management System is a web-based CRUD application that allows HR teams or admins to manage employee records efficiently. It supports adding, viewing, editing, and deleting employee data through a clean, responsive interface.

---

## Features

- Add, view, edit, and delete employee records
- Department management
- Employee profile pages with detailed information
- Responsive UI with custom HTML & CSS
- Admin panel powered by Django's built-in admin interface
- Lightweight SQLite3 database — no setup required

---

## Tech Stack

| Layer      | Technology          |
|------------|---------------------|
| Backend    | Python 3.x, Django  |
| Frontend   | HTML5, CSS3         |
| Database   | SQLite3             |
| Admin      | Django Admin        |

---

## Project Structure

```
employee-management/
├── employee_mgmt/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── employees/              # Main app
│   ├── migrations/
│   ├── templates/
│   │   └── employees/
│   │       ├── base.html
│   │       ├── employee_list.html
│   │       ├── employee_detail.html
│   │       ├── employee_form.html
│   │       └── employee_confirm_delete.html
│   ├── static/
│   │   └── employees/
│   │       └── style.css
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/employee-management.git
   cd employee-management
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. Open your browser and visit: `http://127.0.0.1:8000`

---

## Usage

| URL                        | Description                  |
|----------------------------|------------------------------|
| `/`                        | Employee list (home page)    |
| `/employees/add/`          | Add a new employee           |
| `/employees/<id>/`         | View employee details        |
| `/employees/<id>/edit/`    | Edit employee record         |
| `/employees/<id>/delete/`  | Delete employee              |
| `/admin/`                  | Django admin panel           |

---

## Screenshots

<img width="950" height="431" alt="image" src="https://github.com/user-attachments/assets/c79f59be-e238-4f8f-bc10-6bf36e5a66ff" />

<img width="935" height="392" alt="image" src="https://github.com/user-attachments/assets/8becca1c-abc7-401b-aa88-7fb30cec0230" />

<img width="935" height="416" alt="image" src="https://github.com/user-attachments/assets/dd0fd5a3-be12-4ab3-b78e-0b3e2dcfd001" />

<img width="943" height="404" alt="image" src="https://github.com/user-attachments/assets/4677a688-1215-4deb-978a-b2f0131669cb" />

<img width="367" height="437" alt="image" src="https://github.com/user-attachments/assets/1d123d94-8111-40ca-bcff-b1cf3e568d5e" />

<img width="350" height="199" alt="image" src="https://github.com/user-attachments/assets/ece37cdc-0260-4f46-a822-f3240be025ee" />

<img width="332" height="406" alt="image" src="https://github.com/user-attachments/assets/d43d12cb-76b0-4032-9398-2c1720d54d8b" />

<img width="922" height="271" alt="image" src="https://github.com/user-attachments/assets/2d7ca510-568c-4179-8221-e3c65387a1ab" />

<img width="874" height="197" alt="image" src="https://github.com/user-attachments/assets/aaceb7bc-864c-4e05-86c3-8519a2a1514c" />


## Author

**Your Name**
- GitHub: "https://github.com/urk19cs1207i"
- LinkedIn: "linkedin.com/in/jonnalagadda-akshaya"
