import discord
import json
from discord.ext import commands
import platform

def get_prefix(client, message):
 
bot=commands.Bot(command_prefix=get_prefix)
invitelink="https://discord.com/api/oauth2/authorize?client_id=758552991564431430&permissions=8&scope=bot"
prefix="#"
name="Made by Rohan Op"
Token="NzU4NTUyOTkxNTY0NDMxNDMw.X2wnhg.jCgg58JS1dr5y4zCyasozL_yV54"

async def owner(ctx):
    return ctx.author.id==592262877549690892
     
@bot.event
async def on_ready():
    print("Bot is running!")
    game=discord.Game("Bot by Rohan Op")
    await bot.change_presence(status=discord.Status.idle,activity=game)
    
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if(message.author==bot.user):
        return
    elif(bot.user.mentioned_in(message)):
        await message.channel.send(f"Prefix is ` {prefix} `")
        
@bot.event
async def on_member_join(member):
    channel=discord.utils.get(member.guild.text_channels,id=748402791583842339)
    server=member.guild
    await channel.send(f"{member.name} just joined {server.name}")
    
@bot.event
async def on_member_remove(member):
    channel=discord.utils.get(member.guild.text_channels,id=748402791583842339)
    server=member.guild
    await channel.send(f"{member.name} just left {server.name}")
    
@bot.command()
async def add(ctx,a:int,b:int):
    await ctx.send(f"Your ans is: **{a+b}**")
    
@bot.command()
async def sub(ctx,a:int,b:int):
    await ctx.send(f"Your ans is: **{a-b}**")
    
@bot.command()
async def multiply(ctx,a:int,b:int):
    await ctx.send(f"Your ans is: **{a*b}**")
    
@bot.command()
async def divide(ctx,a:int,b:int):
    await ctx.send(f"Your ans is: **{a/b}**")
        
@bot.command()
async def info(ctx,user:discord.User=None):
    if(user):
        name=f"{user.name}"
        id=f"{user.id}"
        e=discord.Embed(color=0xFF0000)
        e.add_field(name="Name",value=name)
        e.add_field(name="Id",value=id)
        e.set_footer(text=f"{name}")
        await ctx.send(embed=e)
        
@bot.command()
async def ping(ctx):
     pingtime=bot.latency
     e=discord.Embed(color=0xFD0000)
     e.add_field(name="Pong! API Response Time",value=pingtime)
     e.set_footer(text=f"{name}")
     await ctx.send(embed=e)
     
@bot.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await ctx.message.delete()
    await ctx.send(mesg)
    
@bot.command()
async def invite(ctx):
	invitelink1=f"{invitelink}"
	e=discord.Embed(color=0xFF0000)
	e.add_field(name="INVITE ME",value=invitelink1)
	e.set_footer(text=f"{name}")
	await ctx.send(embed=e)
	
@bot.command()
@commands.check(owner)
async def kick(ctx,user:discord.Member=None):
    if(user):
        await ctx.send(f"{user.name} was kicked!")
        await user.kick()
        
@bot.command()
@commands.check(owner)
async def ban(ctx,user:discord.Member=None):
    if(user):
        await ctx.send(f"{user.name} was banned!")
        await user.ban()
        
@bot.command()
async def binfo(ctx):
    pyv=platform.python_version()
    botos=platform.system()
    discordv=discord.__version__
    e=discord.Embed(color=0xFF0000)
    e.add_field(name="Python version",value=pyv)
    e.add_field(name="OS",value=botos)
    e.add_field(name="Discord version",value=discordv)
    e.set_footer(text=f"{name}")
    await ctx.send(embed=e)
    
@bot.command()
@commands.check(owner)
async def nick(ctx,member:discord.Member,*,name):
    await member.edit(nick=name)
    await ctx.send(f"Renamed {member} to {name}")
    
@bot.command()
async def avatar(ctx,member:discord.Member):
    await ctx.send(member.avatar_url)
    
@bot.command(name='whois')
async def userinfo(ctx, member: discord.Member):
    embed = discord.Embed(title= f'{member}', color=0xfcf8f8)
    embed.add_field(name='**Username:**', value=member.name, inline=False)
    embed.add_field(name='**Discriminator:**', value=member.discriminator, inline=False)
    embed.add_field(name='**ID:**', value=member.id, inline=False)
    embed.add_field(name='**Status:**', value=member.status, inline=False)
    embed.add_field(name="**Highest Role:**", value=member.top_role, inline=False)
    embed.add_field(name='**Account Created:**', value=member.created_at.__format__('%A, %d. %B %Y | %H:%M:%S'), inline=False)
    embed.add_field(name='**Server Join Date:**', value=member.joined_at.__format__('%A, %d. %B %Y | %H:%M:%S'), inline=False)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"{name}")
    await ctx.send(content=None, embed=embed)
	
bot.remove_command('help')
@bot.command()
async def help(ctx):
    e=discord.Embed(color=0xFFFF00)
    e.add_field(name=f"{prefix}binfo",value="You can see the bot info.")
    e.add_field(name=f"{prefix}say",value="Say Something with bot.")
    e.add_field(name=f"{prefix}ping",value="Shows bot latency.")
    e.add_field(name=f"{prefix}Aadd {1} {2}",value="Adds 2 numbers.")
    e.add_field(name=f"{prefix}sub {1} {2}",value="Subtracts 2 numbers.")
    e.add_field(name=f"{prefix}multiply {1} {2}",value="Multiplies 2 numbers.")
    e.add_field(name=f"{prefix}divide {1} {2}",value="Divides 2 numbers.")
    e.add_field(name=f"{prefix}info (user)",value="Shows info about a user.")
    e.add_field(name=f"{prefix}invite",value="Gives the link to invite this bot.")
    e.add_field(name=f"{prefix}nick (user)",value="Changes the nickname of a user.")
    e.add_field(name=f"{prefix}avatar (user)",value="Shows the avatar of a user.")
    e.add_fied(name=f"{prefix}whois (user)",value="Full details of user.")
    e.add_field(name=f"{prefix}kick",value="Kick the member if you have admin permission.")
    e.add_field(name=f"{prefix}ban",value="Ban the member if you have admin permission.")
    e.set_footer(text=f"{name}")
    await ctx.send(embed=e)













bot.run(f'{Token}')
