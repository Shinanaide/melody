# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import youtube_dl

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
async def sr(ctx, req: str):
    vc = ctx.author.voice.channel  # voice channel of author
    try:
        await vc.connect()
    except:
        pass

    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    song_exists = os.path.isfile("song.webm")

    if song_exists:
        try:
            os.remove("song.webm")
        except PermissionError:
            await ctx.send("Wait for the current playing music to end or use the 'stop' command")
            return

    # download and conversion options for youtube-dl (should be the best configuration)
    ydl_opts = {
        'format': '249/250/251'
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([req])
    for file in os.listdir("./"):
        if file.endswith(".webm"):
            os.rename(file, "song.webm")
    voice.play(discord.FFmpegPCMAudio("song.webm"))
    # TODO playlist functionality


@bot.command()
async def playlist(ctx):
    pass
    # TODO format playlist into discord chat


@bot.command()
async def remove(ctx, idx):
    pass
    # TODO remove song with idx from playlist


@bot.command()
async def move(ctx, idx1, idx2):
    pass
    # TODO move song with idx1 to position idx2


@bot.command()
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()


@bot.command()
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()


@bot.command()
async def leave(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    try:
        if voice.is_connceted():
            await voice.disconnect()
    except:
        pass


@bot.command()
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()


@bot.command()
async def clear(ctx):
    pass
    # TODO clear playlist & stop current song


@bot.command()
async def skip(ctx):
    pass
    # TODO skip current song


@bot.command()
async def jump(ctx, idx):
    pass
    # TODO jump to specified idx in playlist


@bot.command()
async def shuffle(ctx):
    pass
    # TODO shuffle playlist


bot.run(TOKEN)
