from flask import Flask, request, render_template,  redirect, flash,  jsonify, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY']= 'abc123'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

responses = list()

# @app.route('/')
# def show_home(): 
#    return render_template('base.html', title=satisfaction_survey.title)

@app.route('/')
def show_landing_page():
    return render_template('landing-page.html', title=satisfaction_survey.title, instructions=satisfaction_survey.instructions)

@app.route('/start_survey', methods=["POST"])

def redirect_to_questions(): 

    session["responses"] = []

    return redirect ('/questions/0')

@app.route('/questions/<int:number>')
def redirect_to_question(number): 
    responses = session['responses']
    if number > len(responses): 
        flash('Cannot skip questions, so sorry.', 'error')
        return redirect('/')
    else: 
        print(session)
        return render_template('question.html',question = satisfaction_survey.questions[number].question, choices = satisfaction_survey.questions[number].choices)

@app.route('/answer', methods=["POST"])
def add_answer(): 
    
    user_answer = request.form['choice']

    responses = session["responses"]
    responses.append(user_answer)
    session["responses"] = responses

    if len(responses) == len(satisfaction_survey.questions):
        return redirect('/finished')
    else: 
        return redirect(f"/questions/{len(responses)}")

@app.route('/finished')
def show_finish():
    return render_template('finished.html')