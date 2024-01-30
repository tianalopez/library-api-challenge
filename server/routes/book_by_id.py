from . import request, Resource
from models.book import Book
from schemas.book_schema import BookSchema
from app_setup import db
from decorators import require_librarian

book_schema = BookSchema(session=db.session)


class BookById(Resource):
    def get(self, id):
        if book := db.session.get(Book, id):
            book_schema = BookSchema()
            return book_schema.dump(book), 200
        return {"error": "Could not find book"}, 404

    @require_librarian
    def delete(self, id):
        if book := db.session.get(Book, id):
            try:
                db.session.delete(book)
                db.session.commit()
                return {"message": f"Book {id} has been deleted"}, 200
            except Exception as e:
                db.session.rollback()
                return {"error": str(e)}, 400
        return {"error": "Could not find Book"}, 404
