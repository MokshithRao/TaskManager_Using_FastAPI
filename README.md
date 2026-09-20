# Task Manager API

A simple REST API built with **FastAPI** and **MySQL** for managing tasks. This project focuses on learning the fundamentals of API development, request validation, and database integration using Python.

## Tech Stack

* Python
* FastAPI
* Pydantic
* MySQL
* MySQL Connector
* python-dotenv
* Uvicorn

## Features

* Create tasks
* Retrieve all tasks
* Retrieve a task by ID
* Update task details
* Delete tasks
* MySQL database integration
* Interactive API documentation with Swagger UI

## API Endpoints

| Method | Endpoint           | Description               |
| ------ | ------------------ | ------------------------- |
| GET    | `/`                | Returns a welcome message |
| POST   | `/create`          | Creates a new task        |
| GET    | `/tasks`           | Returns all tasks         |
| GET    | `/tasks/{task_id}` | Returns a specific task   |
| PUT    | `/update`          | Updates an existing task  |
| DELETE | `/delete`          | Deletes a task            |

## Database Configuration

Database credentials are stored in environment variables using a `.env` file.

```env
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_NAME=your_database
```

## Running the Project

Install the required dependencies:

```bash
pip install fastapi uvicorn mysql-connector-python python-dotenv
```

Start the application:

```bash
uvicorn main:api --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation is available through:

```text
http://127.0.0.1:8000/docs
```

## Learning Focus

This project is being developed as a practical introduction to **FastAPI, REST API development, Pydantic request models, and MySQL database operations**.
