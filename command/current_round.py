async def handle(ctx, league_name, bb_db):
    collection = bb_db["leagues"]
    query = { "name": league_name }

    current_round = collection.find_one(query)

    await ctx.send(league_name + " is currently on round " + str(current_round["current_round"]))
