"""
SQLite database module for FuturePlan.

Tables
------
intake_sessions  – one row per intake session (youth_id, caseworker, timestamps)
intake_answers   – one row per question/answer pair per session
case_notes       – caseworker notes and follow-up dates
"""

import sqlite3
from datetime import datetime, date
from typing import Optional

DB_PATH = "futureplan.db"


# ---------------------------------------------------------------------------
# Connection helper
# ---------------------------------------------------------------------------

def _get_conn() -> sqlite3.Connection:
    # check_same_thread=False is safe here because every helper opens a fresh
    # connection, performs its operation, and closes it immediately — no
    # connection object is shared between threads.
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


# ---------------------------------------------------------------------------
# Schema initialisation
# ---------------------------------------------------------------------------

def init_db() -> None:
    conn = _get_conn()
    cur = conn.cursor()

    cur.executescript(
        """
        CREATE TABLE IF NOT EXISTS intake_sessions (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            youth_id        TEXT    NOT NULL,
            youth_name      TEXT    NOT NULL,
            caseworker      TEXT    NOT NULL,
            created_at      TEXT    NOT NULL,
            completed       INTEGER NOT NULL DEFAULT 0,
            risk_score      INTEGER,
            risk_level      TEXT,
            top_needs       TEXT,
            summary_text    TEXT
        );

        CREATE TABLE IF NOT EXISTS intake_answers (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id      INTEGER NOT NULL REFERENCES intake_sessions(id),
            question_key    TEXT    NOT NULL,
            question_text   TEXT    NOT NULL,
            answer          TEXT    NOT NULL,
            answered_at     TEXT    NOT NULL
        );

        CREATE TABLE IF NOT EXISTS case_notes (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            youth_id        TEXT    NOT NULL,
            caseworker      TEXT    NOT NULL,
            note_text       TEXT    NOT NULL,
            follow_up_date  TEXT,
            created_at      TEXT    NOT NULL
        );
        """
    )
    conn.commit()
    conn.close()


# ---------------------------------------------------------------------------
# Intake session operations
# ---------------------------------------------------------------------------

def save_intake_session(
    youth_id: str,
    youth_name: str,
    caseworker: str,
) -> int:
    """Create a new intake session and return its id."""
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO intake_sessions (youth_id, youth_name, caseworker, created_at, completed)
        VALUES (?, ?, ?, ?, 0)
        """,
        (youth_id, youth_name, caseworker, datetime.now().isoformat()),
    )
    session_id = cur.lastrowid
    conn.commit()
    conn.close()
    return session_id


def complete_intake_session(
    session_id: int,
    risk_score: int,
    risk_level: str,
    top_needs: list[str],
    summary_text: str,
) -> None:
    conn = _get_conn()
    conn.execute(
        """
        UPDATE intake_sessions
        SET completed = 1, risk_score = ?, risk_level = ?, top_needs = ?, summary_text = ?
        WHERE id = ?
        """,
        (risk_score, risk_level, ",".join(top_needs), summary_text, session_id),
    )
    conn.commit()
    conn.close()


def get_intake_session(session_id: int) -> Optional[dict]:
    conn = _get_conn()
    row = conn.execute(
        "SELECT * FROM intake_sessions WHERE id = ?", (session_id,)
    ).fetchone()
    conn.close()
    return dict(row) if row else None


def get_sessions_for_youth(youth_id: str) -> list[dict]:
    conn = _get_conn()
    rows = conn.execute(
        "SELECT * FROM intake_sessions WHERE youth_id = ? ORDER BY created_at DESC",
        (youth_id,),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


# ---------------------------------------------------------------------------
# Intake answer operations
# ---------------------------------------------------------------------------

def save_intake_answer(
    session_id: int,
    question_key: str,
    question_text: str,
    answer: str,
) -> None:
    conn = _get_conn()
    conn.execute(
        """
        INSERT INTO intake_answers (session_id, question_key, question_text, answer, answered_at)
        VALUES (?, ?, ?, ?, ?)
        """,
        (session_id, question_key, question_text, answer, datetime.now().isoformat()),
    )
    conn.commit()
    conn.close()


def get_intake_answers(session_id: int) -> list[dict]:
    conn = _get_conn()
    rows = conn.execute(
        "SELECT * FROM intake_answers WHERE session_id = ? ORDER BY id",
        (session_id,),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


# ---------------------------------------------------------------------------
# Case notes operations
# ---------------------------------------------------------------------------

def save_case_note(
    youth_id: str,
    caseworker: str,
    note_text: str,
    follow_up_date: Optional[str] = None,
) -> None:
    conn = _get_conn()
    conn.execute(
        """
        INSERT INTO case_notes (youth_id, caseworker, note_text, follow_up_date, created_at)
        VALUES (?, ?, ?, ?, ?)
        """,
        (youth_id, caseworker, note_text, follow_up_date, datetime.now().isoformat()),
    )
    conn.commit()
    conn.close()


def get_case_notes(youth_id: str) -> list[dict]:
    conn = _get_conn()
    rows = conn.execute(
        "SELECT * FROM case_notes WHERE youth_id = ? ORDER BY created_at DESC",
        (youth_id,),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]
