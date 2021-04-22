from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)



@app.route('/')
def show_form(): 

    return render_template('home.html')

@app.route('/story')
def show_story():

    text = story.generate(request.args)

    return render_template('story.html', story=text)
