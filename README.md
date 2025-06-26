# crud-project-django
# Django CRUD Project

A full-featured CRUD (Create, Read, Update, Delete) application built with Django, providing a complete web interface for managing data with all basic operations.

## Features

- **Create**: Add new records through user-friendly forms
- **Read**: View and browse records with pagination and search
- **Update**: Edit existing records with form validation
- **Delete**: Remove records with confirmation prompts
- Admin interface for data management
- Responsive design for mobile and desktop
- Form validation and error handling
- User authentication (optional)

## Technologies Used

- **Backend**: Django 4.x
- **Database**: SQLite (default) / PostgreSQL / MySQL
- **Frontend**: HTML5, CSS3, Bootstrap
- **Python**: 3.8+

## Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- Git

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/django-crud-project.git
   cd django-crud-project
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   On Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure the database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   
   Open your browser and navigate to: `http://127.0.0.1:8000/`

## Project Structure

```
django-crud-project/
├── manage.py
├── requirements.txt
├── README.md
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── myapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── migrations/
│   └── templates/
│       └── myapp/
│           ├── base.html
│           ├── list.html
│           ├── detail.html
│           ├── create.html
│           └── update.html
└── static/
    ├── css/
    ├── js/
    └── images/
```

## Usage

### Basic Operations

1. **View Records**: Navigate to the home page to see all records
2. **Add New Record**: Click "Add New" button to create a record
3. **Edit Record**: Click "Edit" next to any record to modify it
4. **Delete Record**: Click "Delete" and confirm to remove a record
5. **Search**: Use the search bar to find specific records

### Admin Interface

Access the Django admin at `http://127.0.0.1:8000/admin/` using your superuser credentials to:
- Manage data through Django's built-in admin interface
- Add, edit, or delete records
- Manage users and permissions

## Configuration

### Database Settings

To use a different database, update the `DATABASES` setting in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Environment Variables

Create a `.env` file in the project root for sensitive settings:

```
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | List all records |
| GET | `/create/` | Show create form |
| POST | `/create/` | Create new record |
| GET | `/detail/<id>/` | View record details |
| GET | `/update/<id>/` | Show update form |
| POST | `/update/<id>/` | Update record |
| POST | `/delete/<id>/` | Delete record |

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## Testing

Run the test suite:

```bash
python manage.py test
```

Run with coverage:

```bash
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

## Deployment

### Using Heroku

1. Install Heroku CLI
2. Create a `Procfile`:
   ```
   web: gunicorn myproject.wsgi
   ```
3. Add `gunicorn` to requirements.txt
4. Deploy:
   ```bash
   heroku create your-app-name
   git push heroku main
   heroku run python manage.py migrate
   ```

### Using Docker

```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## Troubleshooting

### Common Issues

1. **Migration errors**: Delete migration files and run `makemigrations` again
2. **Static files not loading**: Run `python manage.py collectstatic`
3. **Database connection errors**: Check database settings and credentials
4. **Port already in use**: Use `python manage.py runserver 8001`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/django-crud-project/issues) page
2. Create a new issue with detailed description
3. Contact: [your-email@example.com]

## Acknowledgments

- Django documentation and community
- Bootstrap for responsive design
- Contributors and testers

---

**Happy Coding!** 🚀