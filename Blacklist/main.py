import discord
from discord.ext import commands
import asyncio
import random

bot = commands.Bot(command_prefix=['?'], intents=discord.Intents.all())

@bot.event
async def on_ready():
  print('로딩완료')
  await bot.change_presence(activity=discord.Game("/docs"))

@bot.event
async def on_member_join(member):
  blacklist = [957541098685882431, 949545593754234890]
  if member.id in blacklist:
    await member.ban(reason='블랙리스트 등록유저')


bot.run('token')
