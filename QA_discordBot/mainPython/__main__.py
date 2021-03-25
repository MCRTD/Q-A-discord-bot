import discord
from discord.ext import commands
import googletrans
from googletrans import Translator

def translate_text(oringinlang, targetlang, input):
	t = googletrans.Translator()
	if oringinlang == None :
		result = t.translate(input, dest = targetlang )
	else :
		result = t.translate(input, scr = originlang, dest = targetlang )
	
	print('目標語言 -> ' + str(targetlang))
	
	print('句子 -> ' + str(input)
	+ ' >>> '
	+ str(result.text))
	
	return result

bot = commands.Bot(command_prefix=  'r?')

@bot.event
async def on_ready():
    print("debug code 0")
    
@bot.command()
async def translate(ctx, lang, *, args):
	print('位置 -> ' + str(ctx))
	#print('目標語言 -> ' + str(lang))
	#print('句子 -> ' + str(args), end=' >>> ')
	#t = googletrans.Translator()
	result =translate_text(None, lang, args)

	embed=discord.Embed(
	title=result.text
	, description=result.src
		+' -> '
		+ result.dest
	, color=0x00ff00
	)

	embed.set_author(
	name = ctx.message.author.name, icon_url = ctx.message.author.avatar_url
	)

	await ctx.send(embed=embed)

bot.run('token')

