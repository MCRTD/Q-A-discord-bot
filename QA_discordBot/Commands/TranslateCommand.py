import discord
from discord.ext import commands
from QA_discordBot.Core.Common import Cod_Extension
from QA_discordBot.Core import TranslateText


class TranslateCommand(Cod_Extension):

    @commands.command()
    async def translate(self, ctx, lang, *, args):
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


def setup(pybot):
    pybot.add_cog(TranslateCommand(pybot))
