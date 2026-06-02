"""
Sample / fake data for the FuturePlan demo.
All names, cases, and details are entirely fictional.
"""

from datetime import date, timedelta

# ---------------------------------------------------------------------------
# Caseworker
# ---------------------------------------------------------------------------

CASEWORKER = {
    "name": "Denise Johnson",
    "title": "Senior Youth Case Manager",
    "agency": "Metro Youth & Family Services",
    "caseload": 18,
    "years_experience": 9,
}

# ---------------------------------------------------------------------------
# Assigned cases (dashboard list)
# ---------------------------------------------------------------------------

def get_sample_cases():
    today = date.today()
    return [
        {
            "id": "YC-1042",
            "name": "Amara Williams",
            "age": 16,
            "risk": "High",
            "status": "Active",
            "program": "Transitional Housing",
            "follow_up": today,
            "notes": "Missed last two appointments. Shelter placement at risk.",
            "alert": True,
        },
        {
            "id": "YC-0987",
            "name": "Marcus Deleon",
            "age": 17,
            "risk": "Medium",
            "status": "Active",
            "program": "Job Readiness",
            "follow_up": today + timedelta(days=3),
            "notes": "Enrolled in GED program, needs transportation support.",
            "alert": False,
        },
        {
            "id": "YC-1105",
            "name": "Kayla Thompson",
            "age": 15,
            "risk": "High",
            "status": "Active",
            "program": "Mental Health Services",
            "follow_up": today + timedelta(days=1),
            "notes": "Recently discharged from short-term residential. Monitoring closely.",
            "alert": True,
        },
        {
            "id": "YC-0834",
            "name": "Jordan Rivera",
            "age": 18,
            "risk": "Low",
            "status": "Transitioning Out",
            "program": "Independent Living",
            "follow_up": today + timedelta(days=14),
            "notes": "Secured part-time employment. Preparing for case closure.",
            "alert": False,
        },
        {
            "id": "YC-1198",
            "name": "Destiny Moore",
            "age": 16,
            "risk": "Medium",
            "status": "Active",
            "program": "Family Reunification",
            "follow_up": today + timedelta(days=5),
            "notes": "Family mediation scheduled next week.",
            "alert": False,
        },
        {
            "id": "YC-1203",
            "name": "Jaylen Carter",
            "age": 17,
            "risk": "High",
            "status": "New Intake",
            "program": "Pending Assessment",
            "follow_up": today + timedelta(days=2),
            "notes": "Referred by school counselor. No prior services.",
            "alert": True,
        },
    ]


# ---------------------------------------------------------------------------
# Amara Williams – full youth profile
# ---------------------------------------------------------------------------

def get_amara_profile():
    today = date.today()
    return {
        "id": "YC-1042",
        "name": "Amara Williams",
        "dob": date(2008, 3, 14),
        "age": 16,
        "gender": "Female (she/her)",
        "race_ethnicity": "Black / African American",
        "intake_date": today - timedelta(days=45),
        "caseworker": "Denise Johnson",
        "program": "Transitional Housing",
        "status": "Active",
        "risk_score": 14,
        "risk_level": "High",
        # Contact
        "phone": "(555) 204-8812",
        "email": "—",
        "emergency_contact": "Aunt Gloria Williams — (555) 204-0031",
        # Housing
        "housing_status": "Currently in emergency shelter (Metro Youth Shelter, Bed 7B). Placement review in 12 days.",
        # Education
        "school": "Lincoln High School (enrolled, irregular attendance)",
        "grade": "10th Grade",
        # Alerts
        "alerts": [
            "⚠️ Missed last two scheduled appointments (5/19 and 5/26)",
            "🏠 Shelter placement expires in 12 days — no permanent placement secured",
            "📋 Pending court date: Juvenile diversion hearing on 6/12",
            "💊 Mental health medication — last prescription filled 3 weeks ago",
        ],
        # Services enrolled
        "services": [
            {"name": "Emergency Shelter", "provider": "Metro Youth Shelter", "status": "Active"},
            {"name": "Individual Counseling", "provider": "Sunrise Behavioral Health", "status": "Active"},
            {"name": "GED/School Liaison", "provider": "Lincoln High School", "status": "Enrolled"},
            {"name": "Mentorship", "provider": "Big Brothers Big Sisters", "status": "Pending Match"},
        ],
        # Next actions
        "next_actions": [
            "Schedule make-up appointment by end of week",
            "Contact Metro Youth Shelter re: 30-day extension request",
            "Confirm attendance at June 12 juvenile diversion hearing",
            "Follow up with Sunrise Behavioral Health on medication refill",
            "Submit housing voucher application to HousingFirst YSP",
        ],
        # Background notes
        "background": (
            "Amara entered care after aging out of a foster family placement at 16. "
            "She has experienced multiple episodes of housing instability over the past year "
            "and has a history of anxiety and depression. She is motivated to complete school "
            "and has expressed interest in cosmetology or healthcare as a career path. "
            "Relationship with biological family is limited; her aunt Gloria is her primary support person."
        ),
    }


