import os
from flask import Flask, render_template

app = Flask(__name__)

resume_data = {
    # ---- Identity ----
    "name": "Mason",
    "full_name": "Mason Maute",
    "title": "Emerging Technologist & Researcher",
    "role_line": "High School Scholar — CS, Cybersecurity, AI",
    "tagline_lead": "Securing",
    "tagline_italic": "Intelligence",
    "tagline_rest": "Through Computational Ethics.",
    "summary": "High School Scholar focused on the intersection of Computer Science, Cybersecurity, and AI development.",

    # ---- Contact ----
    "email": "mason@example.com",
    "linkedin": "linkedin.com/in/masonmaute",
    "github": "github.com/masonmaute",
    "researchgate": "researchgate.net/profile/mason-maute",

    # ---- Home: Focus Areas (Bento Grid) ----
    "focus_areas": [
        {
            "title": "Artificial Intelligence",
            "icon": "brain",
            "description": "Developing ethical AI models and exploring deep learning architectures for predictive analytics.",
            "feature": False,
        },
        {
            "title": "Cybersecurity",
            "icon": "shield",
            "description": "Hardening digital infrastructures against emerging threats and practicing ethical penetration testing.",
            "feature": True,  # dark/filled card
        },
        {
            "title": "Systems Design",
            "icon": "terminal",
            "description": "Mastering low-level programming and optimized backend architectures.",
            "feature": False,
        },
        {
            "title": "Computational Research",
            "icon": "flask",
            "description": "Bridging the gap between theoretical computer science and practical industrial applications.",
            "feature": False,
        },
    ],

    # ---- CV: Experience Timeline ----
    "experience": [
        {
            "company": "School Robotics Club",
            "role": "Tech Lead",
            "duration": "2023 — Present",
            "location": "Atlanta, GA",
            "bullets": [
                "Lead firmware and control-system development for competition robots.",
                "Mentor 12+ underclassmen on embedded C++ and sensor integration.",
                "Architected an autonomous navigation module using PID + computer vision.",
            ],
            "photo": None,
        },
        {
            "company": "SecureLink (Summer Program)",
            "role": "Cybersecurity Intern",
            "duration": "Summer 2023",
            "location": "Remote",
            "bullets": [
                "Audited internal web services for OWASP Top 10 vulnerabilities.",
                "Built a Python-based log anomaly detector flagging brute-force patterns.",
                "Presented findings and remediation playbook to the security team.",
            ],
            "photo": None,
        },
    ],

    # ---- CV: Academic Foundation ----
    "education": [
        {
            "label": "Current Studies",
            "school": "Central High School",
            "degree": "High School Diploma",
            "description": "Senior year student with a focus on Advanced Placement Computer Science, Physics, and Calculus. Maintaining a 4.0 GPA with a focus on STEM excellence.",
            "year": "2026",
            "gpa": "4.0",
            "photo": None,
        },
        {
            "label": "Summer Enrichment",
            "school": "Stanford Pre-College",
            "degree": "Pre-College Engineering",
            "description": "Intensive 6-week residential program focusing on embedded systems and collaborative software development.",
            "year": "2024",
            "gpa": None,
            "photo": None,
        },
    ],

    # ---- CV: Certifications / Awards badges ----
    "certifications": [
        {"label": "Certification", "name": "CompTIA Security+", "icon": "badge", "feature": True},
        {"label": "Proficiency",  "name": "Python & Java (AP)", "icon": "code",  "feature": False},
        {"label": "Award",         "name": "National Merit Scholar", "icon": "trophy", "feature": False},
    ],

    # ---- Skills / Competency Grid ----
    "competencies": [
        {
            "title": "Machine Learning",
            "icon": "brain",
            "description": "Developing neural architectures and predictive models that transform raw data into actionable intelligence.",
            "tags": ["Python", "C++"],
            "feature": False,
        },
        {
            "title": "Network Security",
            "icon": "shield",
            "description": "Hardening infrastructure and designing zero-trust frameworks for mission-critical applications.",
            "tags": [],
            "feature": True,
        },
        {
            "title": "Software Engineering",
            "icon": "terminal",
            "description": "Building scalable backends and efficient algorithms using Python, Java, and C++.",
            "tags": [],
            "feature": False,
        },
        {
            "title": "Cloud Infrastructure",
            "icon": "cloud",
            "description": "Orchestrating containerized deployments and serverless architectures with high availability.",
            "tags": [],
            "feature": False,
        },
    ],

    # ---- Legacy skill tags (kept for flexibility) ----
    "skills": {
        "Languages": ["Python", "Java", "C++", "JavaScript", "SQL"],
        "Frameworks": ["Flask", "PyTorch", "React"],
        "Security": ["Burp Suite", "Wireshark", "Nmap", "Metasploit"],
        "Tools": ["Git", "Docker", "Linux", "AWS"],
    },
    "skills_photo": None,

    # ---- Projects ----
    "projects": [
        {
            "name": "Autonomous Agent Framework",
            "category": "Artificial Intelligence",
            "description": "A modular framework for building goal-directed AI agents with tool-use, planning, and safety guardrails.",
            "tech": ["Python", "PyTorch", "LangGraph"],
            "link": "https://github.com/masonmaute/autonomous-agents",
            "photo": None,
        },
        {
            "name": "Real-time Vulnerability Scanner",
            "category": "Cybersecurity",
            "description": "A network scanner that correlates live traffic with CVE feeds to flag exploitable services before attackers can.",
            "tech": ["Go", "Redis", "Nmap"],
            "link": "https://github.com/masonmaute/vuln-scanner",
            "photo": None,
        },
        {
            "name": "Distributed Database Engine",
            "category": "Computer Science",
            "description": "A Raft-backed key-value store exploring consensus, sharding, and fault tolerance in distributed systems.",
            "tech": ["Rust", "Raft", "gRPC"],
            "link": "https://github.com/masonmaute/dist-db",
            "photo": None,
        },
    ],

    # ---- Contact / Inquiry copy ----
    "contact_headline": "Let's create something secure.",
    "contact_kicker": "Inquiries",
}

# The Command AI navigator uses keyword-to-route mapping.
# Rendered into the template so the JS can read intents without hardcoding.
command_intents = {
    "home":        {"route": "/",           "keywords": ["home", "start", "top"]},
    "experience":  {"route": "/experience", "keywords": ["experience", "work", "job", "robotics", "intern", "cv"]},
    "education":   {"route": "/education",  "keywords": ["education", "school", "academic", "academics", "diploma", "pre-college", "stanford"]},
    "skills":      {"route": "/skills",     "keywords": ["skill", "skills", "stack", "research", "tech", "tools", "competency"]},
    "projects":    {"route": "/projects",   "keywords": ["project", "projects", "portfolio", "work", "showcase", "github"]},
    "contact":     {"route": "/contact",    "keywords": ["contact", "email", "reach", "message", "hire"]},
    "awards":      {"route": "/experience", "keywords": ["award", "awards", "certification", "certifications", "merit", "security+"]},
}


@app.context_processor
def inject_globals():
    return {"command_intents": command_intents}


@app.route("/")
def home():
    return render_template("index.html", **resume_data)

@app.route("/experience")
def experience():
    return render_template("experience.html", **resume_data)

@app.route("/education")
def education():
    return render_template("education.html", **resume_data)

@app.route("/skills")
def skills():
    return render_template("skills.html", **resume_data)

@app.route("/projects")
def projects():
    return render_template("projects.html", **resume_data)

@app.route("/contact")
def contact():
    return render_template("contact.html", **resume_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
