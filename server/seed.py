#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc
import random
from datetime import datetime, timedelta

# Remote library imports
from faker import Faker

# local imports
from app_setup import app, db
from models.book import Book
from models.user import User

if __name__ == "__main__":
    fake = Faker()
    with app.app_context():
        print("Starting seed...")

        # Clear db
        print("Clearing db...")
        User.query.delete()
        Book.query.delete()

        # Add users
        print("Seeding users...")
        users = [
            User(librarian=True),
            User(),
            User(),
            User(),
        ]

        # Commit users to the database
        db.session.add_all(users)
        db.session.commit()

        print("Seeding library")
        isbn = int(fake.isbn13(separator=""))

        library = [
            Book(ISBN=int(fake.isbn13(separator=""))),
            Book(ISBN=int(fake.isbn13(separator=""))),
            Book(ISBN=isbn, checked_out=False),
            Book(
                ISBN=isbn,
                checked_out=True,
                due_date=datetime.now() + timedelta(weeks=2),
                user_id=2,
            ),
            Book(
                ISBN=int(fake.isbn13(separator="")),
                checked_out=True,
                due_date=datetime.now() + timedelta(weeks=2),
                user_id=2,
            ),
            Book(
                ISBN=int(fake.isbn13(separator="")),
                checked_out=True,
                due_date=datetime.now() - timedelta(weeks=1),
                user_id=3,
            ),
        ]
        # Commit library to the database
        db.session.add_all(library)
        db.session.commit()

        print("Done seeding!")
