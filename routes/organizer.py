import os

from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_required
from flask_login import current_user

from werkzeug.utils import secure_filename

from extensions import db
from models.event import Event
from models.registration import Registration

organizer_bp = Blueprint(
    "organizer",
    __name__,
    url_prefix="/organizer"
)

#organizer dashboard

@organizer_bp.route("/dashboard")
@login_required
def dashboard():

    events = Event.query.filter_by(
        organizer_id=current_user.id
    ).all()

    return render_template(
        "organizer/dashboard.html",
        events=events
    )

#create event

@organizer_bp.route(
    "/create-event",
    methods=["GET", "POST"]
)
@login_required
def create_event():

    if request.method == "POST":

        title = request.form["title"]

        description = request.form["description"]

        category = request.form["category"]

        club_name = request.form["club_name"]

        venue = request.form["venue"]

        date = request.form["date"]

        deadline = request.form[
            "registration_deadline"
        ]

        image_file = request.files["image"]

        filename = ""

        if image_file:

            filename = secure_filename(
                image_file.filename
            )

            image_file.save(
                os.path.join(
                    "static/uploads",
                    filename
                )
            )

        event = Event(
            title=title,
            description=description,
            category=category,
            club_name=club_name,
            venue=venue,
            date=date,
            registration_deadline=deadline,
            image=filename,
            organizer_id=current_user.id
        )

        db.session.add(event)
        db.session.commit()

        flash("Event Created")

        return redirect(
            url_for(
                "organizer.dashboard"
            )
        )

    return render_template(
        "organizer/create_event.html"
    )

#edit event

@organizer_bp.route(
    "/edit-event/<int:event_id>",
    methods=["GET", "POST"]
)
@login_required
def edit_event(event_id):

    event = Event.query.get_or_404(
        event_id
    )

    if request.method == "POST":

        event.title = request.form["title"]

        event.description = request.form[
            "description"
        ]

        event.category = request.form[
            "category"
        ]

        event.venue = request.form[
            "venue"
        ]

        db.session.commit()

        flash(
            "Event Updated"
        )

        return redirect(
            url_for(
                "organizer.dashboard"
            )
        )

    return render_template(
        "organizer/edit_event.html",
        event=event
    )

#delete event

@organizer_bp.route(
    "/delete-event/<int:event_id>"
)
@login_required
def delete_event(event_id):

    event = Event.query.get_or_404(
        event_id
    )

    db.session.delete(event)

    db.session.commit()

    flash(
        "Event Deleted"
    )

    return redirect(
        url_for(
            "organizer.dashboard"
        )
    )

#view registrations

@organizer_bp.route(
    "/registrations/<int:event_id>"
)
@login_required
def registrations(event_id):

    registrations = (
        Registration.query.filter_by(
            event_id=event_id
        ).all()
    )

    return render_template(
        "organizer/registrations.html",
        registrations=registrations
    )