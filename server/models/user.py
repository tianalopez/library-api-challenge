from app_setup import db
from sqlalchemy.ext.associationproxy import association_proxy


class User(db.Model):
    __tablename__ = "users"

    # Columns for users Table
    id = db.Column(db.Integer, primary_key=True)
    librarian = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # relationships

    # association

    # validations

    def __repr__(self):
        return f"<User #{self.id} {self.username} />"
