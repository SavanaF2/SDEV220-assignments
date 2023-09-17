from flask import Flask
from flask import request

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     book_name = db.Column(db.String(80), unique=True, nullable=False)
     author = db.Column(db.String(80), nullable=False)
     publisher = db.Column(db.String(120))

     def __repr__(self):
         return f"{self.id} - {self.book_name} - {self.author} - {self.publisher}"

@app.route('/', methods=['GET'])
def home():
    return "Hello world"

@app.route('/books')
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {'id': book.id, 'book_name': book.book_name, 'Author': book.author, 'publisher':book.publisher}
   
        output.append(book_data)
    return {"books": output}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {'id': book.id, 'book_name': book.book_name, 'Author': book.author, 'publisher':book.publisher}

@app.route('/books', methods=['POST'])
def add_book():
    book = Book(id=request.json['id'], book_name=request.json['book_name'], Author=request.json['Author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

@app.route('/books/<id>', methods=['DELETE'])
def delete_book():
    book = Book.query.get(id)
    if book is None:
        return{"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "Successfully deleted"}