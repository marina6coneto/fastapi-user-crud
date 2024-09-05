# FastAPI User Management API

This is a simple FastAPI application for managing users with different roles.

## Features

- Get all users
- Get a specific user by UUID
- Add a new user
- Update an existing user
- Remove a user

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Pydantic

## Installation

1. Clone the repository or download the project files.

2. Navigate to the project directory.

3. Install the required dependencies:

```sh
pip install -r requirements.txt
```

## Running the Application

Run the application with Uvicorn:

```sh
uvicorn app:app --reload
```

This will start the server at `http://127.0.0.1:8000/`.

## API Endpoints

- **GET /** : Root endpoint for a welcome message.
- **GET /api/users** : Retrieve all users.
- **GET /api/users/{id}** : Retrieve a specific user by UUID.
- **POST /api/users** : Add a new user.
- **PUT /api/users/{id}** : Update an existing user by UUID.
- **DELETE /api/users/{id}** : Remove a user by UUID.

## Models

### User

- **id**: UUID
- **first_name**: string
- **last_name**: string
- **email**: string
- **role**: List of roles (admin, aluna, instrutora)

### Role

Enum with possible values:
- 'admin'
- 'aluna'
- 'instrutora'


