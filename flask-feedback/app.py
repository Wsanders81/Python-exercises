from flask import Flask, request, jsonify, session,  render_template, redirect, flash
from models import db, connect_db, User, Feedback
from forms import RegistrationForm, LoginForm, FeedbackForm
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

import logging
handler = logging.FileHandler("test.log")  # Create the file logger
app.logger.addHandler(handler)             # Add it to the built-in logger
app.logger.setLevel(logging.DEBUG)         # Set the log level to debug

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///user_feedback'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"
app.config["SQLALCHEMY_ECHO"] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

toolbar = DebugToolbarExtension(app)

@app.route('/')
def redirect_to_register():
    return redirect('/home')

@app.route('/home')
def show_home_page(): 
    return render_template('home.html')

@app.route('/register', methods=["GET", "POST"])
def register_user():
    
    """ Show registration form. Post: Process registration
    and redirect user to /secret ."""
    
    form = RegistrationForm()
    
    if form.validate_on_submit(): 
        #TODO: add error handling for non-unique username
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        new_user = User.register(username, password, email, first_name, last_name)
        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.username
        flash("Welcome! Successfully created your account!", "alert-success")
        return redirect(f'/users/{username}')
    else: 
        return render_template('registration-form.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def show_login_form():
    
    """ Show login form, if user validated, redirect to user info page """
    
    form = LoginForm()
    if form.validate_on_submit(): 
        username = form.username.data
        password = form.password.data
        user = User.authenticate(username, password)
        if(User.authenticate(username, password)== False): 
            flash('Sorry, invalid login/password', 'alert-danger')
            
            return redirect('/login')
        
        else: 
            session['user_id'] = user.username
            flash(f"Welcome back, {user.username}!", 'alert-primary')
            return redirect(f'/users/{username}')
    else: 
        return render_template('login-form.html', form= form)

@app.route('/users/<username>')
def show_user_page(username):
    
    """Show user information. Show all user feedback with link
    to edit/delete feedback. Show 'add feedback' button and
    'delete user' button """
    
    if"user_id" not in session: 
        flash('Please login first!', 'alert-danger')
        return redirect('/home')
    user = User.query.get_or_404(username)
    feedback = Feedback.query.all()
    return render_template('user-page.html', user=user, feedback=feedback)

@app.route('/users/<username>/delete', methods=["POST"]) 
def delete_user(username):
     
    """ delete user from data base and delete all feedback """
    
    if"user_id" not in session: 
        flash('Please login first!', 'alert-danger')
        return redirect('/home')
    if username == session['user_id']: 
        user = User.query.get_or_404(username)
        db.session.delete(user)
        db.session.commit()
        flash('Your account has been successfully deleted', 'alert-danger')
        session.pop("user_id")
        return redirect('/home')
    else: 
        flash('You do not have access to delete account', 'alert-danger')
        return redirect('/home')

@app.route('/users/<username>/feedback/add', methods=["GET","POST"])
def add_feedback(username): 
    
    """ display form for feedback """
    
    if"user_id" not in session: 
        flash('Please login first!', 'alert-danger')
        return redirect('/home')
    form = FeedbackForm()
    if form.validate_on_submit(): 
        title = form.title.data
        content = form.content.data
        username = session["user_id"]
        new_feedback = Feedback(title=title, content=content, username=username)
        db.session.add(new_feedback)
        db.session.commit()
        flash('Feedback succesfully submitted', 'alert-success')
        return redirect(f'/users/{username}')
    else: 
        return render_template('feedback-form.html', form=form)

@app.route('/users/<int:feedbackID>/update', methods=["GET", "POST"])
def update_user_feedback(feedbackID):
    
    """ Show user feedback edit form. On submission, edit requested
    user feedback """
    
    if"user_id" not in session: 
        flash('Please login first!', 'alert-danger')
        return redirect('/home')
    feedback = Feedback.query.get_or_404(feedbackID)
    form = FeedbackForm(obj=feedback)
    username = feedback.user.username
    if form.validate_on_submit(): 
        feedback.title = form.title.data
        feedback.content = form.content.data
        db.session.commit()
        flash('Your feedback has been successfully updated', 'alert-success')
        return redirect(f'/users/{username}')
    return render_template('feedback-form.html', form=form)

@app.route('/feedback/<feedbackID>/delete', methods=["POST", "GET"])
def delete_feedback(feedbackID): 
    
    """ Delete selected user feedback , redirect user back to user page """

    if"user_id" not in session: 
        flash('Please login first!', 'alert-danger')
        return redirect('/home') 
     
    feedback = Feedback.query.get_or_404(feedbackID)
    username = session["user_id"]
    if feedback.username == session["user_id"]: 
        db.session.delete(feedback)
        db.session.commit()
        flash('Feedback successfully deleted', 'alert-success')
        return redirect(f'/users/{username}')
    else: 
        flash('Permission Denied', 'alert-danger')
        return redirect (f'/users/{username}')
 
@app.route('/logout', methods=["POST"])
def logout_user():
    
    """ Logout current user, redirect to home """
    
    session.pop('user_id')
    flash('You have been logged out', 'alert-danger')
    return redirect('/')

