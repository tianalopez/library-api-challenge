from sqlalchemy.orm import validates
import re
from app_setup import db, timedelta
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.associationproxy import association_proxy


class Book(db.Model):
    __tablename__ = "books"

    # Columns for users Table
    id = db.Column(db.Integer, primary_key=True)
    ISBN = db.Column(db.Integer)
    title = db.Column(db.String)
    checked_out = db.Column(db.Boolean, default=False)
    due_date = db.Column(db.DateTime, server_default=db.func.now() + timedelta(weeks=2))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # relationships
    user = db.relationship("User", back_populates="books")

    # association

    # validations

    def __repr__(self):
        return f"<User #{self.id} {self.username} />"
