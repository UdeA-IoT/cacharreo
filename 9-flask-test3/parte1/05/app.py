from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to supress warning
db = SQLAlchemy(app)

#declaring the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True) #primary key column
    title = db.Column(db.String(80), index = True, unique = True) # book title
    author_name = db.Column(db.String(50), index = True, unique = False)
    author_surname = db.Column(db.String(80), index = True, unique = False) #author surname
    month = db.Column(db.String(20), index = True, unique = False) #the month of the book suggestion
    year = db.Column(db.Integer, index = True, unique = False) #the year of the book suggestion
    reviews = db.relationship('Review', backref='book', lazy='dynamic') #relationship of Books and Reviews
    
    #Get a nice printout for Book objects
    def __repr__(self):
        return "{} in: {},{}".format(self.title, self.month,self.year)

#Add your columns for the Reader model here below.
class Reader(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), index = True, unique = False)
    surname = db.Column(db.String(80), unique = False, index = True)
    email = db.Column(db.String(120), unique = True, index = True)
    #add your relationship column here
    reviews = db.relationship('Review', backref='reviewer', lazy='dynamic') 
  
    #get a nice printout for Reader objects
    def __repr__(self):
        return "Reader: {}".format(self.email)




#some routing for displaying the home page
@app.route('/')
@app.route('/home')
def home():
    return "Congrats! You are making your first one-to-many relationship in Flask-SQLAlchemy!"
