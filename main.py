import discord
import os

from template import MsgTemplate
from services import BotMsgsServices, RolesServices, PartiesServices

# First init
client = discord.Client()

# Events
@client.event
async def on_ready():
    print("Bot initialised.")

@client.event
async def on_message(message):

    # Deflect
    if message.author == client.user:
        return

    if message.content == "$hello":
        await message.channel.send("Hello newb.")

    # Create Party
    if message.channel.category_id == 818917723177615380:

        if message.content == "$create":
            # create party record if not exists
            partyName = message.channel.name
            partyID = PartiesServices().getParty(partyName)
            
            if partyID is None:
                partyLeader = message.author.nick or message.author.name
                partyID = PartiesServices().create(partyName, 12, '', '', partyLeader)
                teamString = await getTeam(partyName)
                botMSG = await message.channel.send(teamString)
                BotMsgsServices().create(botMSG.id, partyID)

            await message.delete()

        # Refresh
        if message.content == '$refresh':
            # update ET MSG
            await updateET(message)
            await message.delete()

        # Add role
        if message.content.startswith('$addRole'):
            characterUser = message.author.nick or message.author.name
            partyName = message.channel.name
            if characterUser == PartiesServices().getParty(partyName)['partyLeader']:
                roleName = message.content[9:]
                if roleName in [
                    'SB Champ',
                    'Devo Pally',
                    'HP 1',
                    'HP 2',
                    'HW',
                    'Snip 1',
                    'Snip 2',
                    'Snip 3',
                    'Bio',
                    'WS',
                    'LK',
                    'Prof',
                    'SN',
                    'Any 1',
                    'Any 2',
                    'Any 3',
                    'Any 4',
                    'Any 5',
                    'Any 6',
                    'Any 7',
                    'Any 8',
                    'Any 9',
                    'Any 10',
                    'Clown',
                    'Gypsy'
                ]:
                    partyName = message.channel.name
                    partyID = PartiesServices().getParty(partyName)['_id']
                    if RolesServices().list(partyID).count() < 12:
                        RolesServices().create(partyID, roleName)

                await updateET(message)
            await message.delete()

        # Join party
        if message.content.startswith('$join'):
            roleName = message.content[6:]
            username = message.author.nick or message.author.name
            partyName = message.channel.name
            partyID = PartiesServices().getParty(partyName)['_id']
            roleList = RolesServices().list(partyID)
            # check if user is in array
            for role in roleList:
                print("For checking..." + role['roleName'])
                if role['roleUsername'] == username:
                    RolesServices().update(partyID, role['roleName'], '', 0)

            roleList = RolesServices().list(partyID)
            # check if character is in array
            for role in roleList:
                print("For inserting... " + role['roleName'])
                if role['roleName'] == roleName:
                    if role['roleIsTaken'] == 0:
                        RolesServices().update(partyID, roleName, username, 1)
                        await updateET(message)
            await message.delete()

        # Leave
        if message.content == '$leave':
            partyName = message.channel.name
            partyID = PartiesServices().getParty(partyName)['_id']
            roleList = RolesServices().list(partyID)
            characterUser = message.author.nick or message.author.name
            for role in roleList:
                if role['roleUsername'] == characterUser:
                    RolesServices().update(partyID, role['roleName'], '', 0)
                    await updateET(message)
            await message.delete()

        # Clean
        if message.content == '$clean':
            characterUser = message.author.nick or message.author.name
            partyName = message.channel.name
            if characterUser == PartiesServices().getParty(partyName)['partyLeader']:
                partyID = PartiesServices().getParty(partyName)['_id']
                RolesServices().clean(partyID)
                await updateET(message)
            await message.delete()

        # Change Date
        if message.content.startswith('$setDate'):
            characterUser = message.author.nick or message.author.name
            partyName = message.channel.name
            if characterUser == PartiesServices().getParty(partyName)['partyLeader']:
                theDate = message.content[9:]
                partyID = PartiesServices().getParty(partyName)['_id']
                PartiesServices().updateDate(partyID, theDate)
                await updateET(message)
            await message.delete()

        # Change Time
        if message.content.startswith('$setTime'):
            characterUser = message.author.nick or message.author.name
            partyName = message.channel.name
            if characterUser == PartiesServices().getParty(partyName)['partyLeader']:
                partyID = PartiesServices().getParty(partyName)['_id']
                theTime = message.content[9:]
                PartiesServices().updateTime(partyID, theTime)
                await updateET(message)
            await message.delete()

        # Delete party
        if message.content == '$remove':
            characterUser = message.author.nick or message.author.name
            partyName = message.channel.name
            if characterUser == PartiesServices().getParty(partyName)['partyLeader']:
                partyID = PartiesServices().getParty(partyName)['_id']
                RolesServices().clean(partyID)
                PartiesServices().delete(partyID)
                botMsgID = BotMsgsServices().get(partyID)['botMsgID']
                msg = await message.channel.fetch_message(botMsgID)
                await msg.delete()
                BotMsgsServices().delete(partyID)

            await message.delete()

async def getTeam(partyName):
    party = PartiesServices().getParty(partyName)
    partyID = party['_id']
    partyDate = party['partyDate']
    partyTime = party['partyTime']
    partyLeader = party['partyLeader']
    roleList = RolesServices().list(partyID)
    string = None

    if partyDate == '' or partyTime == '':
        string = MsgTemplate().getNoTemplate()
    else:
        string = MsgTemplate().getTemplate(roleList, partyDate, partyTime, partyName.upper().replace('-', ' '), partyLeader)
    
    return string

async def updateET(message):
    # render ET update
    teamString = await getTeam(message.channel.name)
    partyID = PartiesServices().getParty(message.channel.name)['_id']
    botMsgID = BotMsgsServices().get(partyID)['botMsgID']
    theMSG = await message.channel.fetch_message(botMsgID)
    await theMSG.edit(content=f"{teamString}")

client.run("ODE4MTA2ODY4ODk5NjQzNDEy.YETPZQ.-jA99dQFLKuvvKStAm79qXFCyD8")