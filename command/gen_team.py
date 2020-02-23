
from data.Team import Team
from function.gen_skilled_player import gen_skilled_player
from function.gen_skills import gen_skill_pool


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
