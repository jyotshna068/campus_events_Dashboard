from flask_mail import Message
from extensions import mail


def send_registration_email(
    user_email,
    event_title
):

    msg = Message(
        subject="Event Registration Successful",
        recipients=[user_email]
    )

    msg.body = f"""
Hello,

You have successfully registered for:

{event_title}

Thank you.

Campus Events Dashboard
"""

    mail.send(msg)
    
#event remainder mail

def send_reminder_email(
    user_email,
    event_title,
    event_date
):

    msg = Message(
        subject="Event Reminder",
        recipients=[user_email]
    )

    msg.body = f"""
Reminder

Your event is coming up.

Event:
{event_title}

Date:
{event_date}

See you there.

Campus Events Dashboard
"""

    mail.send(msg)