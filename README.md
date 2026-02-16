# FastAPI Task API

A simple, production-style CRUD API built with **FastAPI**, **PostgreSQL**, **SQLAlchemy 2.0**, and **Alembic**.
This project demonstrates a clean backend architecture, database migrations, and environment-based configuration.

---

## Tech Stack

* **Backend:** FastAPI
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy 2.0
* **Migrations:** Alembic
* **Environment Management:** python-dotenv / pydantic-settings
* **Containerization:** Docker Compose

---

## Features

* Create tasks
* Read all tasks
* Update task status
* Delete tasks
* PostgreSQL integration
* Database migrations with Alembic
* Environment-based configuration

---

## Project Structure

```
fastapi-task-api/
│
├── app/
│   ├── api/
│   ├── db/
│   ├── models/
│   ├── schemas/
│   ├── config.py
│   └── main.py
│
├── alembic/
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/fastapi-task-api.git
cd fastapi-task-api
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy the example file:

```bash
cp .env.example .env
```

---

## Running the Database (Docker)

Start PostgreSQL:

```bash
docker compose up -d
```

Check that the container is running:

```bash
docker ps
```

---

## Run Database Migrations

```bash
alembic upgrade head
```

---

## Run the API

```bash
uvicorn app.main:app --reload
```

API will be available at:

```
http://127.0.0.1:8000
```

---

## Example Endpoints

### Create Task

```
POST /tasks
```

```json
{
  "title": "Finish FastAPI project"
}
```

### Get All Tasks

```
GET /tasks
```

### Update Task

```
PUT /tasks/{id}
```

### Delete Task

```
DELETE /tasks/{id}
```

---

## Development Roadmap

* [ ] Add CRUD endpoints
* [ ] Add validation and error handling
* [ ] Add tests
* [ ] Add authentication

---

## Purpose of This Project

This repository is part of a backend engineering portfolio focused on:

* Clean API design
* Real database usage (PostgreSQL)
* Migration workflows
* Production-style project structure

---

## Author

**Loc Nguyen**
Computer Science Student – University of Texas at Arlington
Aspiring AI/ML & Backend Engineer
