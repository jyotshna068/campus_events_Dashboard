from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_required
from flask_login import current_user

from extensions import db
from models.user import User
from models.event import Event
from models.registration import Registration

admin_bp = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin"
)
#admin acces helper
def admin_required():

    if current_user.role != "admin":
        return False

    return True

#admin dashboard

@admin_bp.route("/dashboard")
@login_required
def dashboard():

    if not admin_required():
        return redirect(url_for("events.home"))

    total_users = User.query.count()

    total_events = Event.query.count()

    total_registrations = (
        Registration.query.count()
    )

    pending_organizers = (
        User.query.filter_by(
            role="organizer",
            approved=False
        ).all()
    )

    return render_template(
        "admin/dashboard.html",
        total_users=total_users,
        total_events=total_events,
        total_registrations=total_registrations,
        pending_organizers=pending_organizers
    )

#approve organizer

@admin_bp.route(
    "/approve-organizer/<int:user_id>"
)
@login_required
def approve_organizer(user_id):

    if not admin_required():
        return redirect(url_for("events.home"))

    organizer = User.query.get_or_404(
        user_id
    )

    organizer.approved = True

    db.session.commit()

    flash(
        "Organizer Approved"
    )

    return redirect(
        url_for(
            "admin.dashboard"
        )
    )

#reject organizer

@admin_bp.route(
    "/reject-organizer/<int:user_id>"
)
@login_required
def reject_organizer(user_id):

    if not admin_required():
        return redirect(url_for("events.home"))

    organizer = User.query.get_or_404(
        user_id
    )

    db.session.delete(organizer)

    db.session.commit()

    flash(
        "Organizer Rejected"
    )

    return redirect(
        url_for(
            "admin.dashboard"
        )
    )

#manage users

@admin_bp.route("/users")
@login_required
def users():

    if not admin_required():
        return redirect(url_for("events.home"))

    users = User.query.all()

    return render_template(
        "admin/users.html",
        users=users
    )

#delete user

@admin_bp.route(
    "/delete-user/<int:user_id>"
)
@login_required
def delete_user(user_id):

    if not admin_required():
        return redirect(url_for("events.home"))

    user = User.query.get_or_404(
        user_id
    )

    db.session.delete(user)

    db.session.commit()

    flash("User Deleted")

    return redirect(
        url_for(
            "admin.users"
        )
    )

#manage events

@admin_bp.route("/events")
@login_required
def events():

    if not admin_required():
        return redirect(url_for("events.home"))

    events = Event.query.all()

    return render_template(
        "admin/events.html",
        events=events
    )

#delete event

@admin_bp.route(
    "/delete-event/<int:event_id>"
)
@login_required
def delete_event(event_id):

    if not admin_required():
        return redirect(url_for("events.home"))

    event = Event.query.get_or_404(
        event_id
    )

    db.session.delete(event)

    db.session.commit()

    flash(
        "Event Removed"
    )

    return redirect(
        url_for(
            "admin.events"
        )
    )

