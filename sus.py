import discord
from discord.ext import commands
import asyncio
import time
import _thread
import datetime
from math import floor
from webserver import keep_alive
b = commands.Bot(command_prefix='.',intents=discord.Intents.all())
c = discord.Client()
import os 

          
@b.event
async def on_ready():
  await b.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Custom Status"))
  print("Bot Ready")
  async def threading():
    total_seconds_wait=5
    fg=0
    while total_seconds_wait:
      guil = b.get_guild(928684414794342400)
      memberList = guil.members 
      for user in memberList :
        fla=0
        for s in user.activities:
          fla=1
          if isinstance(s, discord.CustomActivity) :
            if str(s).find('gg/oliver') !=-1 :
              r = user.guild.get_role(952619066475028591)
              if r in user.roles :
                continue 
              else :
                embed=discord.Embed(title=f'Thank you for having discord.gg/noerror in your status!')
                embed.set_thumbnail(url="https://cdn.discordapp.com/icons/876113814314164256/a_498f8176aac9459d1f6f2e891afaa5c1.gif?size=1024 ")
                embed.description=f"Here are your **perks!** Hope you enjoy! :D\n**Image** and **embed** perms in  <#942733094723657738> \n\n**Note** : More Perks coming soon!"
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text=f'Role : {r.name} has been added',icon_url=user.avatar_url)
                asyncio.run_coroutine_threadsafe( user.add_roles(r), c.loop).result()
                print(user)
                try : 
                 asyncio.run_coroutine_threadsafe(user.send(embed=embed), c.loop).result()
                 print('SENT')
                except :
                  continue
            else :
              r = user.guild.get_role(952619066475028591)
              if r in user.roles :
                embed=discord.Embed(title=f'Perks have been removed')
                embed.set_thumbnail(url="https://cdn.discordapp.com/icons/876113814314164256/a_498f8176aac9459d1f6f2e891afaa5c1.gif?size=1024 ")
                embed.description=f"**Images** and **Embed** perms in  <#942733094723657738>\nhave been removed!\n\n**Reason** : You have removed **discord.gg/noerror** from your status!"
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text=f'Role : {r.name} has been removed',icon_url=user.avatar_url)
                asyncio.run_coroutine_threadsafe( user.remove_roles(r), c.loop).result()
                print(user)
                try : 
                  asyncio.run_coroutine_threadsafe(user.send(embed=embed), c.loop).result()
                  print('DEL SENT')
                except :
                  continue
        if fla == 0 :
          k = user.guild.get_role(952619066475028591)
          if k in user.roles :
            flaggg=0
            if isinstance(s, discord.CustomActivity):
              #print('u have status')
              flaggg=1
            if flaggg == 0 :
              print('u do not have status')
              embed=discord.Embed(title=f'Perks have been removed')
              embed.set_thumbnail(url="https://cdn.discordapp.com/icons/876113814314164256/a_498f8176aac9459d1f6f2e891afaa5c1.gif?size=1024 ")
              embed.description=f"**Images** and **Embed** perms in  <#942733094723657738>\nhave been removed!\n\n**Reason** : You have removed **discord.gg/noerror** from your status!"
              embed.timestamp = datetime.datetime.utcnow()
              embed.set_footer(text=f'Role : {k.name} has been removed',icon_url=user.avatar_url)
              asyncio.run_coroutine_threadsafe( user.remove_roles(k), c.loop).result()
              print(user)
              try : 
                asyncio.run_coroutine_threadsafe(user.send(embed=embed), c.loop).result()
                print('DEL SENT')
              except :
                continue
      if(fg==0):
          now = floor(time.time())
          fg=1
      if(now+1<=floor(time.time())):
          fg=0
          total_seconds_wait-=1
      if(total_seconds_wait==0):
          total_seconds_wait=5

        
  def between_callback():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(threading())
    loop.close()
  _thread.start_new_thread(between_callback,())

keep_alive()
my_secret = os.environ['token']
b.run(my_secret)

