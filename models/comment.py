from extensions import db
from datetime import datetime


class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    event_id = db.Column(
        db.Integer,
        db.ForeignKey("events.id")
    )

    comment = db.Column(
        db.Text,
        nullable=False
    )

    likes = db.Column(
        db.Integer,
        default=0
    )

    dislikes = db.Column(
        db.Integer,
        default=0
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )