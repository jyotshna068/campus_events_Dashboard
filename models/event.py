from extensions import db
from datetime import datetime

class Event(db.Model):

    __tablename__ = "events"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(255)
    )

    description = db.Column(
        db.Text
    )

    venue = db.Column(
        db.String(255)
    )

    category = db.Column(
        db.String(100)
    )
    
    club_name = db.Column(
    db.String(150)
    )
    
    date = db.Column(
        db.DateTime
    )
    
    registration_deadline = db.Column(
        db.DateTime
    )

    image = db.Column(
        db.String(255)
    )

    organizer_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    qr_code = db.Column(
    db.String(255)
    )
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )