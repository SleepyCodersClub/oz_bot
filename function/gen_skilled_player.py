from random import choice

from data.Player import Player

from function.gen_skills import gen_skill_pool


def gen_skilled_player(team_profile, skills_col):
    skills = []
    starting_skills = team_profile.get('starting_skills')

    while len(skills) < 3:
        skill_pool = gen_skill_pool(team_profile, skills_col)

        add_skill(skills, starting_skills, skill_pool)

    # DEBUG
    print(skills)
    return Player(skills)


def select_skills(skill_pool):
    return choice(skill_pool)


def add_skill(skills, starting_skills, skill_pool):
    skill = select_skills(skill_pool)

    if skill not in skills and skill not in starting_skills:
        skills.append(skill)
    else:
        add_skill(skills, starting_skills, skill_pool)
