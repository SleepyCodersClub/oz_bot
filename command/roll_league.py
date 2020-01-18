async def handle(ctx, league_name, bb_db, advance=1):
    collection = bb_db["leagues"]
    query = { "name": league_name }

    current_round = collection.find_one(query)

    update = { "$set": { "current_round" : current_round["current_round"] + advance } }

    collection.update_one(query, update)

    print(collection.find_one(query))

    await ctx.send(league_name + " has been advanced to round " + str(current_round["current_round"] + advance))
