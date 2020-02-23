from random import sample


async def handle(ctx, team_pack, expansion):
    teams = sample(make_teams(team_pack, expansion), 3)
    await ctx.send(teams)


async def handle_xtr(ctx, league_type, team_pack, expansion):
    teams = sample(make_teams(team_pack, expansion, league_type), 3)
    await ctx.send(teams)


def make_teams(team_pack, expansion, league_type):
    teams_lst = [
        'Bretonnia',
        'Chaos',
        'Dark Elves',
        'Dwarves',
        'High Elves',
        'Humans',
        'Orcs',
        'Skaven',
    ]

    team_pack_lst = [
        'Chaos Dwarves',
        'Khemri',
        'Lizardmen',
        'Necromantic',
        'Norse',
        'Nurgle',
        'Undead',
        'Wood Elves'
    ]

    expansion_teams_lst = [
        'Amazons',
        'Elven Union',
        'Goblins',
        'Halflings',
        'Kislev Circus',
        'Ogres',
        'Underworld Denizens',
        'Vampires'
    ]

    # need to error handle if league_specials == 'Invalid'
    league_specials = league_switch(league_type)

    if team_pack:
        # this needs a better solution
        if league_type == 'randy_linemen':
            teams_lst += league_specials
        teams_lst += team_pack_lst
    if expansion:
        teams_lst += expansion_teams_lst

    return teams_lst


def league_switch(league_type):
    switch = {
        'standard': [],
        'randy_linemen': [
            'Undead (Zombies)'
        ]
    }
    return switch.get(league_type, 'Invalid League Type')


