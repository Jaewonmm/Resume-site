import os
from flask import Flask, render_template

#need to refresh site
app = Flask(__name__)

resume_data = {
    "name": "Mason J Matute",
    "title": "Student",
    "email": "mason.matute@gmail.com",
    "instagram": "www.instagram.com/masonjarm/",
    "github": "github.com/Jaewonmm",
    "summary": "A highschool student with a passion to learn the field of Computer Science and Cybersecurity",
    "experience": [
        {
            "company": "Whitesville St. Anns Summer",
            "role": "Service",
            "duration": "Jan 2022 – Present",
            "location": "Whitesville North Carolina",
            "bullets": [
                "Students and Adults from churches gather to provide aid to the people of Whitesville",
                "Supervised students rebuild decks, repaint houses, fix plumbing, etc",
                "Although work focused, religious activities like church take place with Whitesville's inhabitants"
                "The summer program brings students alike to Whitesville for a week, where they stay at the local school while they assist the citizens every day"
                "The Whitesville Mission Trip provides around 56 total service hours but requires 168 hours of the volunteers time"
            ]
        },
        {
            "company": "Previous Company",
            "role": "Junior Developer",
            "duration": "Jun 2020 – Dec 2021",
            "location": "Remote",
            "bullets": [
                "Developed internal tooling used by 50+ employees",
                "Improved deployment pipeline reducing release time by 40%"
            ]
        }
    ],
    "education": [
        {
            "school": "Allen C Pope Highschool",
            "degree": "Still in school",
            "year": "2026 - 2027",
            "gpa": "3.4"
        }
    ],
    "skills": {
        "Languages": ["Python", "JavaScript", "HTML/CSS", "SQL"],
        "Frameworks": ["Flask", "React", "Node.js"],
        "Tools": ["Git", "Docker", "VS Code", "PostgreSQL"]
    },
    "projects": [
        {
            "name": "Project One",
            "description": "A full-stack web app that does something amazing.",
            "tech": ["Python", "Flask", "PostgreSQL"],
            "link": "https://github.com/yourusername/project-one"
        },
        {
            "name": "Project Two",
            "description": "A mobile-friendly dashboard with real-time data.",
            "tech": ["React", "Node.js", "MongoDB"],
            "link": "https://github.com/yourusername/project-two"
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

#to run program use: python app.py
#to save programs use: git add . (then) git commit -m "describe what you changed" (then) git push