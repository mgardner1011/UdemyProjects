from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
db.init_app(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Books).all()
    return render_template('index.html', all_books=all_books)


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        new_book = Books(title=request.form.get('title'),
                         author=request.form.get('author'),
                         rating=float(request.form.get('rating')))
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/edit', methods=['POST', 'GET'])
def edit_ratings():
    if request.method == 'POST':
        id = request.form.get('id')
        book = Books.query.get(id)
        book.rating = request.form.get('new-rating')
        db.session.commit()
        return redirect(url_for('home'))
    id = request.args.get('id')
    book = Books.query.get(id)
    return render_template('edit.html', book=book)

@app.route('/delete')
def delete():
    id = request.args.get('id')
    book_to_delete = Books.query.get(id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

