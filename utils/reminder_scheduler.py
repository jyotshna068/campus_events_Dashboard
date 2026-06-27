from datetime import datetime
from datetime import timedelta

from models.registration import Registration
from models.event import Event
from models.user import User

from utils.email_utils import (
    send_reminder_email
)

def check_reminders():

    tomorrow = (
        datetime.now() +
        timedelta(hours=24)
    )

    events = Event.query.all()

    for event in events:

        if (
            event.date.date()
            ==
            tomorrow.date()
        ):

            registrations = (
                Registration.query.filter_by(
                    event_id=event.id
                ).all()
            )

            for registration in registrations:

                student = User.query.get(
                    registration.student_id
                )

                send_reminder_email(
                    student.email,
                    event.title,
                    event.date
                )