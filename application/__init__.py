from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expensesDB.db'
app.config['SECRET_KEY'] = 'LLJ0D08SA9LJ9KH1RKA8NQDM33G'

db = SQLAlchemy(app)

from application import routes

# Create tables using flask_sqlalchemy
with app.app_context():
    db.create_all()
