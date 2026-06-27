from flask_login import UserMixin
from extensions import db

class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(
        db.String(150),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    role = db.Column(
        db.String(20),
        nullable=False
    )

    branch = db.Column(db.String(100))

    year = db.Column(db.String(20))
    
    approved = db.Column(
        db.Boolean,
        default=False
    )