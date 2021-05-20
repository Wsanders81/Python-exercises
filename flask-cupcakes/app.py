
from flask import Flask, request, jsonify, render_template, redirect

from forms import AddCupcakeForm
from models import db, connect_db, Cupcake

app = Flask(__name__)

import logging
handler = logging.FileHandler("test.log")  # Create the file logger
app.logger.addHandler(handler)             # Add it to the built-in logger
app.logger.setLevel(logging.DEBUG)         # Set the log level to debug

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)

@app.route('/')
def show_all_cupcakes():
    cupcakes = Cupcake.query.all()
    form = AddCupcakeForm()
    return render_template('index.html', cupcakes=cupcakes, form=form)

@app.route('/api/cupcakes')
def list_all_cupcakes():
    """ Retrieve all cupcakes and return JSON """
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes = all_cupcakes)

@app.route('/api/cupcakes/<int:id>')
def get_single_cupcake(id): 
    """ Retrieve cupcake using id, return JSON """
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake = cupcake.serialize())

@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake(): 
    """ Take given post request info and create a new cupcake"""
    new_cupcake = Cupcake(
                flavor = request.json['flavor'], 
                rating = request.json['rating'], 
                image = request.json.get('image'), 
                size = request.json['size']
    )
    db.session.add(new_cupcake)
    db.session.commit()
    res_json = jsonify(cupcake = new_cupcake.serialize())
    return (res_json, 201)

@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_cupcake(id):
    """ Edit cupcake using given ID, commit changes to database """
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    cupcake.size = request.json.get('size', cupcake. size)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    """ Delete cupcake using given ID, return message stating cupcake has been deleted """
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Selected cupcake has been deleted")
    
