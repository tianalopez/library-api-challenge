from app_setup import db


class User(db.Model):
    __tablename__ = "users"

    # Columns for users Table
    id = db.Column(db.Integer, primary_key=True)
    librarian = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # relationships
    books = db.relationship("Book", back_populates="users")

    # association

    # validations

    def __repr__(self):
        return f"<User #{self.id} {self.username} />"
