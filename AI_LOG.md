# AI Assistance Log

## Overview

Generative AI tools (ChatGPT - OpenAI) were used throughout this project as coding assistants for brainstorming, debugging, database design clarification, and documentation drafting. All generated code and explanations were reviewed, tested, and modified before inclusion in the final application.

---

# 1. Database Design Assistance

## Prompt
- "Help me design a database schema for a bouldering workout tracker."
- "Provide relationships for climbers, training sessions, and session types."

## AI Output
- Suggested a normalized relational schema involving:
  - climbers
  - training_sessions
  - session_types
  - goals
  - session_activities
- Suggested primary and foreign key relationships.

## My Modification
- Simplified the schema for Project 3 by removing:
  - goals
  - session_activities
- Added:
  - last_session_date
- Adjusted attributes to match the Flask application requirements.

---

# 2. Flask Application Setup

## Prompt
- "Walk me through setting up a Flask project in VS Code."
- "Help me connect Flask with SQLAlchemy and SQLite."

## AI Output
- Generated starter Flask structure.
- Explained:
  - virtual environments
  - Flask app structure
  - SQLAlchemy configuration
  - route setup

## My Modification
- Customized the structure for:
  - climbers
  - sessions
  - dashboard routes
- Added additional templates and navigation.

---

# 3. CRUD Functionality

## Prompt
- "Help me implement Create, Read, Update, and Delete operations for climbers and sessions."

## AI Output
- Generated Flask routes and HTML form examples for:
  - adding climbers
  - viewing climbers
  - adding sessions
  - deleting sessions

## My Modification
- Modified route logic to match my database structure.
- Added:
  - validation
  - redirects
  - Bootstrap formatting
- Tested all CRUD operations locally.

---

# 4. Relationship Management

## Prompt
- "How do I display all sessions belonging to a climber?"

## AI Output
- Suggested SQLAlchemy relationship definitions and Jinja2 template loops.

## My Modification
- Implemented:
  - one-to-many relationship
  - climber detail page
  - session display formatting

---

# 5. Transaction Logic

## Prompt
- "Help me implement transaction logic when creating a session."

## AI Output
- Suggested:
  - inserting a session
  - updating last_session_date
  - committing both operations together
  - rollback handling

## My Modification
- Integrated transaction logic directly into the add_session route.
- Tested rollback behavior and session creation.

---

# 6. README.md Documentation

## Prompt
- "Generate a professional README.md for my Flask training tracker project."

## AI Output
- Generated:
  - installation instructions
  - project overview
  - feature descriptions
  - project structure

## My Modification
- Adjusted formatting and project-specific wording.
- Added details specific to my application structure.

---

# 7. NORMALIZATION.md Report

## Prompt
- "Generate a normalization report for my database schema."

## AI Output
- Generated:
  - functional dependencies
  - anomaly identification
  - decomposition steps
  - final relational schema explanation

## My Modification
- Verified all schema descriptions against the implemented Flask models.
- Adjusted explanations to match the final application scope.

---

# 8. schema.sql Generation

## Prompt
- "Generate a schema.sql file for my Flask application database."

## AI Output
- Generated SQL CREATE TABLE statements for:
  - climbers
  - session_types
  - training_sessions

## My Modification
- Verified schema consistency with SQLAlchemy models.
- Adjusted formatting and comments for submission readiness.

---

# 9. General Understanding of Project Stack

## Prompt
- "Explain how Flask templates, models, and routes work together."
- "Explain where the SQLite database is stored and how Flask saves data."
- "Help me understand how SQLAlchemy relationships work."
- "Help debug Flask routing and template errors."

## AI Output
- Explained how:
  - routes.py handles incoming requests
  - models.py defines database tables and relationships
  - templates render dynamic HTML using Jinja2
  - SQLAlchemy connects Flask to the SQLite database
  - data is stored locally inside instance/app.db
- Provided debugging assistance for:
  - BuildError exceptions
  - relationship conflicts
  - routing issues
  - template rendering issues
  - CRUD functionality problems

## My Modification
- Applied the explanations to implement and debug my own project structure.
- Adjusted routes, templates, and models to correctly match my application design.
- Verified all features locally by running and testing the Flask application.