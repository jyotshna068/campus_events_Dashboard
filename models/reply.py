from extensions import db
from datetime import datetime


class Reply(db.Model):

    __tablename__ = "replies"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    comment_id = db.Column(
        db.Integer,
        db.ForeignKey("comments.id")
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    reply = db.Column(
        db.Text,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )