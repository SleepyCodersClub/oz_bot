from math import floor
from random import choice
from random import randint

from data.Player import Player
from data.Team import Team


async def handle(ctx, race, bb_db):
    team_profile = bb_db['teams'].find_one({'team': race}, {'_id': 0, 'team': 0})
    # ToDo: get the skills - this doesnt work
    skills = bb_db['skills']

    rerolls = calculate_rerolls(team_profile.get('rerolls'), calculate_player_tv(team_profile.get('cost')))

    team = gen_team(team_profile, skills, rerolls)

    ctx.author.send(team)


def gen_team(team_profile, skills_col, rerolls):
    roster = []

    while len(roster) < 11:
        roster += gen_skilled_player(team_profile, gen_skill_pool(team_profile, skills_col))

    tv = calculate_tv(calculate_tv(team_profile.get('cost')), calculate_reroll_tv(rerolls, team_profile.get('rerolls')))

    return Team(roster, rerolls, apothecary(tv))


def gen_skilled_player(team_profile, skill_pool):
    skills = []

    while len(skills) < 3:
        skill = select_skills(skill_pool)

        if skill not in skills and skill not in team_profile.get('starting_skills'):
            skills += skill

    return Player(skills)


def gen_skill_pool(team_profile, skills_col):
    if len(set(roll_skills())) == 1:
        return make_doubles_skills(team_profile, skills_col)
    else:
        return make_skills(team_profile, skills_col)


def make_skills(team_profile, skills_col):
    skills = []
    for category in team_profile.get('skills'):
        skills += skills_col.get(category)
    return skills


def make_doubles_skills(team_profile, skills_col):
    skills = []
    for category in team_profile.get('doubles'):
        skills += skills_col.get(category)
    return skills + make_skills(team_profile, skills_col)


def roll_skills():
    result = []

    for i in range(2):
        result += randint(1, 6)

    return result


def select_skills(skill_pool):
    return choice(skill_pool)


def calculate_player_tv(player_value):
    return player_value * 11 / 1000


def calculate_reroll_tv(rerolls, reroll_cost):
    return rerolls * reroll_cost / 1000


def calculate_tv(player_tv, reroll_tv):
    return player_tv + reroll_tv


# max 8
def calculate_rerolls(cost, tv):
    fund = 1000 - tv
    rerolls = floor(fund / cost)
    if rerolls > 8:
        return 8
    else:
        return rerolls


def apothecary(tv):
    if tv <= 950:
        return True
    else:
        return False
