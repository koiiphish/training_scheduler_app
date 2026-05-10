# Database Normalization Report (3NF)

## Overview

This report evaluates the original database schema created during Project 2 and documents the normalization process into Third Normal Form (3NF). The purpose of normalization is to reduce redundancy, eliminate anomalies, and improve data integrity while supporting the functionality required by the Flask application. The Database was also simplified for the project, and details removed from the schema are noted below. 

---

# 1. Original Functional Dependencies

## Table: climbers

Functional Dependency:

```
climber_id → first_name, last_name, email, experience_level, date_joined, created_at
```

Explanation:
- Each climber_id uniquely identifies one climber record.

---

## Table: session_types

Functional Dependency:

```
session_type_id → session_type_name, focus_area, description, created_at
```

Explanation:
- Each session type ID uniquely identifies a training type.

---

## Table: training_sessions

Functional Dependency:

```
session_id → climber_id, session_type_id, session_date, duration_minutes,
perceived_intensity, notes, created_at
```

Explanation:
- Each training session uniquely determines all session-related attributes.

---

## Original Additional Tables from Project 2

### Table: session_activities

Functional Dependency:

```
activity_id → session_id, activity_name, sets_completed,
reps_completed, hold_time_seconds, rest_time_seconds,
grade_attempted, completion_status, training_load, created_at
```

---

### Table: goals

Functional Dependency:

```
goal_id → climber_id, goal_name, goal_category,
target_value, current_value, start_date,
end_date, goal_status, created_at
```

---

# 2. Anomaly Identification

## Update Anomalies

- If session type information were stored directly inside training_sessions, changing a session type name would require updating multiple rows.
- Repeated climber information across tables could lead to inconsistent updates.

Example:
- Updating "Hangboard Training" to "Finger Strength Training" would require updating every training session row containing that value.

---

## Insertion Anomalies

- A training session cannot exist without first creating a climber.
- A session activity cannot exist without a valid training session.
- A goal cannot exist without a valid climber.

---

## Deletion Anomalies

- Deleting a climber could unintentionally remove all related training sessions.
- Deleting a training session could remove all associated session activity information.

---

# 3. Decomposition Steps

## Step 1 — First Normal Form (1NF)

Requirements:
- Atomic values
- No repeating groups

Result:
- All tables already contained atomic attributes.
- No multi-valued attributes existed.

Example:
- experience_level stores only one value per row.

---

## Step 2 — Second Normal Form (2NF)

Requirements:
- Must already satisfy 1NF
- No partial dependencies

Result:
- All tables use single-column primary keys.
- All non-key attributes fully depend on the primary key.

Example:

```
climber_id → first_name, last_name, email
```

No attribute depends on only part of a composite key.

---

## Step 3 — Third Normal Form (3NF)

Requirements:
- Must satisfy 2NF
- No transitive dependencies

### Problem Identified

Session type information conceptually depends on:

```
session_type_id
```

not directly on:

```
session_id
```

### Solution

A separate table was maintained:

```
session_types
```

and referenced using a foreign key:

```
training_sessions.session_type_id
```

This removes redundancy and prevents repeated session type data.

---

# Simplification for Project 3 Application

The original schema from Project 2 included:

- session_activities
- goals

For Project 3, the application scope was simplified to focus on:
- climbers
- training_sessions
- session_types

This reduced application complexity while still satisfying:
- multi-table CRUD
- relationship management
- transaction logic
- dashboard aggregation requirements

---

# 4. Final Relational Schema

## Table: climbers

Attributes:
- climber_id (PK)
- first_name
- last_name
- email (UNIQUE)
- experience_level
- date_joined
- last_session_date
- created_at

---

## Table: session_types

Attributes:
- session_type_id (PK)
- session_type_name
- focus_area
- description
- created_at

---

## Table: training_sessions

Attributes:
- session_id (PK)
- climber_id (FK → climbers.climber_id)
- session_type_id (FK → session_types.session_type_id)
- session_date
- duration_minutes
- perceived_intensity
- notes
- created_at

---

# 5. 3NF Justification

The final schema satisfies Third Normal Form because:

- Each table has a primary key.
- All non-key attributes depend only on the primary key.
- There are no transitive dependencies between non-key attributes.
- Redundant data is minimized.

---

## Note on `last_session_date`

The attribute:

```
last_session_date
```

stored in the climbers table is technically a derived value because it can be calculated using:

```
MAX(training_sessions.session_date)
```

However, this value was intentionally stored to support application-level transaction logic.

When a training session is created:
1. A new session record is inserted.
2. The climber’s last_session_date is updated simultaneously.
3. Both operations occur in a single transaction.

This introduces controlled redundancy for application functionality and performance.

---

# Conclusion

The database schema was successfully normalized into Third Normal Form (3NF). The final structure minimizes redundancy, prevents update/insertion/deletion anomalies.

The resulting schema supports:
- multi-table CRUD operations
- one-to-many relationships
- transaction management
- aggregate dashboard queries
- data integrity through foreign keys and validation