# ---------------------------------------------------------------------------
# Intake questions
# ---------------------------------------------------------------------------

INTAKE_QUESTIONS = [
    {
        "key": "housing",
        "question": "What is your current living situation?",
        "options": [
            "Stable housing (own/renting with family or independently)",
            "Staying with friends or family temporarily (couch surfing)",
            "Emergency shelter or transitional housing",
            "Unsheltered / sleeping outside or in a car",
            "Juvenile detention or residential facility",
        ],
        "risk_map": {
            "Stable housing (own/renting with family or independently)": 0,
            "Staying with friends or family temporarily (couch surfing)": 1,
            "Emergency shelter or transitional housing": 2,
            "Unsheltered / sleeping outside or in a car": 3,
            "Juvenile detention or residential facility": 2,
        },
        "needs_map": {
            "Staying with friends or family temporarily (couch surfing)": ["housing"],
            "Emergency shelter or transitional housing": ["housing"],
            "Unsheltered / sleeping outside or in a car": ["housing"],
            "Juvenile detention or residential facility": ["housing", "legal"],
        },
    },
    {
        "key": "food",
        "question": "Do you have reliable access to food on a daily basis?",
        "options": [
            "Yes, I have enough food",
            "Sometimes — it depends on the day",
            "No, I often don't have enough food",
        ],
        "risk_map": {
            "Yes, I have enough food": 0,
            "Sometimes — it depends on the day": 1,
            "No, I often don't have enough food": 2,
        },
        "needs_map": {
            "Sometimes — it depends on the day": ["food"],
            "No, I often don't have enough food": ["food"],
        },
    },
    {
        "key": "education",
        "question": "Are you currently in school, a training program, or working?",
        "options": [
            "Yes, enrolled in school full-time",
            "Yes, enrolled in school part-time or with irregular attendance",
            "In a job training or vocational program",
            "Working (part-time or full-time)",
            "Not currently in school, training, or work",
        ],
        "risk_map": {
            "Yes, enrolled in school full-time": 0,
            "Yes, enrolled in school part-time or with irregular attendance": 1,
            "In a job training or vocational program": 0,
            "Working (part-time or full-time)": 0,
            "Not currently in school, training, or work": 2,
        },
        "needs_map": {
            "Yes, enrolled in school part-time or with irregular attendance": ["education"],
            "Not currently in school, training, or work": ["education", "employment"],
        },
    },
    {
        "key": "id_docs",
        "question": "Do you have valid identification documents? (e.g., state ID, birth certificate, Social Security card)",
        "options": [
            "Yes, I have all my documents",
            "I have some but not all documents",
            "No, I don't have any documents",
        ],
        "risk_map": {
            "Yes, I have all my documents": 0,
            "I have some but not all documents": 1,
            "No, I don't have any documents": 2,
        },
        "needs_map": {
            "I have some but not all documents": ["id_support"],
            "No, I don't have any documents": ["id_support"],
        },
    },
    {
        "key": "trauma",
        "question": "Have you experienced abuse, neglect, or any form of violence recently or in the past?",
        "options": [
            "No",
            "Yes, in the past — not currently",
            "Yes, currently experiencing this",
            "I prefer not to answer",
        ],
        "risk_map": {
            "No": 0,
            "Yes, in the past — not currently": 2,
            "Yes, currently experiencing this": 3,
            "I prefer not to answer": 1,
        },
        "needs_map": {
            "Yes, in the past — not currently": ["counseling", "trauma_informed"],
            "Yes, currently experiencing this": ["counseling", "trauma_informed", "safety"],
        },
    },
    {
        "key": "mental_health",
        "question": "Are you currently experiencing any mental health concerns, or do you use substances (alcohol or drugs)?",
        "options": [
            "No mental health concerns or substance use",
            "I have mental health concerns but am currently getting support",
            "I have mental health concerns and am NOT getting support",
            "I use substances and would like help",
            "Both mental health concerns and substance use",
        ],
        "risk_map": {
            "No mental health concerns or substance use": 0,
            "I have mental health concerns but am currently getting support": 1,
            "I have mental health concerns and am NOT getting support": 2,
            "I use substances and would like help": 2,
            "Both mental health concerns and substance use": 3,
        },
        "needs_map": {
            "I have mental health concerns but am currently getting support": ["counseling"],
            "I have mental health concerns and am NOT getting support": ["counseling", "mental_health"],
            "I use substances and would like help": ["substance_support"],
            "Both mental health concerns and substance use": ["counseling", "mental_health", "substance_support"],
        },
    },
    {
        "key": "legal",
        "question": "Do you have any legal involvement, such as open cases, probation, or upcoming court dates?",
        "options": [
            "No legal involvement",
            "Yes, a closed or resolved matter",
            "Yes, I am on probation or have supervision requirements",
            "Yes, I have an open case or upcoming court date",
        ],
        "risk_map": {
            "No legal involvement": 0,
            "Yes, a closed or resolved matter": 0,
            "Yes, I am on probation or have supervision requirements": 2,
            "Yes, I have an open case or upcoming court date": 2,
        },
        "needs_map": {
            "Yes, I am on probation or have supervision requirements": ["legal"],
            "Yes, I have an open case or upcoming court date": ["legal"],
        },
    },
    {
        "key": "support",
        "question": "Do you have trusted adults or a supportive community you can turn to?",
        "options": [
            "Yes, I have strong family or community support",
            "I have one or two people I can rely on",
            "I have limited support",
            "No, I don't have anyone I can turn to",
        ],
        "risk_map": {
            "Yes, I have strong family or community support": 0,
            "I have one or two people I can rely on": 1,
            "I have limited support": 2,
            "No, I don't have anyone I can turn to": 3,
        },
        "needs_map": {
            "I have limited support": ["mentorship", "peer_support"],
            "No, I don't have anyone I can turn to": ["mentorship", "peer_support"],
        },
    },
    {
        "key": "goals",
        "question": "What is your primary goal right now?",
        "options": [
            "Find stable housing",
            "Finish school or get my GED",
            "Get a job or learn a trade",
            "Get mental health or emotional support",
            "Reconnect with family",
            "Stay safe and away from violence",
            "I'm not sure yet",
        ],
        "risk_map": {
            "Find stable housing": 0,
            "Finish school or get my GED": 0,
            "Get a job or learn a trade": 0,
            "Get mental health or emotional support": 0,
            "Reconnect with family": 0,
            "Stay safe and away from violence": 1,
            "I'm not sure yet": 0,
        },
        "needs_map": {
            "Find stable housing": ["housing"],
            "Finish school or get my GED": ["education"],
            "Get a job or learn a trade": ["employment"],
            "Get mental health or emotional support": ["counseling"],
            "Stay safe and away from violence": ["safety", "counseling"],
        },
    },
    {
        "key": "safety",
        "question": "Do you have any immediate safety concerns right now — for yourself or someone else?",
        "options": [
            "No, I feel safe",
            "I have some concerns but I'm okay right now",
            "Yes, I have an immediate safety concern",
        ],
        "risk_map": {
            "No, I feel safe": 0,
            "I have some concerns but I'm okay right now": 2,
            "Yes, I have an immediate safety concern": 4,
        },
        "needs_map": {
            "I have some concerns but I'm okay right now": ["safety"],
            "Yes, I have an immediate safety concern": ["safety", "crisis"],
        },
    },
]


