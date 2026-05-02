# Bouldering/Climbing Training Tracker

A full-stack web application built using Flask and SQLAlchemy that allows users to track bouldering training sessions. 
Users can manage climbers, log workouts, 
and view training data through a simple dashboard.

---
## Project Structure

training_scheduler_app/
app/
init.py
extensions.py
models.py
routes.py
static/css/styles.css
templates/base.html
templates/index.html
templates/climbers.html
templates/add_climber.html
templates/climber_detail.html
templates/add_session.html
instance/
app.db
config.py
run.py
requirements.txt
.gitignore
README.md
NORMALIZATION.md
schema.sql

---
## Quick Start

1. Create and activate a virtual environment:

   python -m venv venv
   venv\Scripts\activate

2. Install dependencies:

   pip install -r requirements.txt

3. Run the application:

   python run.py

4. Open in browser:

   http://127.0.0.1:5000


## Database Setup

SQLite is used by default.
The database file is automatically created at:

   instance/app.db

Tables are created automatically at startup using:

   db.create_all()

Seed Initial Data

To add default session types, open:

   http://127.0.0.1:5000/seed

## Application Features

   # Climber Management
      Add new climbers
      View all climbers
      View individual climber details

   # Training Sessions
   Add training sessions linked to climbers
   Record session date, duration, intensity, and notes
   Select session type (e.g., 4x4, Hangboard, Technique)

   # Relationship Management
   One-to-many relationship between climbers and training sessions
   Each climber can have multiple sessions
   Sessions are displayed on the climber detail page
   
   # Transaction Logic
   Adding a session:
   Inserts a new training session
   Updates the climber’s last session date
   Uses a transaction (commit/rollback)

   # Data Validation
   Required fields enforced
   Duration must be greater than 0
   Intensity must be between 1 and 10

   # Dashboard
   Total number of climbers
   Total number of sessions
   Average session duration
   Average session intensity

   # Notes
The database (app.db) is stored locally and is not pushed to GitHub.
This project uses a Flask development server.
SQLAlchemy ORM is used to manage database interactions.

## Author 
Timothy Neoh
CS665 Project 3 — Bouldering Training Tracker

---

