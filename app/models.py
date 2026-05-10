from datetime import datetime
from app.extensions import db

class Climber(db.Model):
    __tablename__ = "climbers"

    climber_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    experience_level = db.Column(db.String(25), nullable=False)
    date_joined = db.Column(db.Date, nullable=False)
    last_session_date = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    sessions = db.relationship(
        "TrainingSession",
        backref="climber",
        cascade="all, delete-orphan"
    )


class SessionType(db.Model):
    __tablename__ = "session_types"

    session_type_id = db.Column(db.Integer, primary_key=True)
    session_type_name = db.Column(db.String(100), nullable=False)
    focus_area = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    sessions = db.relationship(
        "TrainingSession",
        backref="session_type"
    )


class TrainingSession(db.Model):
    __tablename__ = "training_sessions"

    session_id = db.Column(db.Integer, primary_key=True)
    climber_id = db.Column(db.Integer, db.ForeignKey("climbers.climber_id"), nullable=False)
    session_type_id = db.Column(db.Integer, db.ForeignKey("session_types.session_type_id"), nullable=False)

    session_date = db.Column(db.Date, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    perceived_intensity = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)