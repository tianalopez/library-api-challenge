from . import request, Resource
from models.book import Book
from models.user import User
from schemas.book_schema import BookSchema
from app_setup import db
from datetime import datetime

book_schema = BookSchema(session=db.session)
#!user can only have 3 checked out books
#!user can have no overdue books
    #~take the user_id, check if they have any overdue books, check how many books have been checked out

class CheckoutBook(Resource):
    def patch(self, ISBN):
        if book := db.session.query(Book).filter_by(ISBN == ISBN).first():
            try:
                data = request.json
                # Validate data
                book_schema.validate(data)
                # Deserialize data and allow for partial updates
                updated_book = book_schema.load(data, instance=book, partial=True)
                db.session.commit()
                # Serialize the data and package your JSON response
                return book_schema.dump(updated_book), 200
            except Exception as e:
                db.session.rollback()
                return {"error": str(e)}, 400
        return {"error": "Book not found"}, 404
