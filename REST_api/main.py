import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):

        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route('/random')
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe=random_cafe.to_dict())

@app.route('/all')
def get_all_cafes():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])

@app.route('/search')
def search_cafes():
    location = request.args.get('loc')
    cafe_at_loc = Cafe.query.filter(Cafe.location==location).first()
    if cafe_at_loc:
        return jsonify(cafe=cafe_at_loc.to_dict())
    else:
        return jsonify(error={"Not found": "Sorry, we don't have a cafe at that location"})


## HTTP POST - Create Record

@app.route('/add', methods=['POST'])
def add_cafe():
    new_cafe = Cafe(name=request.form.get('name'),
                    map_url=request.form.get('map_url'),
                    img_url=request.form.get('img_url'),
                    location=request.form.get('location'),
                    seats=request.form.get('seats'),
                    has_toilet=int(request.form.get('has_toilet')),
                    has_wifi=int(request.form.get('has_wifi')),
                    has_sockets=int(request.form.get('has_sockets')),
                    can_take_calls=int(request.form.get('can_take_calls')),
                    coffee_price=request.form.get('coffee_price'))
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"Success": "Successfully added the new cafe."})

## HTTP PUT/PATCH - Update Record

@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    cafe_to_update = Cafe.query.get(cafe_id)
    if cafe_to_update:
        cafe_to_update.coffee_price = request.form.get('coffee_price')
        db.session.commit()
        return jsonify(response={"Success": "You have successfully updated the price."})
    else:
        return jsonify(error={"Not Found": " Sorry a cafe with that id was not found"}), 404
## HTTP DELETE - Delete Record

@app.route('/delete/<int:cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    cafe_to_delete = Cafe.query.get(cafe_id)
    if cafe_to_delete:
        if request.args.get('api-key') == 'TopSecretAPIKey':
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={'Success': 'You have successfully deleted the Cafe.'})
        else:
            return jsonify({"error": "Your are not allowed to delete this record."}), 403
    else:
        return jsonify(error={"Not Found": "A cafe with that id was not found."}), 404


if __name__ == '__main__':
    app.run(debug=True)
