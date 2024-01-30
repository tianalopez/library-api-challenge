from . import request, Resource
from models.book import Book
from models.user import User
from schemas.book_schema import BookSchema
from app_setup import db
from datetime import datetime

book_schema = BookSchema(session=db.session)

class ReturnBook(Resource):
    #grab the book based on id
    def patch(self, id, user_id):
        if book := db.session.query(Book).filter_by(id=id, user_id=user_id,checked_out=True).first():
            try:
                #update the data
                book.checked_out = False
                book.user_id = None
                book.due_date = None
                #commit the changes
                db.session.commit()
                # Serialize the data and package your JSON response
                return book_schema.dump(book), 200
            except Exception as e:
                db.session.rollback()
                return {"error": str(e)}, 400
        return {"error": "Book not found"}, 404
