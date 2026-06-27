from flask import Blueprint
from flask import render_template
from flask import request

from datetime import datetime

from extensions import db
from models.event import Event
from models.comment import Comment
from models.reply import Reply

from sqlalchemy import and_

from flask import redirect
from flask import Response

from utils.calendar_utils import (
    google_calendar_link
)

events_bp = Blueprint(
    "events",
    __name__
)

#homepage

@events_bp.route("/")
def home():

    upcoming_events = Event.query.filter(
        Event.date >= datetime.now()
    ).order_by(
        Event.date.asc()
    ).all()

    return render_template(
        "home.html",
        events=upcoming_events
    )

#events page

@events_bp.route("/events")
def events():

    search = request.args.get(
        "search",
        ""
    )

    category = request.args.get(
        "category",
        ""
    )

    club = request.args.get(
        "club",
        ""
    )

    query = Event.query

    if search:

        query = query.filter(
            Event.title.contains(search)
        )

    if category:

        query = query.filter(
            Event.category == category
        )

    if club:

        query = query.filter(
            Event.club_name == club
        )

    else:

        events = query.order_by(
            Event.date.asc()
        ).all()

    return render_template(
        "events.html",
        events=events
    )

#event details

@events_bp.route(
    "/event/<int:event_id>"
)
def event_details(event_id):

    event = Event.query.get_or_404(
        event_id
    )

    comments = Comment.query.filter_by(
        event_id=event_id
    ).all()

    replies = Reply.query.all()

    return render_template(
        "event_details.html",
        event=event,
        comments=comments,
        replies=replies
    )

#past events page

@events_bp.route(
    "/past-events"
)
def past_events():

    events = Event.query.filter(
        Event.date < datetime.now()
    ).order_by(
        Event.date.desc()
    ).all()

    return render_template(
        "past_events.html",
        events=events
    )

#google calender

@events_bp.route(
    "/calendar/<int:event_id>"
)
def add_to_calendar(event_id):

    event = Event.query.get_or_404(
        event_id
    )

    calendar_url = (
        google_calendar_link(
            event
        )
    )

    return redirect(
        calendar_url
    )

#download ics

@events_bp.route(
    "/download-ical/<int:event_id>"
)
def download_ical(event_id):

    event = Event.query.get_or_404(
        event_id
    )

    ics_content = f"""
BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
SUMMARY:{event.title}
DESCRIPTION:{event.description}
LOCATION:{event.venue}
DTSTART:{event.date.strftime('%Y%m%dT%H%M%S')}
END:VEVENT
END:VCALENDAR
"""

    return Response(
        ics_content,
        mimetype="text/calendar",
        headers={
            "Content-Disposition":
            f"attachment; filename=event_{event.id}.ics"
        }
    )