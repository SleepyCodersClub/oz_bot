from random import randint


def gen_skill_pool(team_profile, skills_col):
    if len(set(roll_skills())) == 1:
        return make_doubles_skills(team_profile, skills_col)
    else:
        return make_skills(team_profile, skills_col)


def make_skills(team_profile, skills_col):
    skills = []
    for category in team_profile.get('skills'):
        for skill in skills_col.find_one({'category': category}, {'_id': 0, 'category': 0}).get('skills'):
            skills.append(skill)
    return skills


def make_doubles_skills(team_profile, skills_col):
    skills = []
    for category in team_profile.get('doubles'):
        for skill in skills_col.find_one({'category': category}, {'_id': 0, 'category': 0}).get('skills'):
            skills.append(skill)
    return skills + make_skills(team_profile, skills_col)


# Returns a 2 item list of randomly generated integers between 1 and 6 (2d6 simulation).
def roll_skills():
    result = []

    for _ in range(2):
        result.append(randint(1, 6))

    print(result)

    return result
