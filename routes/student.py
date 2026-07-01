from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_required
from flask_login import current_user

from extensions import db
from models.event import Event
from models.registration import Registration
from models.notification import Notification

from utils.email_utils import (
    send_registration_email
)

student_bp = Blueprint(
    "student",
    __name__,
    url_prefix="/student"
)

#student dashboard

@student_bp.route("/dashboard")
@login_required
def dashboard():
    
    if current_user.role != "student":
        flash("Access Denied")
        return redirect(url_for("auth.login"))
    
    registrations = Registration.query.filter_by(
        student_id=current_user.id
    ).all()

    registered_events = []

    for registration in registrations:

        event = db.session.get(
            Event,
            registration.event_id
        )

        if event:
            registered_events.append(event)

    return render_template(
        "student/dashboard.html",
        events=registered_events
    )

#register for event

@student_bp.route(
    "/register/<int:event_id>"
)
@login_required
def register_event(event_id):

    if current_user.role != "student":
        flash("Access Denied")
        return redirect(url_for("auth.login"))
    
    existing_registration = (
        Registration.query.filter_by(
            student_id=current_user.id,
            event_id=event_id
        ).first()
    )

    if existing_registration:

        flash(
            "Already registered for this event."
        )

        return redirect(
            url_for(
                "events.event_details",
                event_id=event_id
            )
        )

    registration = Registration(
        student_id=current_user.id,
        event_id=event_id
    )

    db.session.add(registration)

    notification = Notification(
        user_id=current_user.id,
        message="Event registration successful."
    )

    db.session.add(notification)

    db.session.commit()
    
    send_registration_email(
    current_user.email,
    Event.query.get(event_id).title
)
   

    flash(
        "Successfully registered."
    )

    return redirect(
        url_for(
            "student.dashboard"
        )
    )

#notification page

@student_bp.route(
    "/notifications"
)
@login_required
def notifications():

    if current_user.role != "student":
        flash("Access Denied")
        return redirect(url_for("auth.login"))

    notifications = (
        Notification.query.filter_by(
            user_id=current_user.id
        )
        .order_by(
            Notification.created_at.desc()
        )
        .all()
    )

    return render_template(
        "student/notifications.html",
        notifications=notifications
    )

#profile page

@student_bp.route("/profile")
@login_required
def profile():
    if current_user.role != "student":
        flash("Access Denied")
        return redirect(url_for("auth.login"))
    
    return render_template(
        "student/profile.html",
        user=current_user
    )
