import importlib


async def handle(ctx, league_name, bb_db):
    collection = bb_db[league_name]

    if collection.count_documents({}) == 0:
        schedule = importlib.import_module("data.schedules." + league_name, package=None)
        collection.insert_many(schedule.schedule)

        await ctx.send('Schedule for league: ' + league_name + ' loaded.')
    else:
        await ctx.send('Schedule already present.')
