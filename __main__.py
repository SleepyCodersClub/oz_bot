import pymongo
from discord.ext import commands

import command
import data.leagues as leagues
import data.skills as skills
import data.teams as teams
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

teams_col = bb_db["teams"]
if teams_col.count_documents({}) == 0:
    teams_col.insert_many(teams.teams)
else:
    print(f"Teams already present.")

skills_col = bb_db["skills"]
if skills_col.count_documents({}) == 0:
    skills_col.insert_many(skills.skills)
else:
    print(f"Skills already present.")


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
async def bb_teams(ctx, league_type="standard", team_pack: bool = True, expansion: bool = True):
    if team_pack is not True:
        team_pack = False
    if expansion is not True:
        expansion = False
    if league_type is not "standard":
        await command.bb_teams.handle(ctx, league_type, team_pack, expansion)
    else:
        await command.bb_teams.handle(ctx, team_pack, expansion)


@bot.command()
async def current_round(ctx, league_name):
    await command.current_round.handle(ctx, league_name, bb_db)


@bot.command()
@commands.has_any_role(settings.SERVER_ADMIN, settings.BLOOD_BOWL_ADMIN)
async def load_schedule(ctx, league_name):
    await command.load_schedule.handle(ctx, league_name, bb_db)


@bot.command()
async def gen_team(ctx, race):
    await command.gen_team.handle(ctx, race, bb_db)


@bot.command()
async def gen_player(ctx, race):
    await command.gen_player.handle(ctx, race, bb_db)


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
