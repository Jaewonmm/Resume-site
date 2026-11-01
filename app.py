import os
from flask import Flask, render_template

app = Flask(__name__)

resume_data = {
    # ---- Identity ----
    "name": "Mason",
    "full_name": "Mason Jaewon Matute",
    "title": "Aspiring Technologist",
    "role_line": "High School Senior — CS, Cybersecurity, Linux",
    "tagline_lead": "Learning",
    "tagline_italic": "Cybersecurity,",
    "tagline_rest": "Building Real Things.",
    "summary": "High school senior in Marietta, GA studying computer science and cybersecurity. Looking for a paid, computer-related internship or job where I can learn.",

    # ---- Contact ----
    "email": "mason.matute@gmail.com",
    "linkedin": None,
    "github": "github.com/Jaewonmm",
    "researchgate": None,

    # ---- Home: Focus Areas (Bento Grid) ----
    "focus_areas": [
        {
            "title": "Computer Science",
            "icon": "code",
            "description": "Python and basic JavaScript, AP CSP and AP CSA coursework, and projects like this website.",
            "feature": False,
        },
        {
            "title": "Cybersecurity",
            "icon": "shield",
            "description": "Studying cybersecurity through TryHackMe courses and working toward entry-level certifications.",
            "feature": True,
        },
        {
            "title": "Linux",
            "icon": "terminal",
            "description": "Set up and customized my own Hyprland desktop on Linux.",
            "feature": False,
        },
        {
            "title": "Hands-On Building",
            "icon": "build",
            "description": "200+ volunteer hours in construction and woodworking, including decks, fences, and home repairs.",
            "feature": False,
        },
    ],

    # ---- CV: Experience Timeline ----
    "experience": [
        {
            "company": None,
            "role": "Construction & Woodworking Volunteer",
            "duration": "200+ Hours",
            "location": "Georgia",
            "bullets": [
                "Built decks and fences and learned to use power tools safely.",
                "Fixed toilets and identified leaks in house crawlspaces.",
                "Completed more than 200 volunteer hours, mostly construction and woodworking.",
            ],
            "photo": None,
        },
        {
            "company": "Pope High School Marching Band",
            "role": "Member & Soloist",
            "duration": "4 Years",
            "location": "Marietta, GA",
            "bullets": [
                "Took on soloist roles in a band ranked among the best in the region.",
                "Won multiple Grand Championships, including Conquest at Allatoona.",
                "Placed 5th as a Regional Finalist at Bands of America (BOA).",
            ],
            "photo": None,
        },
        {
            "company": None,
            "role": "Church Service Volunteer",
            "duration": "Ongoing",
            "location": "Georgia",
            "bullets": [
                "Heavily involved in church service and community activities.",
            ],
            "photo": None,
        },
    ],

    # ---- CV: Academic Foundation ----
    "education": [
        {
            "label": "Current Studies",
            "school": "Pope High School",
            "degree": "High School Diploma, Expected 2027",
            "description": "12th grade. 3.5 weighted GPA. AP coursework includes Precalculus, Business with Personal Finance, Computer Science Principles, and Computer Science A.",
            "year": "2027",
            "gpa": "3.5 weighted",
            "photo": None,
        },
        {
            "label": "Dual Enrollment",
            "school": "Kennesaw State University",
            "degree": "College Courses",
            "description": "Enrolled in college classes at KSU through dual enrollment, taken online alongside high school.",
            "year": "Current",
            "gpa": None,
            "photo": None,
        },
    ],

    # ---- Achievements badges (no certifications yet) ----
    "certifications": [
        {"label": "Achievement", "name": "BOA Regional Finalist, 5th Place", "icon": "trophy", "feature": True},
        {"label": "Achievement", "name": "Multiple-Time Band Grand Champion", "icon": "badge", "feature": False},
        {"label": "Service", "name": "200+ Volunteer Hours", "icon": "service", "feature": False},
    ],

    # ---- Skills / Competency Grid (template expects exactly 4) ----
    "competencies": [
        {
            "title": "Computer Science",
            "icon": "code",
            "description": "Python and basic JavaScript, built through AP Computer Science coursework and personal projects.",
            "tags": ["Python", "JavaScript", "Flask", "Git"],
            "feature": False,
        },
        {
            "title": "Cybersecurity",
            "icon": "shield",
            "description": "Learning through TryHackMe courses and working toward entry-level certifications.",
            "tags": [],
            "feature": True,
        },
        {
            "title": "Linux & Networking",
            "icon": "terminal",
            "description": "Comfortable with Linux, with surface-level networking and computer hardware knowledge.",
            "tags": [],
            "feature": False,
        },
        {
            "title": "Hands-On Building",
            "icon": "build",
            "description": "Woodworking, power tools, and construction, plus communication and leadership skills from band and volunteer work.",
            "tags": [],
            "feature": False,
        },
    ],

    # ---- Legacy skill tags (not currently displayed) ----
    "skills": {
        "Technical": ["Python", "JavaScript (basic)", "Linux", "Git", "AI automation"],
        "Hands-On": ["Woodworking", "Power tools", "Construction"],
        "Personal": ["Communication", "Leadership", "Flexible learner"],
    },
    "skills_photo": None,

    # ---- Projects ----
    "projects": [
        {
            "name": "This Resume Website",
            "category": "Computer Science",
            "description": "A multi-page personal website built with Python and Flask and deployed live on Render.",
            "tech": ["Python", "Flask", "HTML/CSS", "Render"],
            "link": "https://github.com/Jaewonmm/Resume-site",
            "photo": None,
        },
        {
            "name": "Custom Linux Desktop",
            "category": "Linux",
            "description": "Installed Linux and built a customized Hyprland desktop environment from scratch.",
            "tech": ["Linux", "Hyprland"],
            "link": None,
            "photo": None,
        },
        {
            "name": "Home Construction & Repair",
            "category": "Construction",
            "description": "Built decks and fences, fixed toilets, and identified leaks in house crawlspaces.",
            "tech": ["Woodworking", "Power Tools", "Construction"],
            "link": None,
            "photo": None,
        },
    ],

    # ---- Contact / Inquiry copy ----
    "contact_headline": "Looking for a paid, computer-related internship or job.",
    "contact_kicker": "Open to Work",
}

# The Command AI navigator uses keyword-to-route mapping.
# Rendered into the template so the JS can read intents without hardcoding.
command_intents = {
    "home":        {"route": "/",           "keywords": ["home", "start", "top"]},
    "experience":  {"route": "/experience", "keywords": ["experience", "work", "job", "volunteer", "band", "church", "cv"]},
    "education":   {"route": "/education",  "keywords": ["education", "school", "academic", "academics", "diploma", "pope", "ksu", "kennesaw", "gpa", "classes"]},
    "skills":      {"route": "/skills",     "keywords": ["skill", "skills", "stack", "tech", "tools", "linux", "python"]},
    "projects":    {"route": "/projects",   "keywords": ["project", "projects", "portfolio", "showcase", "github", "resume"]},
    "contact":     {"route": "/contact",    "keywords": ["contact", "email", "reach", "message", "hire"]},
    "awards":      {"route": "/experience", "keywords": ["award", "awards", "achievement", "achievements", "grand champion", "boa", "bands of america"]},
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
