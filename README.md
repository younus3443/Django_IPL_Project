🏏 Django IPL Data Analysis Project

📌 Project Objective

This project is built using Django to analyze IPL (Indian Premier League) data using Django ORM.
The goal is to understand:

- Django MVT (Model–View–Template)

- Django ORM (joins, aggregations, migrations)

- Database transactions (atomic)

- Custom Django management commands

- JSON APIs and chart visualization using HighCharts

🛠 Tech Stack

- **Backend:** Django, Python

- **Database:** SQLite

- **ORM:** Django ORM

- **Frontend:** Django Templates, HighCharts (JavaScript)

- **Dataset:** IPL CSV files (matches.csv, deliveries.csv)

📂 Dataset Used

Only IPL dataset is used:

- matches.csv

- deliveries.csv

⚙️ Setup Instructions

1️⃣ Clone the Repository

    git clone <repo-url>
    cd django-ipl-project

2️⃣ Create Virtual Environment

    python -m venv venv
    source venv/bin/activate

3️⃣ Install Dependencies

    pip install django

4️⃣ Run Migrations

    python manage.py makemigrations
    python manage.py migrate

📁 Project Structure

```
ipl/
│
├── analysis/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── tests.py
│   ├── __init__.py
│   │
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_rename_balls_delivery_ball.py
│   │   └── __init__.py
│   │
│   └── management/
│       ├── __init__.py
│       └── commands/
│           ├── __init__.py
│           └── import_ipl_data.py
│
├── data/
│   ├── matches.csv
│   └── deliveries.csv
│
├── ipl/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
│
├── templates/
│   ├── matches.html
│   ├── matches_won.html
│   ├── extra_runs_2016.html
│   └── Top_10_bowler_2015.html
│
├── .gitignore
├── README.md
├── requirements.txt
├── manage.py
├── db.sqlite3

```

🎯 Learning Outcomes

- Strong understanding of Django ORM queries

- Hands-on experience with database transactions

- Ability to build real-world analytical APIs

- Integration of backend APIs with frontend charts