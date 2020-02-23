from function.gen_skilled_player import gen_skilled_player


async def handle(ctx, race, bb_db):
    team_profile = bb_db['teams'].find_one({'team': race}, {'_id': 0, 'team': 0}).get('profile')
    skills = bb_db['skills']

    player = gen_skilled_player(team_profile, skills)
    output_string = ''

    player_dict = player.__dict__
    output_string += f'Player: {team_profile.get("name")} {team_profile.get("lineman")}. Skills: {player_dict["skills"]} \n'

    await ctx.author.send(output_string)
