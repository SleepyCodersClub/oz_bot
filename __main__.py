import pymongo
from discord.ext import commands

import command
import data.leagues as leagues
import function.old_chris as old_chris
import settings


# Bot initialisation
bot = commands.Bot(command_prefix='^')

# Database connection
mongo_client = pymongo.MongoClient("mongodb://localhost:27017")
bb_db = mongo_client["bb_db"]

leagues_col = bb_db["leagues"]
if leagues_col.count_documents({}) == 0:
    leagues_col.insert_many(leagues.leagues)
else:
    print(f"Leagues already present.")


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_message(message):
    if message.author.id == int(settings.CHRIS_ID):
        await old_chris.handle(message)
        print(f'Attempted to react to message')
    await bot.process_commands(message)


@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')


@bot.command()
async def bb_teams(ctx, team_pack: bool = True, expansion: bool = True):
    print(f'bbteams executed')
    if team_pack is not True:
        team_pack = False
    if expansion is not True:
        expansion = False
    await command.bb_teams.handle(ctx, team_pack, expansion)


@bot.command()
async def current_round(ctx, league_name):
    await command.current_round.handle(ctx, league_name, bb_db)


@bot.command()
@commands.has_any_role(settings.SERVER_ADMIN, settings.BLOOD_BOWL_ADMIN)
async def load_schedule(ctx, league_name):
    await command.load_schedule.handle(ctx, league_name, bb_db)


# OZ THIS IS THE COMMAND YOU ARE WORKING ON
@bot.command()
# ctx is the bot context - get the user id from this - google discord.py api.
# coach_name is obviously the user supplied coach name in game.
# bb_db is the link through to the database - it just makes it easier than initialising it in every command file.
async def register_coach(ctx, coach_name):
    await command.register_coach.handle(ctx, coach_name, bb_db)


@bot.command()
@commands.has_any_role(settings.SERVER_ADMIN, settings.BLOOD_BOWL_ADMIN)
async def roll_league(ctx, league_name, advance=1):
    await command.roll_league.handle(ctx, league_name, bb_db, advance)


@bot.command()
@commands.has_any_role(settings.SERVER_ADMIN, settings.BLOOD_BOWL_ADMIN)
async def roll_league_back(ctx, league_name, reverse=1):
    await command.roll_league_back.handle(ctx, league_name, bb_db, reverse)


@bot.command()
async def scheddy(ctx, league_name="ozlan_bloodbowl_redux"):
    await command.scheddy.handle(ctx, bb_db, league_name)


@bot.command()
async def scheddy_plus(ctx, week: int, league_name="ozlan_bloodbowl_redux"):
    await command.scheddy_plus.handle(ctx, bb_db, week, league_name)


@bot.command()
@commands.has_any_role(settings.SERVER_ADMIN, settings.BLOOD_BOWL_ADMIN)
async def set_round(ctx, league_name, set_rnd: int):
    await command.set_round.handle(ctx, league_name, bb_db, set_rnd)


bot.run(settings.BOT_TOKEN)
