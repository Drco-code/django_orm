📚 Django ORM Learning Project

Welcome to the Django ORM Learning Project! This repository is dedicated to mastering Django's Object-Relational Mapping (ORM), which allows developers to interact with databases using Python instead of raw SQL.

🚀 Project Overview

Django ORM provides a powerful abstraction layer over databases, making data handling more efficient and readable. This project covers:

🏗️ Defining models and migrations

🔍 Querying data using ORM

🔄 Performing CRUD operations

🔗 Working with relationships (One-to-One, One-to-Many, Many-to-Many)

📊 Filtering and optimizing queries

🖥️ Using the Django shell for database interaction

⚡ Getting Started

🔹 Clone the Repository

git clone https://github.com/your-username/django_orm.git

  cd django_orm

🔹 Set Up a Virtual Environment

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate    # Windows

🔹 Install Dependencies

pip install -r requirements.txt

🔹 Apply Migrations

python manage.py makemigrations
python manage.py migrate

🔹 Create a Superuser (Optional for Admin Panel)

python manage.py createsuperuser

🔹 Run the Development Server

python manage.py runserver

Visit http://127.0.0.1:8000/admin/ to access the Django Admin Panel.

🛠️ Working with Django ORM

🔹 Create a New Record

from app.models import Book
book = Book.objects.create(title="Django for Beginners", author="William S. Vincent", published_date="2023-01-15")

🔹 Retrieve All Records

books = Book.objects.all()

🔹 Filter Records

django_books = Book.objects.filter(author="William S. Vincent")

🔹 Update a Record

restaurant = Restaurant.objects.get(id=1)
book.title = "Django Advanced"
book.save()

🔹 Delete a Record

book = Book.objects.get(id=1)
book.delete()

🔄 Handling Migrations & Data Backup

🔹 Export Database Data

python manage.py dumpdata --exclude auth.permission --exclude contenttypes > data.json

🔹 Import Data After Cloning

python manage.py loaddata data.json

🔥 Git Best Practices for This Project

🔹 Ignore Database Files

Add this to .gitignore:

# Ignore database file
db.sqlite3

🔹 Push Changes to GitHub

git add .
git commit -m "Updated models and migrations"
git push origin main

🤝 Contributing

If you have improvements, feel free to fork the repository, create a new branch, and submit a pull request!

📜 License

This project is open-source.

Happy coding! 🚀
