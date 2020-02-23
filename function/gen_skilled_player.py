from random import choice

from data.Player import Player


def gen_skilled_player(team_profile, skill_pool):
    # DEBUG - write some tests Sean, come on
    print(skill_pool)
    skills = []
    starting_skills = team_profile.get('starting_skills')
    # DEBUG
    print(starting_skills)

    while len(skills) < 3:
        skill = select_skills(skill_pool)

        if skill not in skills and skill not in starting_skills:
            skills.append(skill)
    # DEBUG
    print(skills)
    return Player(skills)


def select_skills(skill_pool):
    return choice(skill_pool)
