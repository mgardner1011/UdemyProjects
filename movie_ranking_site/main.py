from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie-collection.db"
db.init_app(app)

movie_url = 'https://api.themoviedb.org/3/search/movie'
api_key = 'your_api_key'
parameters = {
    'api_key': api_key,
    'language': 'en-US'
}

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(500), nullable=True)
    img_url = db.Column(db.String(1500), nullable=False)


class MovieForm(FlaskForm):
    rating = FloatField('Your rating out of 10', validators=[DataRequired()])
    review = StringField('Your review', validators=[DataRequired()])


class AddForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Submit')

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    all_movies = db.session.query(Movies).order_by(Movies.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
        db.session.commit()
    return render_template("index.html", all_movies=all_movies)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    id = request.args.get('id')
    movie = Movies.query.get(id)
    form = MovieForm(movie_id=id)
    if request.method == 'POST':
        id = request.form.get('id')
        movie = Movies.query.get(id)
        movie.rating = request.form.get('rating')
        movie.review = request.form.get('review')
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', movie=movie, form=form)

@app.route('/delete')
def delete():
    id = request.args.get('id')
    movie_to_delete = Movies.query.get(id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/add', methods=['POST', 'GET'])
def add():
    form = AddForm()
    if request.method == 'POST':
        parameters['query'] = form.title.data
        response = requests.get(url=movie_url, params=parameters).json()
        data = []
        for movie in response['results']:
            movie_data = {
                'title': movie['title'],
                'id': movie['id'],
                'year': movie['release_date'].split('-')[0]
            }
            data.append(movie_data)
        return render_template('select.html', movies=data)
    return render_template('add.html', form=form)

@app.route('/add_movie')
def add_movie():
    url = 'https://api.themoviedb.org/3/movie/' + request.args.get('id')
    params = {
        'api_key': api_key,
        'language': 'en-US',
    }
    response = requests.get(url=url, params=params).json()
    new_movie = Movies(title=response['title'],
                       year=int(response['release_date'].split('-')[0]),
                       description=response['overview'],
                       rating=response['vote_average'],
                       img_url='https://image.tmdb.org/t/p/w500' + response['poster_path'])
    db.session.add(new_movie)
    db.session.commit()
    movie = Movies.query.filter_by(title=response['title']).first()
    movie_id = movie.id
    return redirect(url_for('edit', id=movie_id))



if __name__ == '__main__':
    app.run(debug=True)
