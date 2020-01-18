# when called return a table formatted version of the Blood Bowl schedule for the current week
async def handle(ctx, league_name, bb_db):
    all_leagues = bb_db["leagues"]
    league = bb_db[league_name]

    round_query = { "name": league_name }
    current_round = all_leagues.find_one(round_query)

    print(current_round)
    current_round_no = current_round["current_round"]

    round_schedule = league.find_one({ "_id": current_round_no })

    await ctx.send(round_schedule)





# def printTable(myDict, colList=None):
#    if not colList:
#        colList = list(myDict[0].keys() if myDict else [])
#    myList = [colList] # 1st row = header
#    for item in myDict:
#        myList.append([str(item[col] or '') for col in colList])
#    #maximun size of the col for each element
#    colSize = [max(map(len,col)) for col in zip(*myList)]
#    #insert seperating line before every line, and extra one for ending.
#    for i in  range(0, len(myList)+1)[::-1]:
#         myList.insert(i, ['-' * i for i in colSize])
#    #two format for each content line and each seperating line
#    formatStr = ' | '.join(["{{:<{}}}".format(i) for i in colSize])
#    formatSep = '-+-'.join(["{{:<{}}}".format(i) for i in colSize])
#    for item in myList:
#        if item[0][0] == '-':
#            print(formatSep.format(*item))
#        else:
#            print(formatStr.format(*item))