# ---------------------------------------------------------------------------
# Resource catalog
# ---------------------------------------------------------------------------

def get_resources():
    return {
        "housing": [
            {
                "name": "HousingFirst Youth Support Program",
                "type": "Transitional Housing",
                "description": "Safe transitional housing for youth ages 16–24 experiencing homelessness. Up to 24-month placement with case management.",
                "contact": "(555) 800-4400 | housingfirstysp.org",
                "eligibility": "Ages 16–24, currently experiencing homelessness or housing instability",
            },
            {
                "name": "Metro Youth Emergency Shelter",
                "type": "Emergency Shelter",
                "description": "Immediate shelter (up to 90 days) with meals, hygiene supplies, and on-site case management.",
                "contact": "(555) 800-2200 | metroyouthshelter.org",
                "eligibility": "Ages 12–21, any youth in crisis",
            },
            {
                "name": "Rapid Re-Housing Voucher Program",
                "type": "Housing Voucher",
                "description": "Rental assistance vouchers for youth transitioning to independent living.",
                "contact": "(555) 800-3300 | cityhousingauth.gov/youth",
                "eligibility": "Ages 18–24 (or 16–17 with guardian consent)",
            },
        ],
        "food": [
            {
                "name": "City Youth Food Pantry Network",
                "type": "Food Assistance",
                "description": "Weekly food distribution at 12 locations. No ID required. Youth-specific hours available.",
                "contact": "(555) 700-1100 | cityfoodpantry.org",
                "eligibility": "Any youth in need; no documentation required",
            },
            {
                "name": "Community Kitchen & Meal Program",
                "type": "Meals",
                "description": "Hot meals served Monday–Saturday, 11am–1pm and 5pm–7pm. Carry-out available.",
                "contact": "(555) 700-2200 | communitykitchen.org",
                "eligibility": "Open to all",
            },
        ],
        "counseling": [
            {
                "name": "Sunrise Behavioral Health – Youth Track",
                "type": "Mental Health Counseling",
                "description": "Individual and group therapy for youth ages 12–24. Trauma-informed, culturally affirming approach.",
                "contact": "(555) 600-1000 | sunrisebh.org",
                "eligibility": "Ages 12–24; sliding scale fees; Medicaid accepted",
            },
            {
                "name": "Crisis Line & Mobile Support",
                "type": "Crisis Intervention",
                "description": "24/7 crisis line with mobile outreach team for youth experiencing mental health emergencies.",
                "contact": "Call or text: 988 | youthcrisisline.org",
                "eligibility": "Any youth in crisis",
            },
        ],
        "mental_health": [
            {
                "name": "Youth Wellness Center",
                "type": "Mental Health Services",
                "description": "Comprehensive mental health assessments, psychiatry, medication management, and therapy.",
                "contact": "(555) 600-3300 | youthwellnesscenter.org",
                "eligibility": "Ages 12–24; insurance not required",
            },
        ],
        "substance_support": [
            {
                "name": "Youth Recovery & Wellness Program",
                "type": "Substance Use Support",
                "description": "Peer support, group sessions, and individualized recovery planning for youth.",
                "contact": "(555) 600-5500 | youthrecovery.org",
                "eligibility": "Ages 13–24",
            },
        ],
        "id_support": [
            {
                "name": "ID & Document Assistance Program",
                "type": "ID / Documentation",
                "description": "Help obtaining state ID, birth certificate, Social Security card, and other vital documents. Free of charge.",
                "contact": "(555) 500-7700 | youthidhelp.org",
                "eligibility": "Youth experiencing homelessness or in foster care",
            },
        ],
        "education": [
            {
                "name": "GED & Alternative Education Program",
                "type": "Education",
                "description": "Free GED preparation classes, tutoring, and testing. Flexible scheduling for working youth.",
                "contact": "(555) 400-2200 | learnforward.edu",
                "eligibility": "Youth ages 16–24 not currently enrolled in traditional school",
            },
            {
                "name": "School Liaison & Re-Engagement Program",
                "type": "Education",
                "description": "Supports youth in re-enrolling in school, navigating credits, and addressing barriers to attendance.",
                "contact": "(555) 400-3300 | schoolliaison.org",
                "eligibility": "Youth experiencing school disruption",
            },
        ],
        "employment": [
            {
                "name": "YouthWorks Job Training & Placement",
                "type": "Employment",
                "description": "Paid internships, job readiness workshops, resume help, interview prep, and job placement assistance.",
                "contact": "(555) 300-4400 | youthworks.org",
                "eligibility": "Ages 16–24",
            },
            {
                "name": "Vocational Training Center",
                "type": "Vocational Training",
                "description": "Free vocational training in healthcare, construction, cosmetology, and technology.",
                "contact": "(555) 300-5500 | voctraining.org",
                "eligibility": "Ages 16–24; no prior experience needed",
            },
        ],
        "legal": [
            {
                "name": "Youth Legal Aid Clinic",
                "type": "Legal Aid",
                "description": "Free legal representation and advice for youth involved in juvenile justice, civil matters, or court proceedings.",
                "contact": "(555) 200-8800 | youthlegalaid.org",
                "eligibility": "Youth ages 10–24 with open legal matters",
            },
            {
                "name": "Juvenile Diversion & Restorative Justice Program",
                "type": "Diversion",
                "description": "Alternative to formal court processing; restorative justice circles, community service, and skill-building.",
                "contact": "(555) 200-9900 | restorativejustice.org",
                "eligibility": "Youth ages 10–17 with first-time or minor offenses",
            },
        ],
        "mentorship": [
            {
                "name": "Big Brothers Big Sisters – Youth Program",
                "type": "Mentorship",
                "description": "One-on-one mentoring relationships with trained adult volunteers. Community and school-based options.",
                "contact": "(555) 100-3300 | bbbs.org",
                "eligibility": "Youth ages 6–18",
            },
        ],
        "peer_support": [
            {
                "name": "Youth Peer Support Network",
                "type": "Peer Support",
                "description": "Peer-led support groups facilitated by trained young adults with lived experience in the system.",
                "contact": "(555) 100-4400 | youthpeernetwork.org",
                "eligibility": "Ages 14–24",
            },
        ],
        "safety": [
            {
                "name": "Safe Harbor – Domestic Violence & Youth Safety",
                "type": "Safety / DV Services",
                "description": "Confidential shelter, safety planning, and advocacy for youth fleeing violence or unsafe home situations.",
                "contact": "(555) 900-0000 (24/7) | safeharboryouth.org",
                "eligibility": "Any youth in unsafe situation",
            },
        ],
        "trauma_informed": [
            {
                "name": "Trauma Recovery Center – Youth Services",
                "type": "Trauma Services",
                "description": "Specialized trauma-informed therapy, group processing, and somatic support for youth survivors.",
                "contact": "(555) 600-7700 | traumarecoverycenter.org",
                "eligibility": "Youth ages 12–24 with trauma history",
            },
        ],
        "crisis": [
            {
                "name": "988 Suicide & Crisis Lifeline",
                "type": "Crisis Line",
                "description": "Free, confidential crisis support available 24/7. Call or text 988.",
                "contact": "Call or text: 988",
                "eligibility": "Anyone in crisis",
            },
            {
                "name": "Local Crisis Stabilization Unit",
                "type": "Crisis Stabilization",
                "description": "Short-term (up to 7 days) crisis stabilization for youth experiencing mental health emergencies.",
                "contact": "(555) 999-1111 | crisisstabilization.org",
                "eligibility": "Youth ages 12–24 in acute psychiatric crisis",
            },
        ],
    }
