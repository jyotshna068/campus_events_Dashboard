from extensions import db


class Club(db.Model):

    __tablename__ = "clubs"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(150),
        nullable=False
    )

    description = db.Column(
        db.Text
    )

    approved = db.Column(
        db.Boolean,
        default=False
    )

    organizer_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )