async def handle(ctx, coach_name, bb_db):
    # initialise the database collection for the coach profiles

    # get the discord user ID from ctx - look in __main.py__ at the old_chris function and the api documentation of how this works

    # research how to create an object that we can store in mongo DB
    # this might mean making a Class (Coach) - look at the 11-lineman branch, or master if it has been merged for an example of this
    # with Team and Player.

    # should look like this:
    # {
    #   _id: 0,   <- this is auto-generated by mongo if you dont specify it so dont worry about including it
    #   discord_user: <discordID>,
    #   coach_name: <coach_name>
    # }

    # once you have it in a format that can be saved to the database, add it to the collction on the db.
    # look in the pymongo documentation at collection.insert()
    # ask me for help if you are not sure.


    # This just send the message to the channel in which the command was invoked - we want it to PM confirmation to the caller
    # again look at the 11 lineman branch for how to get the bot to reply via pm
    await ctx.send('REGISTRATION SUCCESSFUL')
