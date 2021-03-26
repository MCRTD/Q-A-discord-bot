import discord
import TranslateText
from discord.ext import commands

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


bot.run("token")
