import discord
from discord.ext import commands
import random, os

# buat intents
intents = discord.Intents.default()
intents.message_content = True

# kenalkan bot-nya
bot = commands.Bot(command_prefix='$', intents=intents)

# buat reaksi dan command untuk bot-nya

@bot.event # agar bot bereaksi ketika ada sesuatu
async def on_ready(): # ketika bot siap
    print('BOT TELAH SIAP!')

@bot.command() # untuk menentukan command buat bot
async def idesampah(ctx):
    img_name = random.choice(os.lisdir('kerajinan'))
    with open(f'kerajinan/{img_name}', 'rb') as gambar: # membuka file gambar dan disimpan di variable
        picture = discord.File(gambar)
    await ctx.send(picture)

bot.run('your token here') # token kalian
