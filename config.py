import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    SECRET_KEY = os.getenv("SECRET_KEY", "super_secret_key")

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL")
      #  "mysql+pymysql://root:Qgjd%40rbjb@localhost/campus_events_db" #
    

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True

    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

    UPLOAD_FOLDER = "static/uploads"
    QR_FOLDER = "static/qr_codes"
