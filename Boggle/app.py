from flask import Flask, request, render_template,  redirect, flash,  jsonify, session
from flask_debugtoolbar import DebugToolbarExtension

from boggle import Boggle


app = Flask(__name__)
app.debug=True
app.config['SECRET_KEY']="abc123"
toolbar = DebugToolbarExtension(app)


#? This would not worked when placed inside of my home
#? route???
boggle_game = Boggle()
board = boggle_game.make_board()

@app.route('/')
def show_board(): 
    """
    Place board into session memory, create board, set
    session cookies for highscore and playtimes if 
    none exist. Render base template
    """
    session["board"] = board
    
    # highscore = session.get('highscore', 0)
    # playtimes = session.get('playtimes', 0)
    
    return render_template('base.html', game_board = board)


@app.route('/check-for-answer')
def check_word(): 
    """
    import submitted word, check if word is valid, 
    return string identifying whether or not 
    word is valid
    """
    word = request.args['word']
    session_board = session["board"]
    isValid = boggle_game.check_valid_word(session_board, word)
    return jsonify({"result":isValid})

@app.route('/post-score', methods=["POST"])
def score(): 
    """
    import score, check for highscore and times played
    return True or False
    """
    score = request.json['score']
    intscore = int(score)
    playtimes = session.get('playtimes',0)
    highscore = session.get('highscore', 0)
    session['playtimes'] = playtimes + 1

    if intscore > highscore: 
        session['highscore'] = score
        
    return jsonify(brokeRecord = score > highscore)
    

