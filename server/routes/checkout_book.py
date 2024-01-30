from . import request, Resource
from models.book import Book
from schemas.book_schema import BookSchema
from app_setup import db
from datetime import datetime, timedelta

book_schema = BookSchema(session=db.session)


class CheckoutBook(Resource):
    def patch(self,user_id, id):
        try:
            # find the book to checkout
            if not (
                wanted_book := db.session.query(Book)
                .filter_by(id=id, checked_out=False)
                .first()
            ):
                return {"message": f"Cannot find available book"}, 404

            # get all checked-out books by the user
            checked_out_books = (
                db.session.query(Book)
                .filter_by(user_id=user_id, checked_out=True)
                .all()
            )
            # check if the user has already checked out 3 books
            if len(checked_out_books) >= 3:
                return {"message": "You can only have 3 books checked out at once"}, 400

            # check if any of the user's checked-out books are overdue
            for book in checked_out_books:
                #use 13 days to avoid slight time differences
                if book.due_date and book.due_date <= datetime.utcnow() + timedelta(
                    days=13
                ):
                    return {
                        "message": f"This book with ISBN: {book.ISBN} is overdue. You must return it before checking out another book"
                    }, 400

            # manually update the wanted_book to mark it as checked out
            wanted_book.checked_out = True
            wanted_book.due_date = datetime.utcnow() + timedelta(weeks=2)
            wanted_book.user_id = user_id

            db.session.commit()
            return book_schema.dump(wanted_book), 200

        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500
