# Food Tracker

A web-based application for tracking food intake, managing food items, and monitoring nutrition progress. Built using **Django**.

## Features

- **User Registration & Authentication**: Sign up, log in, and log out securely.
- **Add Food Items**: Maintain a database of food items with nutritional info.
- **Log Food Consumption**: Track what you eat each day.
- **View Logged Foods**: See all foods you've logged, complete with nutrition data.
- **Progress Chart**: Visualize your nutritional tracking over time.
- **User Dashboard**: Personalized homepage for each authenticated user.

## Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS (Django Templates)
- **Database**: Default SQLite (can be changed)
- **Authentication**: Django’s built-in authentication

## Installation & Setup

1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/food-tracker.git
   cd food-tracker
   ```

2. **Create a Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser (optional)**
   ```sh
   python manage.py createsuperuser
   ```

6. **Run the Development Server**
   ```sh
   python manage.py runserver
   ```

7. **Access the App**
   - Open your web browser: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Project Structure

```
CalorieTracker
│   README.md
│
└───calorie_tracker
    │   db.sqlite3
    │   manage.py
    │
    ├───calorie_tracker
    │   │   asgi.py
    │   │   settings.py
    │   │   urls.py
    │   │   wsgi.py
    │   │   __init__.py
    │   │
    │   └───__pycache__
    │           settings.cpython-313.pyc
    │           urls.cpython-313.pyc
    │           wsgi.cpython-313.pyc
    │           __init__.cpython-313.pyc
    │
    └───tracker
        │   admin.py
        │   apps.py
        │   forms.py
        │   models.py
        │   tests.py
        │   urls.py
        │   views.py
        │   __init__.py
        │
        ├───migrations
        │   │   0001_initial.py
        │   │   __init__.py
        │   │
        │   └───__pycache__
        │           0001_initial.cpython-313.pyc
        │           __init__.cpython-313.pyc
        │
        ├───templates
        │   └───tracker
        │           add_food_item.html
        │           add_food_log.html
        │           foods_logged.html
        │           home.html
        │           login.html
        │           progress_chart.html
        │           signup.html
        │
        └───__pycache__
                admin.cpython-313.pyc
                apps.cpython-313.pyc
                forms.cpython-313.pyc
                models.cpython-313.pyc
                urls.cpython-313.pyc
                views.cpython-313.pyc
                __init__.cpython-313.pyc
```

## Usage

- Register a new account or log in.
- Add food items (name, calories, protein, carbs, fats).
- Log foods you've eaten (choose food item, add date).
- View your food logs and analyze nutrition.
- Visualize your progress in the Progress Chart.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.  
For feedback and bug reports, open an issue on GitHub.


**Happy tracking! 🍎**