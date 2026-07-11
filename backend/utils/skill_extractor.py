KNOWN_SKILLS = [
    "Python",
    "C",
    "C++",
    "Java",
    "JavaScript",
    "TypeScript",
    "SQL",
    "HTML",
    "CSS",
    "React",
    "Node.js",
    "FastAPI",
    "Flask",
    "Django",
    "Git",
    "GitHub",
    "Docker",
    "Kubernetes",
    "Linux",
    "AWS",
    "Azure",
    "GCP",
    "TensorFlow",
    "PyTorch",
    "Scikit-learn",
    "Machine Learning",
    "Deep Learning",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Power BI",
    "Excel",
    "MongoDB",
    "PostgreSQL",
    "SQLite"
]


def extract_skills(text: str):

    text = text.lower()

    found_skills = []

    for skill in KNOWN_SKILLS:
        if skill.lower() in text:
            found_skills.append(skill)

    return sorted(set(found_skills))