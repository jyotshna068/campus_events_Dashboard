from urllib.parse import quote


def google_calendar_link(event):

    title = quote(event.title)

    details = quote(
        event.description
    )

    location = quote(
        event.venue
    )

    start = event.date.strftime(
        "%Y%m%dT%H%M%SZ"
    )

    end = event.date.strftime(
        "%Y%m%dT%H%M%SZ"
    )

    url = (
        f"https://calendar.google.com/calendar/render?"
        f"action=TEMPLATE"
        f"&text={title}"
        f"&details={details}"
        f"&location={location}"
        f"&dates={start}/{end}"
    )

    return url