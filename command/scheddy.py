import json


# when called return a table formatted version of the Blood Bowl schedule for the current week
async def handle(ctx, bb_db, league_name="ozlan_bloodbowl_redux"):
    all_leagues = bb_db["leagues"]
    league = bb_db[league_name]

    round_query = { "name": league_name }
    current_round = all_leagues.find_one(round_query)

    print(current_round)
    current_round_no = current_round["current_round"]

    round_schedule = league.find_one({ "_id": current_round_no })

    await ctx.send(json.dumps(round_schedule))
