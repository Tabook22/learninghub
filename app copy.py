from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os
from flask import request

#Creating a Fallback key"
FALLBACK_SECRET_KEY = 'f20b407505e52722f6df01ede3b35890'
"""
The fallback secret key is a predefined key that your application will use if the SECRET_KEY environment variable is 
not set. It's a way to ensure your application has a secret key to use, even if the preferred, secure method of 
setting the key via an environment variable fails for some reason.
"""

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Tabook22@localhost/mydb'
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', FALLBACK_SECRET_KEY)
db = SQLAlchemy(app)

"""
Note: creating a secret key is crucial for a Flask application, especially when dealing with sessions, 
as it ensures the integrity and security of your application. The secret key is used to encrypt 
session data, which is stored client-side (in the user's browser). Without a secret key, 
attackers could tamper with the session data, potentially leading to security vulnerabilities.
"""


# User Model
class User(db.Model):
    __tablename__ = 'user'  # Specify the table name as 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    user_type = db.Column(db.String(50), nullable=False, default='user')

    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()  # Query the database for the user
        if user and check_password_hash(user.password_hash, password):  # Verify the password
            session['user_id'] = user.id  # Store user ID in session
            return redirect(url_for('index'))  # Redirect to the index page
        else:
            return "Invalid credentials, try again."  # Display error message
    return render_template('login.html')  # Render the login page for GET requests


@app.route('/adduser', methods=['GET', 'POST'])
def adduser():
    error_messages = {}
    form_data = {'name': '', 'email': '', 'username': '', 'password': '', 'confirm_password': ''}

    user_added = False  # Variable to indicate whether a user was added
    if request.method == 'POST':
        form_data = {
            'name': request.form['name'],
            'email': request.form['email'],
            'username': request.form['username'],
            'password': request.form['password'],
            'confirm_password': request.form['confirm_password']
        }

        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if not name:
            error_messages['name'] = "Name is required."
        if not email:
            error_messages['email'] = "Email is required."
        if not username:
            error_messages['username'] = "Username is required."
        if password != confirm_password:
            error_messages['password'] = "Passwords do not match."

        if not error_messages:
            password_hash = generate_password_hash(password)
            user = User(name=name, email=email, username=username, password_hash=password_hash)
            try:
                db.session.add(user)
                db.session.commit()
                user_added = True  # Move this line here
                #return "User added successfully!"
            except Exception as e:
                db.session.rollback()
                # Assume any exception is due to a duplicate username or email
                error_messages['database'] = "An error occurred. Username or email may already be taken."
        # Assume user is added successfully
        user_added = True
    return render_template('addusers.html', error_messages=error_messages,form_data=form_data, user_added=user_added)



@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    return render_template('index.html', user=user)

@app.route('/home')
def home():
    return render_template('home.html')


@app.route("/nsttopics")
def nsttopics():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    return render_template("nsttopics.html", user=user)



@app.route("/assignment")
def assignment():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    return render_template("assignment.html", user=user)



@app.route("/ussersac")
def usersac():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    return render_template("usersac.html", user=user)



@app.route("/surveysc")
def surveysc():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    return render_template("surveysc.html", user=user)



@app.route("/chatbotsc")
def chatbotsc():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    return render_template("chatbotsc.html", user=user)



@app.route('/aiedu')
def aiedu():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    return render_template("aiedu.html", user=user)



@app.route("/nisot")
def nisot():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    return render_template("nisot.html", user=user)



@app.route("/ainusc")
def ainusc():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    return render_template("ainusc.html", user=user)


@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove user_id from session
    return redirect(url_for('login'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)