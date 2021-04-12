from config import db


class User(db.Model):
    """User table """
    __table_args__ = {'extend_existing': True}
    name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    grov_id = db.Column(db.Integer, nullable=False, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    company = db.Column(db.String(60), unique=True, nullable=False, )
