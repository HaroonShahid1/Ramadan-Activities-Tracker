# Ramadan Tracker

Ramadan Tracker is a Django web application that allows users to track their activities during the Ramadan month.

## Features

- Record daily activities, including date, day, Quran recitation, and prayers.
- Optional checkbox for Tahajjud prayer.
- View a list of recorded activities.

## Getting Started

### Prerequisites

- Python 3.6+
- Django

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/RamadanTracker.git
    cd RamadanTracker
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # Unix/Mac
    .\env\Scripts\activate  # Windows
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser account:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the application:**

    Visit http://your_localhost_url/tracker/record/ to use the application.

## Usage

1. Log in to the Django Admin panel using the superuser account created.
2. Record your daily activities using the provided form.
