from . import request, Resource
from models.book import Book
from models.user import User
from schemas.book_schema import BookSchema
from app_setup import db

books_schema = BookSchema(many=True, session=db.session)

class CheckedOutBooks(Resource):
    def get(self, id):
        checked_out_books = books_schema.dump(Book.query.filter_by(user_id=id, checked_out=True))
        return checked_out_books, 200
