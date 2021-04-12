""" from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# config sqlalchemy to the database
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://admin_user:admin_user@localhost:5000/assesment_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'

# instance of the database engine
db = SQLAlchemy(app) """
from config import app, db
from models.users import User

@app.route("/")
def hello():
    return "Hello, world!"

if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
