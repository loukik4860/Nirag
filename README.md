# Nirag

### Table of Contents

1.  Project Overview

2.  Installation

3. Configuration

4. Usage

5. Contributing

6. License


Project Overview

The project consists of the following components:

* **Models**: Defines the database schema for storing information about parents, children/students, classes, and enrollments.


* **Forms**: Provides forms for creating and updating parent, child/student, class, and enrollment records.


* **Views**: Implements the logic for handling user requests and rendering HTML templates.


* **Templates**: Contains HTML templates for rendering user interfaces.


* **URLs**: Defines URL patterns for mapping user requests to view functions.



    SchoolProject/
            │
            
            ├── SchoolApp/                  # Django app for school management
            
            │   ├── migrations/             # Database migrations
 
            │   ├── __init__.py
            
            │   ├── admin.py
            
            │   ├── apps.py
            
            │   ├── models.py               # Database models
            
            │   ├── tests.py                # Unit tests
            
            │   ├── urls.py                 # URL configurations
            
            │   └── views.py                # Views (controller logic)
            
            │
            
            ├── SchoolProject/              # Django project settings
            
            │   ├── __init__.py
            
            │   ├── asgi.py
            
            │   ├── settings.py             # Project settings
            
            │   ├── urls.py                 # Root URL configurations
            
            │   └── wsgi.py
            
            │
            
            ├── static/                     # Additional static files
            
            │
            
            ├── templates/                  # Additional HTML templates
            
            │
            
            ├── .venv/                       # Python virtual environment (optional)
            
            │
            
            ├── db.sqlite3                  # SQLite database file (local development)
            
            │
            
            ├── manage.py                   # Django management script
            
            │
            
            └── README.md                   # Project README file


Install dependencies:

        pip install -r requirements.txt

Apply migrations:

        python manage.py migrate

Run the development server:

        python manage.py runserver

### Configuration

#### Database Configuration

The project uses PostgreSQL as the database backend by default. You can configure the database settings in the settings.py file located in the SchoolProject directory.

Static Files and Media Configuration

Static files (CSS, JavaScript, images) are served from the static/ directory, and media files are served from the media/ directory. You can customize these settings in the settings.py file if needed.

### Usage

Once the project is set up and running, you can access the following functionalities:

**Home Page**: View a list of parents and search for parents by name or email.


**Parents Management**:     Add, update, delete, and list parents.


**Students Management**:    Add, update, delete, and list students. Enroll students in classes.


**Classes Management**:     Add, update, delete, and list classes. View enrolled students in each class.


**Enrollments**:    Enroll students in classes and view enrolled students.


### Contributing

Contributions are welcome! If you find any bugs or want to suggest new features, feel free to open an issue or submit a pull request.



