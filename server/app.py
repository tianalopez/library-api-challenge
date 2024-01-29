#!/usr/bin/env python3

# Standard library imports

# Local imports
from app_setup import app, db, ma, api

# Route imports
from routes.book_by_id import BookById
from routes.books import Books
from routes.overdue_books import OverdueBooks
from routes.users import Users

# Add resources
api.add_resource(BookById, "/books/<int:id>")
api.add_resource(Books, "/books")
api.add_resource(OverdueBooks, "/books/overdue")
api.add_resource(Users, "/users")


@app.route("/")
def index():
    return "<h1>Project Server</h1>"


if __name__ == "__main__":
    app.run(port=5555, debug=True)
