from discord.ext import commands
from discord.ext.commands import Bot
import os

import discord

# from dotenv import load_dotenv

# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')

# client = discord.Client()
Client = discord.Client()
client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print("Bot is ready!")

    # ps: did not know what to take as guild-name parameter
    # guild = discord.utils.get(client.guilds, name=GUILD)
    guild = discord.utils.get(client.guilds)

    if guild:
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

        channels = '\n - '.join([channel.name for channel in guild.channels])
        print(f'Guild Channels:\n - {channels}')


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == "cookie":
        await message.channel.send(":cookie:")

    # Reagiere auf das kürzel HZP um Informationen für die Hochschulzugangsprüfung an zu zeigen.
    # ToDo: Nur alle x Tage oder alle x Meldungen darauf reagieren...
    if 'hzp' in message.content.lower():
        await message.channel.send('**Wichtige Informationen** zur **HZP** findest du auch auf unserem Discourse unter: https://talk.wb-student.org/tag/hzp')
    elif 'wbtalk' in message.content.lower():
        await message.channel.send('**** zur **HZP** findest du auch auf unserem Discourse unter: https://talk.wb-student.org/tag/hzp')


client.run(
    'ODM4ODUwMjY3Nzc1NzYyNDYy.YJBGMA.wpVrxtREaRwh1eQh_CerGo0xrJE', bot=True)
