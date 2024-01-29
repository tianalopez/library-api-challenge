#!/usr/bin/env python3

# Standard library imports

# Local imports
from app_setup import app, db, ma, api

# Route imports
from routes.book_by_id import BookById
from routes.books import Books
from routes.overdue_books import OverdueBooks
from routes.users import Users
from routes.return_book import ReturnBook
from routes.checked_out_books import CheckedOutBooks

# Add resources
api.add_resource(BookById, "/books/<int:id>")
api.add_resource(Books, "/books")
api.add_resource(OverdueBooks, "/books/overdue")
api.add_resource(Users, "/users")
api.add_resource(ReturnBook, "/users/<int:id>/return")
api.add_resource(CheckedOutBooks, "users/<int:id>/checkedout")


@app.route("/")
def index():
    return "<h1>Project Server</h1>"


if __name__ == "__main__":
    app.run(port=5555, debug=True)
