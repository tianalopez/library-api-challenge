from sqlalchemy.orm import validates
import re
from app_setup import db, timedelta
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.associationproxy import association_proxy

# , server_default=db.func.now() + timedelta(weeks=2)


class Book(db.Model):
    __tablename__ = "books"

    # Columns for users Table
    id = db.Column(db.Integer, primary_key=True)
    ISBN = db.Column(db.Integer, nullable=False)
    checked_out = db.Column(db.Boolean, default=False)
    due_date = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # relationships
    user = db.relationship("User", back_populates="books")

    # association

    # validations
    @validates("ISBN")
    def validate_ISBN(self, _, value):
        if not isinstance(value, int):
            raise TypeError("Input must be a string")
        elif len(value) is not 13:
            raise ValueError("ISBN Number must be 13 digits long")
        return value


    def __repr__(self):
        return f"<Book #{self.id} {self.ISBN} />"
