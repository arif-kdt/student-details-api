# Student Details API

Django REST Framework API for managing student records.

## Setup

```bash
git clone https://github.com/your-username/student-details-api.git
cd student-details-api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET    | /api/students/ | List all students |
| POST   | /api/students/add/ | Add a student |
| GET    | /api/students/<id>/ | Get one student |
| PUT    | /api/students/update/<id>/ | Update a student |
| DELETE | /api/students/delete/<id>/ | Delete a student |