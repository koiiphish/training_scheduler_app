from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import func


from .extensions import db
from .models import Climber, SessionType, TrainingSession

main = Blueprint("main", __name__)


@main.route("/")
def index():
    total_climbers = Climber.query.count()
    total_sessions = TrainingSession.query.count()
    avg_duration = db.session.query(func.avg(TrainingSession.duration_minutes)).scalar()
    avg_intensity = db.session.query(func.avg(TrainingSession.perceived_intensity)).scalar()

    return render_template(
        "index.html",
        total_climbers=total_climbers,
        total_sessions=total_sessions,
        avg_duration=avg_duration,
        avg_intensity=avg_intensity
    )

@main.route("/seed")
def seed():
    if SessionType.query.count() == 0:
        session_types = [
            SessionType(
                session_type_name="4x4 Endurance",
                focus_area="Endurance",
                description="Repeated bouldering problems with short rest."
            ),
            SessionType(
                session_type_name="Hangboard Training",
                focus_area="Finger Strength",
                description="Finger strength training using hangboard edges."
            ),
            SessionType(
                session_type_name="Technique Training",
                focus_area="Technique",
                description="Footwork, body positioning, and movement drills."
            ),
            SessionType(
                session_type_name="Hard Bouldering",
                focus_area="Power",
                description="Projecting difficult boulders and limit attempts."
            ),
            SessionType(
                session_type_name="Mobility / Recovery",
                focus_area="Recovery",
                description="Stretching, mobility, and recovery work."
            )
        ]

        db.session.add_all(session_types)
        db.session.commit()

    return "Session types seeded!"

@main.route("/climbers/add", methods=["GET", "POST"])
def add_climber():
    if request.method == "POST":
        first_name = request.form["first_name"].strip()
        last_name = request.form["last_name"].strip()
        email = request.form["email"].strip()
        experience_level = request.form["experience_level"].strip()

        if not first_name or not last_name or not email or not experience_level:
            return "All fields are required."

        climber = Climber(
            first_name=first_name,
            last_name=last_name,
            email=email,
            experience_level=experience_level,
            date_joined=datetime.today().date()
        )

        db.session.add(climber)
        db.session.commit()

        return redirect(url_for("main.index"))

    return render_template("add_climber.html")

@main.route("/climbers")
def view_climbers():
    climbers = Climber.query.all()
    return render_template("climbers.html", climbers=climbers)

@main.route("/climbers/<int:climber_id>")
def climber_detail(climber_id):
    climber = Climber.query.get_or_404(climber_id)
    return render_template("climber_detail.html", climber=climber)

@main.route("/sessions/add", methods=["GET", "POST"])
def add_session():
    climbers = Climber.query.all()
    session_types = SessionType.query.all()

    if request.method == "POST":
        climber_id = int(request.form["climber_id"])
        session_type_id = int(request.form["session_type_id"])
        session_date = datetime.strptime(request.form["session_date"], "%Y-%m-%d").date()
        duration_minutes = int(request.form["duration_minutes"])
        perceived_intensity = int(request.form["perceived_intensity"])
        notes = request.form["notes"].strip()

        # Validation
        if duration_minutes <= 0:
            return "Duration must be greater than 0."

        if perceived_intensity < 1 or perceived_intensity > 10:
            return "Intensity must be between 1 and 10."

        session = TrainingSession(
            climber_id=climber_id,
            session_type_id=session_type_id,
            session_date=session_date,
            duration_minutes=duration_minutes,
            perceived_intensity=perceived_intensity,
            notes=notes
        )

        climber = Climber.query.get(climber_id)

        # Transaction Logic
        try:
            db.session.add(session)

            # update derived field
            climber.last_session_date = session_date

            db.session.commit()
        except:
            db.session.rollback()
            return "Transaction failed."

        return redirect(url_for("main.climber_detail", climber_id=climber_id))

    return render_template("add_session.html", climbers=climbers, session_types=session_types)