from extensions import db


class Media(db.Model):

    __tablename__ = "media"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    event_id = db.Column(
        db.Integer,
        db.ForeignKey("events.id")
    )

    file_path = db.Column(
        db.String(255)
    )

    uploaded_at = db.Column(
        db.DateTime
    )