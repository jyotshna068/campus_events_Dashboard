import uuid

from flask import Blueprint
from flask import redirect
from flask import url_for
from flask import flash
from flask import render_template

from flask_login import (
    login_required,
    current_user
)

from extensions import db

from models.event import Event
from models.user import User
from models.attendance import Attendance
from models.certificate import Certificate

from utils.certificate_utils import (
    generate_certificate
)

certificates_bp = Blueprint(
    "certificates",
    __name__,
    url_prefix="/certificates"
)

#generate certificate

@certificates_bp.route(
    "/generate/<int:event_id>"
)
@login_required
def generate(event_id):

    attendance = (
        Attendance.query.filter_by(
            student_id=current_user.id,
            event_id=event_id
        ).first()
    )

    if not attendance:

        flash(
            "Attendance not found."
        )

        return redirect(
            url_for(
                "student.dashboard"
            )
        )

    existing = (
        Certificate.query.filter_by(
            student_id=current_user.id,
            event_id=event_id
        ).first()
    )

    if existing:

        flash(
            "Certificate already exists."
        )

        return redirect(
            url_for(
                "certificates.my_certificates"
            )
        )

    event = Event.query.get(
        event_id
    )

    certificate_id = (
        str(uuid.uuid4())[:8]
    )

    filename = generate_certificate(
        current_user.name,
        event.title,
        certificate_id
    )

    certificate = Certificate(

        student_id=current_user.id,

        event_id=event_id,

        certificate_id=certificate_id,

        pdf_path=filename

    )

    db.session.add(
        certificate
    )

    db.session.commit()

    flash(
        "Certificate Generated"
    )

    return redirect(
        url_for(
            "certificates.my_certificates"
        )
    )

#my certificates

@certificates_bp.route(
    "/my-certificates"
)
@login_required
def my_certificates():

    certificates = (
        Certificate.query.filter_by(
            student_id=current_user.id
        ).all()
    )

    return render_template(
        "student/certificates.html",
        certificates=certificates
    )

#verify certificate

@certificates_bp.route(
    "/verify/<certificate_id>"
)
def verify(certificate_id):

    certificate = (
        Certificate.query.filter_by(
            certificate_id=certificate_id
        ).first()
    )

    return render_template(
        "verify_certificate.html",
        certificate=certificate
    )