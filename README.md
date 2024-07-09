# Requirements App

## Introduction
This project is a simple web application built with Django for managing requirements and associated documents.
## Features
- Add, edit, and delete requirements
- Add, edit, and delete documents
- Associate documents with requirements
- View details of requirements and associated documents
- Change the validation status of documents

## Installation and Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/matteotrab/SimpleCSRManager.git
    cd SimpleCSRManager
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
    
4. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

5. **Access the application:**
    Open your web browser and go to `http://127.0.0.1:8000/`.

## Database Structure

### Models

1. **Requirement**
    - `title` (CharField): The title of the requirement.
    - `description` (TextField): The description of the requirement.
    - `created_at` (DateTimeField): The timestamp when the requirement was created.
    - `updated_at` (DateTimeField): The timestamp when the requirement was last updated.
    - `isCompliant` (BooleanField): The compliance status of the requirement.
    - `documents` (ManyToManyField): The documents associated with the requirement.

2. **Document**
    - `title` (CharField): The title of the document.
    - `description` (TextField): The description of the document.
    - `isValidated` (BooleanField): The validation status of the document.

### Relationships

- A `Requirement` can have multiple `Documents`.
- A `Document` can be associated with multiple `Requirements`.

---
A version of the app can be found at http://matteotrab.eu.pythonanywhere.com.
