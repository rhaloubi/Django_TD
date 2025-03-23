# Student Management System

A Django-based web application for managing students and courses at an engineering school.

## Features

### Student Management
- Add, edit, and delete student records
- View student details
- Track student course enrollments

### Course Management
- Create, update, and delete courses
- View course details
- Manage student enrollments

## Prerequisites
- Python 3.x
- Django 5.1.7
- SQLite3 (included with Django)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd studant_app
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install django
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

## Project Structure
```
studant_app/
├── etudiants/          # Student management app
├── cours/              # Course management app
├── templates/          # HTML templates
│   ├── base.html
│   ├── etudiants/
│   └── cours/
└── studant_app/        # Main project directory
```

## Usage

1. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

2. **Access the application:**
   - Admin interface: [http://localhost:8000/admin/](http://localhost:8000/admin/)
   - Student management: [http://localhost:8000/etudiants/](http://localhost:8000/etudiants/)
   - Course management: [http://localhost:8000/cours/](http://localhost:8000/cours/)

## Models

### Student (Etudiant)
- First Name (`prenom`)
- Last Name (`nom`)
- Date of Birth (`date_naissance`)
- Email (`email`)

### Course (Cours)
- Title (`titre`)
- Description (`description`)
- Course Code (`code_cours`)
- Students (Many-to-Many relationship)

### Enrollment (Inscription)
- Student (Foreign Key)
- Course (Foreign Key)
- Enrollment Date (`date_inscription`)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m "Add new feature"`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

