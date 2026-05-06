import os
from flask import Flask, render_template

app = Flask(__name__)

resume_data = {
    "name": "Your Name",
    "title": "Software Developer",
    "email": "you@email.com",
    "linkedin": "linkedin.com/in/yourprofile",
    "github": "github.com/yourusername",
    "summary": "A passionate developer with experience in building clean, modern tech solutions.",

    "experience": [
        {
            "company": "Company Name",
            "role": "Job Title",
            "duration": "Jan 2022 – Present",
            "location": "Atlanta, GA",
            "bullets": [
                "Built X feature that improved Y by Z%",
                "Led a team of 3 engineers",
                "Shipped 10+ features to production"
            ],
            # Put your image filename here e.g. "company1.jpg"
            # Add the image to your static/images/ folder
            # Set to None if you have no photo for this job
            "photo": None
        },
        {
            "company": "Previous Company",
            "role": "Junior Developer",
            "duration": "Jun 2020 – Dec 2021",
            "location": "Remote",
            "bullets": [
                "Developed internal tooling used by 50+ employees",
                "Improved deployment pipeline reducing release time by 40%"
            ],
            "photo": None
        }
    ],

    "education": [
        {
            "school": "University Name",
            "degree": "B.S. Computer Science",
            "year": "2020",
            "gpa": "3.8",
            # A campus or graduation photo works great here
            "photo": None
        }
    ],

    # Simple skill tags — no levels!
    "skills": {
        "Languages": ["Python", "JavaScript", "HTML/CSS", "SQL"],
        "Frameworks": ["Flask", "React", "Node.js"],
        "Tools": ["Git", "Docker", "VS Code", "PostgreSQL"]
    },

    # Optional banner photo for top of skills page
    "skills_photo": None,

    "projects": [
        {
            "name": "Project One",
            "description": "A full-stack web app that does something amazing.",
            "tech": ["Python", "Flask", "PostgreSQL"],
            "link": "https://github.com/yourusername/project-one",
            # A screenshot of the project works great here
            "photo": None
        },
        {
            "name": "Project Two",
            "description": "A mobile-friendly dashboard with real-time data.",
            "tech": ["React", "Node.js", "MongoDB"],
            "link": "https://github.com/yourusername/project-two",
            "photo": None
        }
    ]
}

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