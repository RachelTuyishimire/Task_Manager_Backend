# Task Manager API

## | This is the backend of the **Task Manager**, built with **Django** and **Django REST Framework**. It provides a RESTful API for creating, reading, updating, and deleting tasks.

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/RachelTuyishimire/Task_Manager_Backend.git
cd Task_Manager_Backend

```

### 2. Create a virtual environment

```
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 5. Run migrations

```
python manage.py runserver
```

---

## API Endpoints

### Base URL: `http://127.0.0.1:8000/api/tasks/`

| Endpoint | Method | Description            |
| -------- | ------ | ---------------------- |
| `/`      | GET    | Get all task           |
| `/`      | POST   | Create a new task      |
| `/{id}/` | GET    | Get a specific task    |
| `/{id}/` | PUT    | Update a specific task |
| `/{id}/` | DELETE | Delete a specific task |