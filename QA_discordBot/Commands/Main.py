import discord
from discord.ext import commands
from QA_discordBot.Core.Classes import Cod_Extension
from QA_discordBot.resources import TranslateText


class Main(Cod_Extension):

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

    @commands.command()
    async def ping(self, ctx):
        print('呼叫延遲檢測 -> ' + str(self.bot.latency))
        embed = discord.Embed(
            title="連線延遲 ping",
            description=str(self.bot.latency*1000)+' ms',
            color=0x00ff00
        )

        embed.set_author(
            name=ctx.message.author.name,
            icon_url=ctx.message.author.avatar_url
        )

        await ctx.send(embed=embed)


def setup(pybot):
    pybot.add_cog(Main(pybot))
