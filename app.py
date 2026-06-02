"""
FuturePlan – Youth Services Case Management Demo
================================================
A Streamlit demo application for youth-serving caseworkers.

⚠️  DISCLAIMER: All names, cases, and personal details in this application
are entirely fictional and created for demonstration purposes only.
No real youth or client data is used or stored.

Run with:  streamlit run app.py
"""

import streamlit as st
from datetime import date, datetime, timedelta
import pandas as pd

from database import (
    init_db,
    save_intake_session,
    save_intake_answer,
    complete_intake_session,
    get_intake_answers,
    get_intake_session,
    get_sessions_for_youth,
    save_case_note,
    get_case_notes,
)
from sample_data import (
    CASEWORKER,
    get_sample_cases,
    get_amara_profile,
    get_resources,
    INTAKE_QUESTIONS,
)

# ---------------------------------------------------------------------------
# App-wide config
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="FuturePlan – Youth Services",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# CSS polish
# ---------------------------------------------------------------------------

st.markdown(
    """
    <style>
        /* Global font */
        html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

        /* Sidebar brand */
        .sidebar-brand {
            font-size: 1.4rem;
            font-weight: 700;
            color: #4F46E5;
            margin-bottom: 0.25rem;
        }
        .sidebar-sub {
            font-size: 0.78rem;
            color: #6B7280;
            margin-bottom: 1.5rem;
        }

        /* Metric cards */
        .metric-card {
            background: #F9FAFB;
            border: 1px solid #E5E7EB;
            border-radius: 12px;
            padding: 1rem 1.25rem;
            text-align: center;
        }
        .metric-card .metric-value {
            font-size: 2rem;
            font-weight: 700;
            color: #1F2937;
        }
        .metric-card .metric-label {
            font-size: 0.8rem;
            color: #6B7280;
            margin-top: 0.2rem;
        }

        /* Risk badges */
        .badge-high   { background:#FEE2E2; color:#991B1B; border-radius:8px; padding:2px 10px; font-size:0.8rem; font-weight:600; }
        .badge-medium { background:#FEF3C7; color:#92400E; border-radius:8px; padding:2px 10px; font-size:0.8rem; font-weight:600; }
        .badge-low    { background:#D1FAE5; color:#065F46; border-radius:8px; padding:2px 10px; font-size:0.8rem; font-weight:600; }

        /* Section headers */
        .section-header {
            font-size: 1.1rem;
            font-weight: 600;
            color: #1F2937;
            border-left: 4px solid #4F46E5;
            padding-left: 0.75rem;
            margin: 1.25rem 0 0.75rem 0;
        }

        /* Alert box */
        .alert-box {
            background: #FFF7ED;
            border: 1px solid #FDBA74;
            border-radius: 10px;
            padding: 0.85rem 1rem;
            margin-bottom: 0.5rem;
            font-size: 0.9rem;
        }

        /* Question card */
        .question-card {
            background: #EEF2FF;
            border: 1px solid #C7D2FE;
            border-radius: 12px;
            padding: 1.25rem 1.5rem;
            margin-bottom: 1rem;
        }

        /* Disclaimer banner */
        .disclaimer {
            background: #ECFDF5;
            border: 1px solid #6EE7B7;
            border-radius: 10px;
            padding: 0.65rem 1rem;
            font-size: 0.78rem;
            color: #065F46;
            margin-bottom: 1rem;
        }

        /* Hide Streamlit default header/footer */
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }

        div[data-testid="stSidebarNav"] { display: none; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Database init (once per session)
# ---------------------------------------------------------------------------

if "db_ready" not in st.session_state:
    init_db()
    st.session_state.db_ready = True

# ---------------------------------------------------------------------------
# Session state defaults
# ---------------------------------------------------------------------------

def _init_state():
    defaults = {
        "page": "dashboard",
        "intake_session_id": None,
        "intake_step": 0,
        "intake_answers": {},
        "intake_complete": False,
        "intake_risk_score": 0,
        "intake_risk_level": "Low",
        "intake_needs": [],
        "show_amara_profile": False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

_init_state()


# ---------------------------------------------------------------------------
# Navigation helpers
# ---------------------------------------------------------------------------

def nav_to(page: str):
    st.session_state.page = page
    st.rerun()


# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------

with st.sidebar:
    st.markdown(
        '<div class="sidebar-brand">🌟 FuturePlan</div>'
        '<div class="sidebar-sub">Youth Services Platform</div>',
        unsafe_allow_html=True,
    )

    st.markdown(f"**👤 {CASEWORKER['name']}**")
    st.caption(f"{CASEWORKER['title']}")
    st.caption(f"{CASEWORKER['agency']}")
    st.divider()

    pages = {
        "dashboard": "🏠  Dashboard",
        "youth_profile": "👤  Youth Profile – Amara",
        "intake_flow": "📋  Intake Assessment",
        "summary": "🧠  AI Summary",
        "resources": "🔗  Resource Recommendations",
        "action_plan": "📅  30/60/90 Action Plan",
        "case_notes": "📝  Case Notes",
    }

    for key, label in pages.items():
        is_active = st.session_state.page == key
        if st.button(
            label,
            key=f"nav_{key}",
            use_container_width=True,
            type="primary" if is_active else "secondary",
        ):
            nav_to(key)

    st.divider()
    st.markdown(
        '<div class="disclaimer">'
        "⚠️ <strong>Demo Mode</strong> — All data is fictional and for demonstration purposes only."
        "</div>",
        unsafe_allow_html=True,
    )


# ===========================================================================
# PAGE: CASEWORKER DASHBOARD
# ===========================================================================

def page_dashboard():
    st.title("🏠 Caseworker Dashboard")
    st.caption(f"Welcome back, **{CASEWORKER['name']}** · {date.today().strftime('%A, %B %d, %Y')}")

    st.markdown(
        '<div class="disclaimer">'
        "⚠️ <strong>Fake Data Disclaimer:</strong> All cases, names, and details shown are entirely fictional and exist for demonstration purposes only."
        "</div>",
        unsafe_allow_html=True,
    )

    cases = get_sample_cases()
    today = date.today()

    high_risk = sum(1 for c in cases if c["risk"] == "High")
    alerts = sum(1 for c in cases if c["alert"])
    due_today = sum(1 for c in cases if c["follow_up"] <= today)

    # Summary metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(
            f'<div class="metric-card"><div class="metric-value">{len(cases)}</div>'
            '<div class="metric-label">Assigned Cases</div></div>',
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            f'<div class="metric-card"><div class="metric-value" style="color:#DC2626">{high_risk}</div>'
            '<div class="metric-label">High-Risk Youth</div></div>',
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            f'<div class="metric-card"><div class="metric-value" style="color:#D97706">{alerts}</div>'
            '<div class="metric-label">Active Alerts</div></div>',
            unsafe_allow_html=True,
        )
    with col4:
        st.markdown(
            f'<div class="metric-card"><div class="metric-value" style="color:#7C3AED">{due_today}</div>'
            '<div class="metric-label">Follow-Ups Due</div></div>',
            unsafe_allow_html=True,
        )

    st.markdown("")

    # High-risk / alert section
    alert_cases = [c for c in cases if c["alert"]]
    if alert_cases:
        st.markdown('<div class="section-header">🚨 High-Risk Alerts</div>', unsafe_allow_html=True)
        for c in alert_cases:
            with st.container():
                col_a, col_b, col_c = st.columns([3, 2, 1])
                with col_a:
                    risk_color = {"High": "badge-high", "Medium": "badge-medium", "Low": "badge-low"}.get(c["risk"], "badge-low")
                    st.markdown(
                        f"**{c['name']}** (Age {c['age']}) &nbsp;"
                        f'<span class="{risk_color}">{c["risk"]} Risk</span>',
                        unsafe_allow_html=True,
                    )
                    st.caption(f"📌 {c['notes']}")
                with col_b:
                    st.caption(f"Program: {c['program']}")
                    follow_label = "Today" if c["follow_up"] == today else c["follow_up"].strftime("%b %d")
                    st.caption(f"Follow-up: **{follow_label}**")
                with col_c:
                    if c["id"] == "YC-1042":
                        if st.button("Open Amara's Case", key=f"open_{c['id']}", type="primary"):
                            nav_to("youth_profile")
                    else:
                        st.button("View Case", key=f"open_{c['id']}", disabled=True)
                st.divider()

    # Full caseload table
    st.markdown('<div class="section-header">📋 Full Caseload</div>', unsafe_allow_html=True)

    df_data = []
    for c in cases:
        follow_label = "⚠️ Today" if c["follow_up"] == today else c["follow_up"].strftime("%b %d, %Y")
        df_data.append(
            {
                "ID": c["id"],
                "Name": c["name"],
                "Age": c["age"],
                "Risk": c["risk"],
                "Status": c["status"],
                "Program": c["program"],
                "Follow-Up": follow_label,
            }
        )
    df = pd.DataFrame(df_data)
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.markdown("")
    st.info("💡 **Tip:** Click **Open Amara's Case** above or use the sidebar to navigate to the full youth profile.")


# ===========================================================================
# PAGE: YOUTH PROFILE
# ===========================================================================

def page_youth_profile():
    profile = get_amara_profile()

    st.title(f"👤 Youth Profile — {profile['name']}")
    st.caption(f"Case ID: {profile['id']} · Caseworker: {profile['caseworker']} · Status: **{profile['status']}**")

    st.markdown(
        '<div class="disclaimer">'
        "⚠️ <strong>Fake Data Disclaimer:</strong> This profile is entirely fictional and for demonstration purposes only."
        "</div>",
        unsafe_allow_html=True,
    )

    # Risk score banner
    risk_color_map = {"High": "#FEE2E2", "Medium": "#FEF3C7", "Low": "#D1FAE5"}
    risk_text_map = {"High": "#991B1B", "Medium": "#92400E", "Low": "#065F46"}
    bg = risk_color_map.get(profile["risk_level"], "#F9FAFB")
    fg = risk_text_map.get(profile["risk_level"], "#1F2937")
    st.markdown(
        f'<div style="background:{bg};border-radius:12px;padding:1rem 1.5rem;margin-bottom:1rem;">'
        f'<span style="font-size:1.5rem;font-weight:700;color:{fg}">Risk Score: {profile["risk_score"]} / 20 — {profile["risk_level"]} Risk</span>'
        "</div>",
        unsafe_allow_html=True,
    )

    tab1, tab2, tab3, tab4 = st.tabs(["📄 Profile", "🚨 Alerts & Actions", "🔧 Services", "📝 Background"])

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="section-header">Basic Information</div>', unsafe_allow_html=True)
            st.markdown(f"**Name:** {profile['name']}")
            st.markdown(f"**Date of Birth:** {profile['dob'].strftime('%B %d, %Y')} (Age {profile['age']})")
            st.markdown(f"**Gender:** {profile['gender']}")
            st.markdown(f"**Race / Ethnicity:** {profile['race_ethnicity']}")
            st.markdown(f"**Intake Date:** {profile['intake_date'].strftime('%B %d, %Y')}")

            st.markdown('<div class="section-header">Contact</div>', unsafe_allow_html=True)
            st.markdown(f"**Phone:** {profile['phone']}")
            st.markdown(f"**Email:** {profile['email']}")
            st.markdown(f"**Emergency Contact:** {profile['emergency_contact']}")

        with col2:
            st.markdown('<div class="section-header">Housing & Education</div>', unsafe_allow_html=True)
            st.markdown(f"**Housing Status:** {profile['housing_status']}")
            st.markdown(f"**School:** {profile['school']}")
            st.markdown(f"**Grade:** {profile['grade']}")

    with tab2:
        st.markdown('<div class="section-header">🚨 Active Alerts</div>', unsafe_allow_html=True)
        for alert in profile["alerts"]:
            st.markdown(
                f'<div class="alert-box">{alert}</div>',
                unsafe_allow_html=True,
            )

        st.markdown('<div class="section-header">✅ Recommended Next Actions</div>', unsafe_allow_html=True)
        for i, action in enumerate(profile["next_actions"], 1):
            st.markdown(f"**{i}.** {action}")

        st.markdown("")
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("📋 Start New Intake Assessment", type="primary", use_container_width=True):
                # Reset intake state
                st.session_state.intake_session_id = None
                st.session_state.intake_step = 0
                st.session_state.intake_answers = {}
                st.session_state.intake_complete = False
                st.session_state.intake_risk_score = 0
                st.session_state.intake_needs = []
                nav_to("intake_flow")
        with col_b:
            if st.button("📝 Add Case Note", use_container_width=True):
                nav_to("case_notes")

    with tab3:
        st.markdown('<div class="section-header">Enrolled Services</div>', unsafe_allow_html=True)
        for svc in profile["services"]:
            status_icon = {"Active": "🟢", "Enrolled": "🔵", "Pending Match": "🟡"}.get(svc["status"], "⚪")
            st.markdown(
                f"{status_icon} **{svc['name']}** — {svc['provider']} *(Status: {svc['status']})*"
            )

    with tab4:
        st.markdown('<div class="section-header">Background & Context</div>', unsafe_allow_html=True)
        st.write(profile["background"])


# ===========================================================================
# PAGE: INTAKE FLOW
# ===========================================================================

def _compute_risk(answers: dict) -> tuple[int, str, list[str]]:
    """Compute risk score, level, and needs list from intake answers."""
    score = 0
    needs = set()

    for q in INTAKE_QUESTIONS:
        key = q["key"]
        answer = answers.get(key)
        if answer is None:
            continue
        score += q["risk_map"].get(answer, 0)
        for need in q["needs_map"].get(answer, []):
            needs.add(need)

    if score <= 4:
        level = "Low"
    elif score <= 9:
        level = "Medium"
    else:
        level = "High"

    return score, level, sorted(needs)


def page_intake_flow():
    profile = get_amara_profile()
    st.title("📋 AI-Assisted Intake Assessment")
    st.caption(f"Youth: **{profile['name']}** (ID: {profile['id']}) · Caseworker: **{CASEWORKER['name']}**")

    st.markdown(
        '<div class="disclaimer">'
        "⚠️ <strong>Demo Mode:</strong> This simulates a guided intake flow. No real data is transmitted."
        "</div>",
        unsafe_allow_html=True,
    )

    total = len(INTAKE_QUESTIONS)

    # Start session if not yet started
    if st.session_state.intake_session_id is None:
        session_id = save_intake_session(
            youth_id=profile["id"],
            youth_name=profile["name"],
            caseworker=CASEWORKER["name"],
        )
        st.session_state.intake_session_id = session_id

    if st.session_state.intake_complete:
        st.success("✅ Intake assessment complete! Proceed to the AI Summary below.")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🧠 View AI Summary", type="primary", use_container_width=True):
                nav_to("summary")
        with col2:
            if st.button("🔄 Restart Intake", use_container_width=True):
                st.session_state.intake_session_id = None
                st.session_state.intake_step = 0
                st.session_state.intake_answers = {}
                st.session_state.intake_complete = False
                st.session_state.intake_risk_score = 0
                st.session_state.intake_needs = []
                st.rerun()
        return

    step = st.session_state.intake_step

    # Progress bar
    progress = step / total
    st.progress(progress, text=f"Question {step + 1} of {total}")

    # Show answered questions (read-only recap)
    if step > 0:
        with st.expander(f"✅ {step} question(s) answered — click to review", expanded=False):
            for i in range(step):
                q = INTAKE_QUESTIONS[i]
                ans = st.session_state.intake_answers.get(q["key"], "—")
                st.markdown(f"**{i+1}. {q['question']}**")
                st.markdown(f"&nbsp;&nbsp;&nbsp;📌 *{ans}*")
                st.markdown("---")

    # Current question
    q = INTAKE_QUESTIONS[step]
    st.markdown(
        f'<div class="question-card">'
        f'<div style="font-size:0.85rem;color:#6366F1;font-weight:600;margin-bottom:0.5rem;">'
        f"QUESTION {step + 1} OF {total}</div>"
        f'<div style="font-size:1.15rem;font-weight:600;color:#1F2937;">{q["question"]}</div>'
        f"</div>",
        unsafe_allow_html=True,
    )

    # Pre-select existing answer if going back
    existing = st.session_state.intake_answers.get(q["key"])
    default_idx = q["options"].index(existing) if existing in q["options"] else 0

    selected = st.radio(
        "Select an answer:",
        options=q["options"],
        index=default_idx,
        key=f"radio_{q['key']}",
        label_visibility="collapsed",
    )

    col_prev, col_next = st.columns([1, 3])
    with col_prev:
        if step > 0:
            if st.button("← Back", use_container_width=True):
                st.session_state.intake_step -= 1
                st.rerun()
    with col_next:
        btn_label = "Next Question →" if step < total - 1 else "✅ Complete Intake"
        if st.button(btn_label, type="primary", use_container_width=True):
            # Save answer to state
            st.session_state.intake_answers[q["key"]] = selected
            # Persist to DB
            save_intake_answer(
                session_id=st.session_state.intake_session_id,
                question_key=q["key"],
                question_text=q["question"],
                answer=selected,
            )
            if step < total - 1:
                st.session_state.intake_step += 1
                st.rerun()
            else:
                # Compute risk and complete session
                score, level, needs = _compute_risk(st.session_state.intake_answers)
                st.session_state.intake_risk_score = score
                st.session_state.intake_risk_level = level
                st.session_state.intake_needs = needs

                summary = _generate_summary_text(score, level, needs)
                complete_intake_session(
                    session_id=st.session_state.intake_session_id,
                    risk_score=score,
                    risk_level=level,
                    top_needs=needs,
                    summary_text=summary,
                )
                st.session_state.intake_complete = True
                st.rerun()


# ===========================================================================
# PAGE: AI SUMMARY
# ===========================================================================

NEED_LABELS = {
    "housing": "Stable Housing",
    "food": "Food Security",
    "education": "Education / GED",
    "employment": "Employment / Job Training",
    "id_support": "ID & Documentation",
    "counseling": "Mental Health Counseling",
    "mental_health": "Mental Health Services",
    "substance_support": "Substance Use Support",
    "legal": "Legal Aid",
    "mentorship": "Mentorship",
    "peer_support": "Peer Support",
    "safety": "Safety Planning",
    "trauma_informed": "Trauma-Informed Care",
    "crisis": "Crisis Intervention",
}

NEED_PRIORITY = {
    "crisis": 0,
    "safety": 1,
    "housing": 2,
    "food": 3,
    "mental_health": 4,
    "counseling": 5,
    "trauma_informed": 6,
    "substance_support": 7,
    "legal": 8,
    "id_support": 9,
    "education": 10,
    "employment": 11,
    "mentorship": 12,
    "peer_support": 13,
}


def _generate_summary_text(score: int, level: str, needs: list[str]) -> str:
    lines = [f"Risk Level: {level} (score {score}/20)."]
    if needs:
        top = [NEED_LABELS.get(n, n) for n in needs[:3]]
        lines.append(f"Primary needs identified: {', '.join(top)}.")
    return " ".join(lines)


def page_summary():
    profile = get_amara_profile()
    st.title("🧠 AI-Generated Intake Summary")
    st.caption(f"Youth: **{profile['name']}** · Session ID: {st.session_state.get('intake_session_id', '—')}")

    st.markdown(
        '<div class="disclaimer">'
        "⚠️ <strong>Demo Mode:</strong> This summary is generated by rule-based logic for demonstration purposes. "
        "It is not clinical advice."
        "</div>",
        unsafe_allow_html=True,
    )

    if not st.session_state.get("intake_complete"):
        st.warning("No completed intake session found. Please complete the intake assessment first.")
        if st.button("Go to Intake Assessment"):
            nav_to("intake_flow")
        return

    score = st.session_state.intake_risk_score
    level = st.session_state.intake_risk_level
    needs = st.session_state.intake_needs

    # Risk level banner
    risk_color_map = {"High": "#FEE2E2", "Medium": "#FEF3C7", "Low": "#D1FAE5"}
    risk_text_map = {"High": "#991B1B", "Medium": "#92400E", "Low": "#065F46"}
    risk_icon_map = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}
    bg = risk_color_map.get(level, "#F9FAFB")
    fg = risk_text_map.get(level, "#1F2937")
    icon = risk_icon_map.get(level, "⚪")

    st.markdown(
        f'<div style="background:{bg};border-radius:12px;padding:1.25rem 1.5rem;margin-bottom:1.25rem;">'
        f'<div style="font-size:1.6rem;font-weight:700;color:{fg}">{icon} {level} Risk</div>'
        f'<div style="font-size:1rem;color:{fg};margin-top:0.25rem;">Composite Risk Score: <strong>{score} / 20</strong></div>'
        f"</div>",
        unsafe_allow_html=True,
    )

    # Urgency statement
    if level == "High":
        urgency = "**Immediate action required.** Multiple high-risk factors identified. Prioritize safety, housing stability, and crisis support."
    elif level == "Medium":
        urgency = "**Elevated concern.** Several needs identified that require timely follow-up and service connection."
    else:
        urgency = "**Monitoring recommended.** Youth has protective factors in place; continue check-ins and support."

    st.info(f"🎯 **Urgency:** {urgency}")

    # Needs breakdown
    if needs:
        sorted_needs = sorted(needs, key=lambda n: NEED_PRIORITY.get(n, 99))
        top_needs = sorted_needs[:3]
        secondary_needs = sorted_needs[3:]

        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="section-header">🔴 Top Needs (Primary)</div>', unsafe_allow_html=True)
            for n in top_needs:
                st.markdown(f"• **{NEED_LABELS.get(n, n)}**")

        with col2:
            if secondary_needs:
                st.markdown('<div class="section-header">🟡 Secondary Needs</div>', unsafe_allow_html=True)
                for n in secondary_needs:
                    st.markdown(f"• {NEED_LABELS.get(n, n)}")
            else:
                st.markdown('<div class="section-header">✅ No Secondary Needs Identified</div>', unsafe_allow_html=True)

    # Answers recap
    st.markdown('<div class="section-header">📋 Intake Answers</div>', unsafe_allow_html=True)
    answers = st.session_state.intake_answers
    for q in INTAKE_QUESTIONS:
        ans = answers.get(q["key"])
        if ans:
            st.markdown(f"**{q['question']}**")
            st.markdown(f"&nbsp;&nbsp;&nbsp;→ *{ans}*")
            st.markdown("")

    # Next step buttons
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("🔗 View Resource Recommendations", type="primary", use_container_width=True):
            nav_to("resources")
    with col_b:
        if st.button("📅 View 30/60/90 Action Plan", use_container_width=True):
            nav_to("action_plan")


# ===========================================================================
# PAGE: RESOURCE RECOMMENDATIONS
# ===========================================================================

def page_resources():
    profile = get_amara_profile()
    st.title("🔗 Resource Recommendations")
    st.caption(f"Youth: **{profile['name']}** · Based on completed intake assessment")

    st.markdown(
        '<div class="disclaimer">'
        "⚠️ All resource listings are fictional placeholders for demonstration purposes only."
        "</div>",
        unsafe_allow_html=True,
    )

    if not st.session_state.get("intake_complete"):
        st.warning("No completed intake session found. Please complete the intake assessment first.")
        if st.button("Go to Intake Assessment"):
            nav_to("intake_flow")
        return

    needs = st.session_state.intake_needs
    all_resources = get_resources()

    if not needs:
        st.success("✅ No urgent resource needs identified based on this intake.")
        return

    sorted_needs = sorted(needs, key=lambda n: NEED_PRIORITY.get(n, 99))

    st.markdown(
        f"**{len(sorted_needs)} need area(s) identified.** Matched resources are shown below, "
        "ordered by priority. The caseworker should review and confirm appropriateness before referral."
    )

    for need_key in sorted_needs:
        resources = all_resources.get(need_key, [])
        if not resources:
            continue

        label = NEED_LABELS.get(need_key, need_key)
        st.markdown(f'<div class="section-header">📌 {label}</div>', unsafe_allow_html=True)

        for r in resources:
            with st.container():
                col_a, col_b = st.columns([3, 1])
                with col_a:
                    st.markdown(f"**{r['name']}** — *{r['type']}*")
                    st.write(r["description"])
                    st.caption(f"📞 {r['contact']}")
                    st.caption(f"✔️ Eligibility: {r['eligibility']}")
                with col_b:
                    st.button(
                        "📋 Refer",
                        key=f"refer_{need_key}_{r['name'][:20]}",
                        help="(Demo only — referral tracking not implemented)",
                        disabled=True,
                    )
                st.markdown("---")

    # Navigation
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("📅 View 30/60/90 Action Plan", type="primary", use_container_width=True):
            nav_to("action_plan")
    with col_b:
        if st.button("📝 Add Case Note", use_container_width=True):
            nav_to("case_notes")


# ===========================================================================
# PAGE: 30/60/90 ACTION PLAN
# ===========================================================================

ACTION_TEMPLATES = {
    "housing": {
        30: "Connect youth to emergency/transitional housing program; submit shelter extension request if needed.",
        60: "Follow up on housing application status; explore long-term housing options (vouchers, host homes).",
        90: "Confirm permanent or stable housing placement; transition to independent-living supports.",
    },
    "food": {
        30: "Connect youth to nearest food pantry and meal program; confirm access within this week.",
        60: "Ensure ongoing food access; explore SNAP eligibility and enrollment.",
        90: "Assess food stability; link to long-term nutrition and benefits programs.",
    },
    "education": {
        30: "Contact school liaison to address attendance barriers; enroll in GED program if needed.",
        60: "Monitor school attendance and progress; address transportation or scheduling barriers.",
        90: "Review academic standing; plan for next semester enrollment or graduation pathway.",
    },
    "employment": {
        30: "Enroll youth in job readiness workshop; assist with resume and application materials.",
        60: "Support job search and interview prep; connect to paid internship opportunities.",
        90: "Review employment status; address any workplace challenges or barriers.",
    },
    "id_support": {
        30: "Schedule appointment with ID assistance program to gather available documents.",
        60: "Complete ID document applications (birth certificate, state ID, SSN card).",
        90: "Confirm all critical IDs obtained; store copies in case file.",
    },
    "counseling": {
        30: "Schedule initial counseling intake appointment at Sunrise Behavioral Health.",
        60: "Confirm regular therapy attendance; address scheduling barriers.",
        90: "Review counseling progress; adjust level of care if needed.",
    },
    "mental_health": {
        30: "Schedule full mental health assessment; confirm or initiate medication management.",
        60: "Monitor medication adherence; follow up on therapy engagement.",
        90: "Review mental health status with clinician; update treatment plan.",
    },
    "substance_support": {
        30: "Connect youth to Youth Recovery & Wellness Program; complete intake.",
        60: "Monitor engagement with recovery program; address relapse risk factors.",
        90: "Assess recovery progress; adjust support level as needed.",
    },
    "legal": {
        30: "Connect youth to Youth Legal Aid Clinic; confirm upcoming court dates.",
        60: "Ensure legal representation in place; attend court proceedings as support.",
        90: "Review case outcome; explore diversion or expungement options.",
    },
    "mentorship": {
        30: "Submit referral to Big Brothers Big Sisters; complete volunteer matching process.",
        60: "Confirm mentor match and first meeting; set expectations and goals.",
        90: "Check in on mentorship relationship quality; address any concerns.",
    },
    "peer_support": {
        30: "Enroll youth in Youth Peer Support Network; identify a peer group that fits.",
        60: "Monitor group attendance; gather youth feedback on experience.",
        90: "Assess impact of peer support; explore leadership opportunities for youth.",
    },
    "safety": {
        30: "Complete safety assessment; create and document safety plan with youth.",
        60: "Review safety plan; confirm ongoing safety; address any new threats.",
        90: "Re-evaluate safety situation; adjust plan or services as needed.",
    },
    "trauma_informed": {
        30: "Connect youth to Trauma Recovery Center; complete trauma-informed intake.",
        60: "Monitor trauma therapy progress; ensure trauma-informed approach across all services.",
        90: "Review trauma symptom trends; update treatment goals with clinician.",
    },
    "crisis": {
        30: "Conduct immediate safety assessment; connect to Crisis Stabilization Unit or 988 as needed.",
        60: "Follow up on crisis resolution; ensure stable support structure is in place.",
        90: "Review crisis history; build resilience and coping strategies with youth.",
    },
}


def page_action_plan():
    profile = get_amara_profile()
    st.title("📅 30 / 60 / 90 Day Action Plan")
    st.caption(f"Youth: **{profile['name']}** · Caseworker: **{CASEWORKER['name']}**")

    st.markdown(
        '<div class="disclaimer">'
        "⚠️ <strong>Demo Mode:</strong> This action plan is auto-generated from the intake for demonstration purposes."
        "</div>",
        unsafe_allow_html=True,
    )

    if not st.session_state.get("intake_complete"):
        st.warning("No completed intake session found. Please complete the intake assessment first.")
        if st.button("Go to Intake Assessment"):
            nav_to("intake_flow")
        return

    needs = st.session_state.intake_needs
    if not needs:
        st.success("✅ No urgent action items identified.")
        return

    sorted_needs = sorted(needs, key=lambda n: NEED_PRIORITY.get(n, 99))
    today = date.today()

    tab_30, tab_60, tab_90 = st.tabs([
        f"🟠 30 Days  (by {(today + timedelta(days=30)).strftime('%b %d')})",
        f"🟡 60 Days  (by {(today + timedelta(days=60)).strftime('%b %d')})",
        f"🟢 90 Days  (by {(today + timedelta(days=90)).strftime('%b %d')})",
    ])

    for tab, day in [(tab_30, 30), (tab_60, 60), (tab_90, 90)]:
        with tab:
            due_date = today + timedelta(days=day)
            st.markdown(f"**Target Completion: {due_date.strftime('%B %d, %Y')}**")
            st.markdown("")
            idx = 1
            for need_key in sorted_needs:
                template = ACTION_TEMPLATES.get(need_key, {}).get(day)
                if template:
                    label = NEED_LABELS.get(need_key, need_key)
                    st.markdown(f"**{idx}. [{label}]** {template}")
                    idx += 1

    # Export as text block
    st.markdown('<div class="section-header">📄 Plain Text Export</div>', unsafe_allow_html=True)
    lines = [f"30/60/90 Day Action Plan — {profile['name']} ({profile['id']})", f"Caseworker: {CASEWORKER['name']}", f"Generated: {today.strftime('%B %d, %Y')}", ""]
    for day in [30, 60, 90]:
        due_date = today + timedelta(days=day)
        lines.append(f"--- {day}-DAY ACTIONS (by {due_date.strftime('%B %d, %Y')}) ---")
        idx = 1
        for need_key in sorted_needs:
            template = ACTION_TEMPLATES.get(need_key, {}).get(day)
            if template:
                label = NEED_LABELS.get(need_key, need_key)
                lines.append(f"{idx}. [{label}] {template}")
                idx += 1
        lines.append("")

    plan_text = "\n".join(lines)
    st.text_area("Copy and paste this action plan:", value=plan_text, height=250, key="plan_export")

    # Navigation
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("📝 Add Case Note / Schedule Follow-Up", type="primary", use_container_width=True):
            nav_to("case_notes")
    with col_b:
        if st.button("🏠 Return to Dashboard", use_container_width=True):
            nav_to("dashboard")


# ===========================================================================
# PAGE: CASE NOTES & FOLLOW-UP DATE
# ===========================================================================

def page_case_notes():
    profile = get_amara_profile()
    st.title("📝 Case Notes & Follow-Up")
    st.caption(f"Youth: **{profile['name']}** · Caseworker: **{CASEWORKER['name']}**")

    st.markdown(
        '<div class="disclaimer">'
        "⚠️ <strong>Demo Mode:</strong> Notes are saved to a local SQLite database for demo purposes only."
        "</div>",
        unsafe_allow_html=True,
    )

    # Add new note
    st.markdown('<div class="section-header">➕ Add New Case Note</div>', unsafe_allow_html=True)

    with st.form("case_note_form", clear_on_submit=True):
        note_text = st.text_area(
            "Case Note",
            placeholder="Enter your case note here — observations, next steps, barriers, progress...",
            height=150,
        )
        follow_up_date = st.date_input(
            "Schedule Next Follow-Up / Review Date",
            value=date.today() + timedelta(days=7),
            min_value=date.today(),
        )
        submitted = st.form_submit_button("💾 Save Note", type="primary", use_container_width=True)

    if submitted:
        if note_text.strip():
            save_case_note(
                youth_id=profile["id"],
                caseworker=CASEWORKER["name"],
                note_text=note_text.strip(),
                follow_up_date=follow_up_date.isoformat(),
            )
            st.success(f"✅ Case note saved. Next follow-up scheduled for **{follow_up_date.strftime('%B %d, %Y')}**.")
            st.rerun()
        else:
            st.error("Please enter a note before saving.")

    # Existing notes
    st.markdown('<div class="section-header">📋 Previous Case Notes</div>', unsafe_allow_html=True)
    notes = get_case_notes(profile["id"])

    if not notes:
        st.info("No case notes yet. Add the first note above.")
    else:
        for note in notes:
            created = datetime.fromisoformat(note["created_at"])
            follow_up = note.get("follow_up_date")
            with st.container():
                col_a, col_b = st.columns([4, 1])
                with col_a:
                    st.markdown(f"**{created.strftime('%B %d, %Y at %I:%M %p')}** — {note['caseworker']}")
                    st.write(note["note_text"])
                with col_b:
                    if follow_up:
                        st.markdown(
                            f'<div style="background:#EEF2FF;border-radius:8px;padding:0.5rem;text-align:center;font-size:0.8rem;">'
                            f"<strong>Follow-Up</strong><br>{follow_up}</div>",
                            unsafe_allow_html=True,
                        )
                st.markdown("---")

    # Navigation
    if st.button("🏠 Return to Dashboard", use_container_width=True):
        nav_to("dashboard")


# ===========================================================================
# ROUTER
# ===========================================================================

PAGE_MAP = {
    "dashboard": page_dashboard,
    "youth_profile": page_youth_profile,
    "intake_flow": page_intake_flow,
    "summary": page_summary,
    "resources": page_resources,
    "action_plan": page_action_plan,
    "case_notes": page_case_notes,
}

current_page = st.session_state.get("page", "dashboard")
page_fn = PAGE_MAP.get(current_page, page_dashboard)
page_fn()
