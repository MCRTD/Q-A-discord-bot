import os
import discord
import json
import TranslateText
from discord.ext import commands

with open(os.path.abspath(os.path.dirname(os.getcwd()))+'/resources/Setting.json', mode='r',encoding='utf8') as Setting_Json:
    Setting_Json_data = json.load(Setting_Json)

bot = commands.Bot(command_prefix='r?')


@bot.event
async def on_ready():
    print("debug code 0")


@bot.command()
async def translate(ctx, lang, *, args):
    print('位置 -> '
          + str(ctx)
          )

    result = TranslateText.translate_text(None, lang, args)

    embed = discord.Embed(
        title=result.text,
        description=result.src
                    + ' -> '
                    + result.dest,
        color=0x00ff00
    )

    embed.set_author(
        name=ctx.message.author.name,
        icon_url=ctx.message.author.avatar_url
    )

    await ctx.send(embed=embed)


@bot.command()
async def ping(ctx):
    print('呼叫延遲檢測 -> ' + str(bot.latency))
    embed = discord.Embed(
        title="連線延遲 ping",
        description=str(bot.latency),
        color=0x00ff00
    )

    embed.set_author(
        name=ctx.message.author.name,
        icon_url=ctx.message.author.avatar_url
    )

    await ctx.send(embed=embed)

bot.run(Setting_Json_data['token'])
