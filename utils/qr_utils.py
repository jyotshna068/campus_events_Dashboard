import qrcode
import os


def generate_event_qr(
    event_id
):

    qr_data = (
        f"http://localhost:5000/"
        f"attendance/checkin/{event_id}"
    )

    qr = qrcode.make(
        qr_data
    )

    filename = (
        f"event_{event_id}.png"
    )

    filepath = os.path.join(
        "static/qr",
        filename
    )

    qr.save(filepath)

    return filename