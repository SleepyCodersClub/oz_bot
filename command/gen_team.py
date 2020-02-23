from random import choice
from random import randint

from data.Player import Player
from data.Team import Team


async def handle(ctx, race, bb_db):
    team_profile = bb_db['teams'].find_one({'team': race}, {'_id': 0, 'team': 0}).get('profile')
    skills = bb_db['skills']

    team = gen_team(team_profile, skills)
    output_string = ''

    for player in team.players:
        player_dict = player.__dict__
        output_string += f'Player: {team.race} {team.unit}. Skills: {player_dict["skills"]} \n'

    await ctx.author.send(output_string)


def gen_team(team_profile, skills_col):
    roster = []

    while len(roster) < 11:
        roster.append(gen_skilled_player(team_profile, gen_skill_pool(team_profile, skills_col)))

    return Team(team_profile.get('name'), team_profile.get('lineman'), roster, team_profile.get('cost'))


def gen_skilled_player(team_profile, skill_pool):
    print(skill_pool)
    skills = []
    starting_skills = team_profile.get('starting_skills')
    print(starting_skills)

    while len(skills) < 3:
        skill = select_skills(skill_pool)

        if skill not in skills and skill not in starting_skills:
            skills.append(skill)
    print(skills)
    return Player(skills)


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

    return result


def select_skills(skill_pool):
    return choice(skill_pool)
