# when called return a table formatted version of the Blood Bowl schedule for a requested week
async def handle(ctx, bb_db, week, league_name="ozlan_bloodbowl_redux"):
    all_leagues = bb_db["leagues"]
    league = bb_db[league_name]

    round_query = {"name": league_name}
    current_round = all_leagues.find_one(round_query)

    print(current_round)
    requested_round_no = current_round["current_round"] + week

    round_schedule = league.find_one({"_id": requested_round_no})

    output_string = ""

    for match in round_schedule["match"]:
        output_string += f'**{match["home"]}** vs **{match["away"]}** \n'

    await ctx.send(output_string)
