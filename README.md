# Book Giveaway Service API

## Overview
Welcome to the Book Giveaway Service API. This service allows registered users to offer books for free and claim books offered by others. Non-registered users can view the list of available books. This repository includes user registration, book management, supporting resources, and more.

## Table of Contents
- [Features](#key-features)
- [Technology Stack](#technology-stack)
- [Getting Started](#setup)
  - [Using Virtual Environment (venv)](#using-virtual-environment-venv)
  - [Using Docker](#using-docker)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)

## Key Features
- **User Authentication:** Simple registration using just an email.
- **Books Management:** 
  - CRUD operations on books.
  - Filter books based on author, genre, etc.
- **Supporting Resources:** Manage authors, genres, book condition, images...
- **Book Retrieval Information:** Offers clarity on where to retrieve the selected book.
- **Ownership Decision:** Owners can choose the book recipient if multiple people are interested.

## Technology Stack
- Backend Framework: Django
- Database: PostgreSQL
- RESTful API
- Version Control: Git
- API Documentation: Swagger
- Containerization: Docker & Docker Compose

## Setup

### Using Virtual Environment (venv)

1. **Clone this repository**

    ```bash
    git clone https://github.com/qildeli/book_giveaway_service.git
    ```

2. **Navigate into the repository's directory**

    ```bash
    cd book_giveaway_service
    ```

3. **Create a virtual environment** (optional)

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

5. **Configure Database**

    Make sure to have PostgreSQL running and configure your database settings in `settings.py`.


6. **Run migrations**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Run the Server**

    ```bash
    python manage.py runserver
    ```
   
    Visit http://localhost:8000/ to access the API.

### Using Docker
1. **Clone this repository**

    ```bash
    git clone https://github.com/qildeli/Book_Giveaway_Service.git
    ```

2. **Navigate into the repository's directory**

    ```bash
    cd Book_Giveaway_Service
    ```
   
3. **Build and Run Containers**

    ```bash
    docker-compose build
    docker-compose up
    ```
   
    Visit http://localhost:8000/ to access the API.


## API Documentation
Access the API documentation at http://localhost:8000/swagger.