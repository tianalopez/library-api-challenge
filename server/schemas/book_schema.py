from marshmallow import fields, validate, validates, ValidationError
from models.book import Book
from app_setup import ma


class BookSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Book
        load_instance = True
        fields = [
            "id",
            "ISBN",
            "checked_out",
            "due_date",
            "user_id",
        ]

    # ISBN = fields.Integer(required=True, )
