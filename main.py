# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
ch_general = int(os.getenv('GENERAL-CHAT'))
ch_musiccmds = int(os.getenv('MUSIC-CMDS'))

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_member_join(member):
    channel = client.get_channel(ch_general)
    await channel.send(
        f'A new GAMER has arrived! Welcome {member.name} /G A M E ! :dogege:'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    'TODO: RegEx'
    if message.content == '!sr' and message.channel.id == ch_musiccmds:
        response = 'todo'
        await message.channel.send(response)


client.run(TOKEN)
