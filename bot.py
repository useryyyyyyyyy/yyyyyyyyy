import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı!')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Token'ı çevresel değişkenlerden al
TOKEN = os.environ.get("DISCORD_TOKEN")
bot.run(TOKEN)
