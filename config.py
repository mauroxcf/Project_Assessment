from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# config sqlalchemy to the database
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqldb://root:root@localhost:5000/assesment_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'

# instance of the database engine
db = SQLAlchemy(app)
