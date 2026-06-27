import os
import uuid

from reportlab.platypus import (
    SimpleDocTemplate,
    Spacer,
    Paragraph
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_certificate(
    student_name,
    event_title,
    certificate_id
):

    filename = (
        f"{certificate_id}.pdf"
    )

    filepath = os.path.join(
        "static/certificates",
        filename
    )

    doc = SimpleDocTemplate(
        filepath
    )

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "Certificate of Participation",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            f"This certifies that "
            f"<b>{student_name}</b>",
            styles["Heading2"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            f"has successfully participated in "
            f"<b>{event_title}</b>",
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            f"Certificate ID: "
            f"{certificate_id}",
            styles["Normal"]
        )
    )

    doc.build(elements)

    return filename