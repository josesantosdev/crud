from flask import Blueprint, current_app, jsonify, request
from .model import Book
from .serealize import BookSchema

bp_books = Blueprint('books', __name__)
bs = BookSchema()


@bp_books.route('/mostrar', methods=['GET'])
def show():
    bs = BookSchema(many=True)
    books = Book.query.all()
    return bs.jsonify(books), 200
    
@bp_books.route('/mostrar/<id>', methods=['GET'])
def show_by_id(id):
    book = Book.query.filter_by(id=id).first_or_404()
    book_by_id = bs.dump(book)
    return jsonify(book_by_id), 200

    
@bp_books.route('/cadastrar', methods=['POST'])
def create():
    data = request.get_json()
    book = bs.load(data)
    current_app.db.session.add(book)
    current_app.db.session.commit()
    return bs.jsonify(book), 201
    
    
@bp_books.route('/editar/<id>', methods=['PUT'])
def edit(id):
   query = Book.query.filter(Book.id == id)
   query.update(request.json)
   current_app.db.session.commit()
   return bs.jsonify(query.first()), 200
    
@bp_books.route('/deletar/<id>', methods=['DELETE'])
def delete(id):
    Book.query.filter(Book.id == id).delete()
    current_app.db.session.commit()
    return jsonify('Deletado'), 200
    
    
    