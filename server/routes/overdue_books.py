from . import Resource
from models.book import Book
from schemas.book_schema import BookSchema
from app_setup import db
from datetime import datetime
from decorators import require_librarian

books_schema = BookSchema(many=True, session=db.session)

class OverdueBooks(Resource):
    @require_librarian
    def get(self):
        overdue_books = db.session.query(Book).filter(Book.due_date < datetime.utcnow(), Book.checked_out == True).all()
        overdue_books_data = books_schema.dump(overdue_books)
        return overdue_books_data, 200
