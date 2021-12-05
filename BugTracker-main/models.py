from flask_sqlalchemy import SQLAlchemy
from config import app
from datetime import datetime

db = SQLAlchemy(app)


# Models
class bug_report(db.Model):
    # These are the database columns, where the data gets stored and read from
    _id = db.Column("id", db.Integer, primary_key=True)
    reporter_name = db.Column("reporter_name", db.Text(320))
    reporter_email = db.Column("reporter_email", db.Text(320))
    reporter_phone = db.Column("reporter_phone", db.Text(320))
    system = db.Column("system", db.Text(320))
    severity = db.Column("severity", db.Text(8))
    steps = db.Column("steps", db.Text(1024))
    message = db.Column("message", db.Text(1024))
    status = db.Column("status", db.Text(1024), default='Pending')
    time_of_report = db.Column("time_of_report", db.DateTime(
    ), default=datetime.utcnow(), nullable=False)

    def __init__(self, reporter_name, reporter_email, reporter_phone, system, severity, steps, message):
        self.reporter_name = reporter_name
        self.reporter_email = reporter_email
        self.reporter_phone = reporter_phone
        self.system = system
        self.severity = severity
        self.steps = steps
        self.message = message
