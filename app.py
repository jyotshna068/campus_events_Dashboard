from flask import Flask

from config import Config
from extensions import db, login_manager, mail
from models.user import User
    
def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    mail.init_app(app)

    login_manager.init_app(app)

    login_manager.login_view = "auth.login"

    with app.app_context():
        db.create_all()

    from routes.auth import auth_bp
    from routes.events import events_bp
    from routes.student import student_bp
    from routes.organizer import organizer_bp
    from routes.admin import admin_bp
    from routes.comments import comments_bp
    from routes.attendance import attendance_bp
    from routes.certificates import certificates_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(events_bp)
    app.register_blueprint(student_bp)
    app.register_blueprint(organizer_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(comments_bp)
    app.register_blueprint(attendance_bp)
    app.register_blueprint(certificates_bp)

    return app


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
