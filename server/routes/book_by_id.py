from . import request, Resource
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

    #!Optional: Allows librarians to remove book by ISBN
    # def delete(self, ISBN):
    #     if book := db.session.query(Book).filter_by(ISBN == ISBN).first():
    #         try:
    #             db.session.delete(book)
    #             db.session.commit()
    #             return {"message": f"Book {id} has been deleted"}, 200
    #         except Exception as e:
    #             db.session.rollback()
    #             return {"error": str(e)}, 400
    #     return {"error": "Could not find book"}, 404
