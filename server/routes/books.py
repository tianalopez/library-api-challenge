from . import request, Resource
from models.book import Book
from schemas.book_schema import BookSchema
from app_setup import db

book_schema = BookSchema(session=db.session)
books_schema = BookSchema(many=True, session=db.session)


class Books(Resource):
    def get(self):
        books = books_schema.dump(Book.query)
        return books, 200

    def post(self):
        #receive the ISBN from the frontend
        try:
            data = request.json
            # validate data
            book_schema.validate(data)
            # deserialize with load()
            new_book = book_schema.load(data)
            # add new book to book table
            db.session.add(new_book)
            db.session.commit()
            # serialize with dump()
            serialized_book = book_schema.dump(new_book)
            return serialized_book, 201
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 400
