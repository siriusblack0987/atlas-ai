from backend.knowledge.skill_priority import SKILL_PRIORITY


def learning_priority(missing_skills):

    roadmap = []

    for skill in missing_skills:

        info = SKILL_PRIORITY.get(
            skill,
            {
                "priority": "MEDIUM",
                "reason": "Recommended skill."
            }
        )

        roadmap.append({

            "skill": skill,

            "priority": info["priority"],

            "reason": info["reason"]

        })

    order = {

        "HIGH": 0,

        "MEDIUM": 1,

        "LOW": 2

    }

    roadmap.sort(
        key=lambda x: order[x["priority"]]
    )

    return roadmap