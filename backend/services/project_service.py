from backend.knowledge.projects import PROJECT_DATABASE


def recommend_projects(missing_skills):

    recommendations = []
    seen = set()

    for skill in missing_skills:

        projects = PROJECT_DATABASE.get(skill, [])

        for project in projects:

            title = project["title"]

            if title in seen:
                continue

            score = len(
                set(project["skills"]) &
                set(missing_skills)
            )

            project_copy = project.copy()
            project_copy["score"] = score

            recommendations.append(project_copy)

            seen.add(title)

    recommendations.sort(
        key=lambda project: project["score"],
        reverse=True
    )

    return recommendations