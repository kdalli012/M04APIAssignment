#everytime close terminal will need to reenter: export FLASK_APP=M04API & export FLASK_ENV=development
#in the filepath of this assignment then enter flask run

from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
app.app_context().push()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120))
    publisher = db.Column(db.String(120))

   

    def __repr__(self):
        return f"{self.title} - {self.author} - {self.publisher}"

@app.route('/')
def index():
    return 'Hello'

@app.route('/books')
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {'title': book.title, 'author': book.author, 'publisher': book.publisher}

        output.append(book_data)

    return {"books": output}
@app.route('/books/<id>')
def get_book(id):
    drink = Drink.query.get_or_404(id)
    return {"title": book.title, "author": book.author, "Publisher": book.publisher}