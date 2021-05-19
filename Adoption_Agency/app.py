from flask import Flask, render_template, request, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPet

app = Flask(__name__)

import logging
handler = logging.FileHandler("test.log")  # Create the file logger
app.logger.addHandler(handler)             # Add it to the built-in logger
app.logger.setLevel(logging.DEBUG)         # Set the log level to debug
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.config["SECRET_KEY"] = "abc123"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def show_home_page():
    """Render homepage and show available pets"""
    pets = Pet.query.all()
    
    return render_template('home.html', pets = pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """
    Create form for adding pet, pass to add_pet template. 
    Post route check for CSRF token then commit new pet to db.
    """
    form = AddPet()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data
        pet = Pet(name=name, species=species, photo_url=photo_url, notes=notes, available=available)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else: 
        return render_template('add_pet.html', form=form)

@app.route('/<int:id>', methods=["GET", "POST"])
def show_pet_details(id):
    """
    Render page showing details for selected pet.
    Create form for editing pet details.
    Post route check for CSRF token then commit edited information to db.
    """
    pet = Pet.query.get_or_404(id)
    form = AddPet(obj=pet)
    if form.validate_on_submit(): 
        pet.name = form.name.data
        pet.species = form.species.data
        pet.notes = form.notes.data
        pet.photo_url = form.photo_url.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/')
    else: 
        return render_template('pet_details.html', pet=pet, form=form)
