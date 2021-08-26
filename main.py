# bot.py
import os

# imports
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
ch_general = int(os.getenv('GENERAL-CHAT'))
ch_musiccmds = int(os.getenv('MUSIC-CMDS'))

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(ch_general)
    await channel.send(
        f'A new GAMER has arrived! Welcome {member.name} /G A M E ! :dogege:'
    )


@bot.command()
async def sr(ctx, req):
    pass
    # TODO regex & YouTube API


@bot.command()
async def playlist(ctx):
    pass
    # TODO format playlist


bot.run(TOKEN)
