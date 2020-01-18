from random import sample


async def handle(ctx, team_pack, expansion):
    teams = sample(make_teams(team_pack, expansion), 3)
    await ctx.send(teams)


def make_teams(team_pack, expansion):
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
        'Lizard Men',
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

    if team_pack:
        if expansion:
            return teams_lst + team_pack_lst + expansion_teams_lst
        else:
            return teams_lst + team_pack_lst
    else:
        if expansion:
            return teams_lst + expansion_teams_lst
        else:
            return teams_lst



