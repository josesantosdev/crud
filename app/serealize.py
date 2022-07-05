from marshmallow import fields
from flask_marshmallow import Marshmallow
from sqlalchemy import true

from app.model import Book
from flask import current_app

ma = Marshmallow()

def configure(app):
    ma.init_app(app)
    
    
class BookSchema(ma.SQLAlchemyAutoSchema):
   class Meta:
       model = Book
       load_instance = true
       
       id = fields.Integer()
       livro = fields.Str(required=True)
       escritor = fields.Str(required=True)
        