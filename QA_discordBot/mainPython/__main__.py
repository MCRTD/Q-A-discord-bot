import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='r?')

@bot.event
async def on_ready():
    print("debug code 0")



bot.run('NTQ0MTY4MzYzMDI3NTk1Mjk0.XGA6Rw.RC1pQBQNXwAx3yukwoycmcA3lEI')


