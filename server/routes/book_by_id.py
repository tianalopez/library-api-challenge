from . import Resource
from models.book import Book
from schemas.book_schema import BookSchema
from app_setup import db

book_schema = BookSchema(session=db.session)


class BookById(Resource):
    def get(self, ISBN):
        if book := db.session.query(Book).filter_by(ISBN == ISBN).first():
            book_schema = BookSchema()
            return book_schema.dump(book), 200
        return {"error": "Could not find book"}, 404

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

    def delete(self, ISBN):
        if book := db.session.query(Book).filter_by(ISBN == ISBN).first():
            try:
                db.session.delete(book)
                db.session.commit()
                return {"message": f"Book {id} has been deleted"}, 200
            except Exception as e:
                db.session.rollback()
                return {"error": str(e)}, 400
        return {"error": "Could not find book"}, 404
