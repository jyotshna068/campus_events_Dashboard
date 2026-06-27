from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_required
from flask_login import current_user

from extensions import db
from models.comment import Comment
from models.reply import Reply

comments_bp = Blueprint(
    "comments",
    __name__,
    url_prefix="/comments"
)

#add comment

@comments_bp.route(
    "/add/<int:event_id>",
    methods=["POST"]
)
@login_required
def add_comment(event_id):

    comment_text = request.form["comment"]

    comment = Comment(
        user_id=current_user.id,
        event_id=event_id,
        comment=comment_text
    )

    db.session.add(comment)
    db.session.commit()

    flash(
        "Comment Added"
    )

    return redirect(
        url_for(
            "events.event_details",
            event_id=event_id
        )
    )

#edit comment

@comments_bp.route(
    "/edit/<int:comment_id>",
    methods=["GET", "POST"]
)
@login_required
def edit_comment(comment_id):

    comment = Comment.query.get_or_404(
        comment_id
    )

    if comment.user_id != current_user.id:

        flash(
            "Unauthorized"
        )

        return redirect(
            url_for("events.home")
        )

    if request.method == "POST":

        comment.comment = request.form[
            "comment"
        ]

        db.session.commit()

        flash(
            "Comment Updated"
        )

        return redirect(
            url_for("events.home")
        )

    return render_template(
        "edit_comment.html",
        comment=comment
    ) 

#delete comment

@comments_bp.route(
    "/delete/<int:comment_id>"
)
@login_required
def delete_comment(comment_id):

    comment = Comment.query.get_or_404(
        comment_id
    )

    if comment.user_id != current_user.id:

        flash(
            "Unauthorized"
        )

        return redirect(
            url_for("events.home")
        )

    db.session.delete(comment)

    db.session.commit()

    flash(
        "Comment Deleted"
    )

    return redirect(
        url_for("events.home")
    )

#add reply

@comments_bp.route(
    "/reply/<int:comment_id>",
    methods=["POST"]
)
@login_required
def add_reply(comment_id):

    reply_text = request.form["reply"]

    reply = Reply(
        comment_id=comment_id,
        user_id=current_user.id,
        reply=reply_text
    )

    db.session.add(reply)

    db.session.commit()

    flash(
        "Reply Added"
    )

    return redirect(
        request.referrer
    )

#like comment

@comments_bp.route(
    "/like/<int:comment_id>"
)
@login_required
def like_comment(comment_id):

    comment = Comment.query.get_or_404(
        comment_id
    )

    comment.likes += 1

    db.session.commit()

    return redirect(
        request.referrer
    )

#dislike comment

@comments_bp.route(
    "/dislike/<int:comment_id>"
)
@login_required
def dislike_comment(comment_id):

    comment = Comment.query.get_or_404(
        comment_id
    )

    comment.dislikes += 1

    db.session.commit()

    return redirect(
        request.referrer
    )