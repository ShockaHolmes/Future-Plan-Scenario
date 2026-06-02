# FuturePlan – Youth Services Case Management Demo

> ⚠️ **All names, cases, and personal details in this application are entirely fictional and created for demonstration purposes only. No real youth or client data is used or stored.**

## Run the demo

1. Open a terminal in the project folder:

```bash
cd /Users/shocka/Future-Plan-Scenario
```

2. Install dependencies:

```bash
npm install
```

3. Start the dashboard (auto-opens browser):

```bash
npm start
```

4. Open the URL shown in the terminal (typically `http://localhost:5173/`).

5. Stop the server when done with `Ctrl + C`.

## One-click launch on macOS

If you prefer, you can start everything by double-clicking `start.command` in Finder.
This script will:

- install dependencies if needed
- start the Vite server
- open the dashboard in your browser

## Optional: production preview

1. Build the app:

```bash
npm run build
```

2. Start preview server:

```bash
npm run preview
```

3. Open the preview URL shown in terminal (typically `http://localhost:4173/`).

Currently, two official plugins are available:

- **Caseworker Dashboard** — assigned cases, high-risk alerts, and follow-ups due today
- **Youth Profile Page** — full profile for Amara Williams with risk score, alerts, services, and next actions
- **AI-Assisted Intake Flow** — 10 guided questions asked one at a time with progress tracking
- **AI Summary** — risk level, top needs, secondary needs, and urgency statement
- **Resource Recommendations** — matched resources (housing, counseling, ID support, education, legal, and more)
- **30/60/90 Day Action Plan** — auto-generated caseworker tasks from intake results
- **Case Notes & Follow-Up** — add notes and schedule the next review date, saved to SQLite

---

## Quick Start

```bash
pip install -r requirements.txt
streamlit run app.py
```

## File Structure

| File | Purpose |
|------|---------|
| `app.py` | Main Streamlit application (all pages and routing) |
| `database.py` | SQLite database module (`intake_sessions`, `intake_answers`, `case_notes`) |
| `sample_data.py` | Fictional sample data, intake questions, and resource catalog |
| `requirements.txt` | Python dependencies |

## Demo Script

1. Open the app — you land on **Denise Johnson's Dashboard** showing 6 fictional cases.
2. Click **"Open Amara's Case"** (or use the sidebar) to view Amara's full profile.
3. From the profile, click **"Start New Intake Assessment"** to begin the guided intake.
4. Answer all 10 questions (one at a time). Click **"Complete Intake"** on the last question.
5. Click **"View AI Summary"** to see the risk score, top needs, and urgency.
6. Navigate to **Resource Recommendations** to see matched community resources.
7. Open the **30/60/90 Action Plan** to review caseworker tasks and export the plan.
8. Go to **Case Notes** to add a note and schedule the next follow-up date.

---

## React + Vite (Future Path Dashboards)

This repository also includes a React/Vite front-end for the Future Path dashboards (Teen, Caseworker, and AI Assistant). To run it:

```bash
npm install
npm run dev
```
