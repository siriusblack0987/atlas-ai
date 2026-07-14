from backend.knowledge.career_paths import CAREER_PATHS


def analyze_gap(goal: str, current_skills: list):

    goal = goal.upper()

    career = CAREER_PATHS.get(goal)

    if career is None:
        return {
            "error": f"No career path found for '{goal}'."
        }

    required = career["required_skills"]

    matched = []
    missing = []

    earned_points = 0
    total_points = sum(required.values())

    for skill, weight in required.items():

        if skill in current_skills:

            matched.append(skill)
            earned_points += weight

        else:

            missing.append(skill)

    readiness = round(
        earned_points / total_points * 100,
        2
    )

    return {

        "career": goal,

        "readiness": readiness,

        "matched_skills": matched,

        "missing_skills": missing,

        "earned_points": earned_points,

        "total_points": total_points

    }