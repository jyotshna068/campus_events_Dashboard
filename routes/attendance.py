from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_required
from flask_login import current_user

from extensions import db

from models.event import Event
from models.attendance import Attendance
from models.registration import Registration

from utils.qr_utils import (
    generate_event_qr
)

attendance_bp = Blueprint(
    "attendance",
    __name__,
    url_prefix="/attendance"
)

#generate qr

@attendance_bp.route(
    "/generate/<int:event_id>"
)
@login_required
def generate_qr(event_id):

    event = Event.query.get_or_404(
        event_id
    )

    filename = generate_event_qr(
        event_id
    )

    event.qr_code = filename

    db.session.commit()

    flash(
        "QR Generated"
    )

    return redirect(
        url_for(
            "organizer.dashboard"
        )
    )

#qr check-in route

@attendance_bp.route(
    "/checkin/<int:event_id>"
)
@login_required
def checkin(event_id):

    registration = (
        Registration.query.filter_by(
            student_id=current_user.id,
            event_id=event_id
        ).first()
    )

    if not registration:

        flash(
            "Register first."
        )

        return redirect(
            url_for("events.home")
        )

    existing = (
        Attendance.query.filter_by(
            student_id=current_user.id,
            event_id=event_id
        ).first()
    )

    if existing:

        flash(
            "Attendance already marked."
        )

        return redirect(
            url_for(
                "student.dashboard"
            )
        )

    attendance = Attendance(
        student_id=current_user.id,
        event_id=event_id
    )

    db.session.add(
        attendance
    )

    db.session.commit()

    flash(
        "Attendance Marked"
    )

    return redirect(
        url_for(
            "student.dashboard"
        )
    )

#attendance report

@attendance_bp.route(
    "/report/<int:event_id>"
)
@login_required
def attendance_report(event_id):

    attendance = (
        Attendance.query.filter_by(
            event_id=event_id
        ).all()
    )

    return render_template(
        "organizer/attendance_report.html",
        attendance=attendance
    )