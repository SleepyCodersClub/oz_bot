async def handle(ctx, league_name, bb_db, set_round):
    collection = bb_db["leagues"]
    query = { "name": league_name }
    update = { "$set": { "current_round" : set_round } }

    collection.update_one(query, update)

    print(collection.find_one(query))

    await ctx.send(league_name + " has been set to round " + str(set_round))
