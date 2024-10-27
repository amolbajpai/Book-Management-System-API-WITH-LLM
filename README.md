Here’s your `README.md` file for the Book Management System API, with corrected formatting for the markdown issues:

```markdown
# Book Management System API WITH LLM

## Overview

This API provides a set of endpoints to manage a book collection, allowing users to perform CRUD operations on books, add reviews, and generate book summaries using an LLM (Large Language Model). The API is built using FastAPI and supports user authentication.

## Features

- Retrieve a list of all books
- Retrieve details of a specific book
- Add, retrieve, and delete reviews for books
- Generate summaries for books using LLM
- Retrieve personalized book recommendations

## Getting Started

### Prerequisites

- Python 3.8 or higher (Recommended 3.11)
- FastAPI
- SQLAlchemy
- AsyncSQLAlchemy
- Pydantic
- uvicorn

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/amolbajpai/Book-Management-System-API-WITH-LLM.git
   cd Book-Management-System-API-WITH-LLM
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database and migrations (if using Alembic or similar).

4. Run the API:

   ```bash
   uvicorn main:app --reload
   ```

## Environment Variables

Create a file named `.env` in the root directory of the project with the following content:

```plaintext
GROQ_API_KEY=your_key
SECRET_KEY=your_secret_key
DATABASE_URL=postgres://user:pwd@localhost:5432/book_management
```

- **GROQ_API_KEY**: Your API key for the GROQ service.
- **SECRET_KEY**: A secret key used for securing your application.
- **DATABASE_URL**: Connection string for your PostgreSQL database in the format:
  - `postgres://YourUserName:YourPassword@YourHostname:5432/YourDatabaseName`
    - Replace `user` with your username.
    - Replace `pwd` with your password.
    - `localhost` is the hostname where your database is running.
    - `5432` is the default port number for PostgreSQL.
    - `book_management` is the name of the database to connect to.

## API Endpoints

### Endpoints Requiring User Authentication

These endpoints require the user to be logged in (authenticated):

1. **Get All Books**
   - `GET /books`
   
2. **Get Book by ID**
   - `GET /books/{id}`

3. **Delete Book by ID**
   - `DELETE /books/{id}`

4. **Add Review**
   - `POST /books/{id}/reviews`

5. **Get Reviews for a Book**
   - `GET /books/{id}/reviews`

6. **Get Book Summary**
   - `GET /books/{book_id}/summary`

7. **Get Book Recommendations using LLM**
   - `GET /recommendations`

8. **Get Current User's Details**
   - `GET /whoami`

### Endpoints Requiring Admin Authentication

These endpoints require the user to have an admin role:

1. **Generate Book Summary using LLM**
   - `POST /books/{id}/generate-summary`

## Summary

- **User Authentication Required:** 
  - `GET /books`
  - `GET /books/{id}`
  - `PUT /books/{id}`
  - `DELETE /books/{id}`
  - `POST /books/{id}/reviews`
  - `GET /books/{id}/reviews`
  - `GET /books/{book_id}/summary`
  - `GET /recommendations`
  - `GET /whoami`
```