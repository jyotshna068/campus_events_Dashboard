from extensions import db
from datetime import datetime


class Certificate(db.Model):

    __tablename__ = "certificates"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    event_id = db.Column(
        db.Integer,
        db.ForeignKey("events.id"),
        nullable=False
    )

    certificate_id = db.Column(
        db.String(100),
        unique=True
    )

    generated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    pdf_path = db.Column(
        db.String(255)
    )