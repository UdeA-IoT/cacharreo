from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#database configuration
app = Flask(__name__) #application instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db' #path to database and its name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to supress warning
db = SQLAlchemy(app) #database instance


#some routing for displaying the home page
@app.route('/')
@app.route('/home')
def home():
    return "Congrats! You have just created your first Flask application supporting databases!"
