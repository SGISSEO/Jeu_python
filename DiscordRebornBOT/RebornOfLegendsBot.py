import os
from dotenv import load_dotenv



import discord
from discord import message


from discord.ext import commands
from discord.ext.commands import MissingPermissions
from random import randint

load_dotenv(dotenv_path="config")


intents = discord.Intents.all()


bot = commands.Bot(command_prefix = "!", intents=intents)



@bot.event
async def on_ready():
    print("Ready !")



@bot.event
async def on_ready():
    print("Bot Ready !")
    await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.playing , name = "Clash Of Clans"))



@bot.command(pass_context=True, name="dice" , aliases = ["dé","dés","dices"])
async def dice(ctx,nb:int) :
    result = randint(1,nb)
    embed=discord.Embed(
        title = f"Tirage d'un dé de {nb} faces",
        description = f"Le dé tombe sur `{result}` ! ",
        color = 0xAE02A1
    )
    await ctx.send(f"Le dé tombe sur {result}")



async def help(ctx):
    embed=discord.Embed(
        title = "Page d'aide 1/1",
        description = "Vous trouverez ici toutes les commandes du bot",
        color = 0x0AAB1D
    )
    embed.add_field(
        name="Pour lancer un dé",
        value="Faîtes `!dice <number of face>` ou encore ` !dé <nombre de faces>`"
    )
    await ctx.send(embed=embed)



@bot.event
async def on_member_join(member):
    channel = bot.get_channel(880132486955425803) # ID du channel
    await channel.send(f"**Bienvenu(e)** à {member.mention} sur le *serveur* **RebornOfLegends** !")




@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1049431854324916234)
    await channel.send(f"**Good Bye !** à {member.mention} qui vient de **quittez** le *serveur* **RebornOfLegends** !")



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.channel.send("Tu n'es pas un **membre** du **staff** pour pouvoir utilisé ceci !")



@bot.command()
async def say(ctx, number, *texte):
    for i in range(int(number)):
        await ctx.send(" ".join(texte))



# Creaton du rôle Muted
async def createMutedRole(ctx):
    mutedRole = await ctx.guild.create_role(name = "Muted",
                                            permissions = discord.Permissions(
                                                send_messages = False,
                                                speak = False),
                                            reason = "Creation du role Muted pour mute des gens.")
    for channel in ctx.guild.channels:
        await channel.set_permissions(mutedRole, send_messages = False, speak = False)
    return mutedRole


async def getMutedRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Muted":
            return role

    return await createMutedRole(ctx)



@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseigné"):
    mutedRole = await getMutedRole(ctx)
    await member.add_roles(mutedRole, reason = reason)
    await ctx.send(f"{member.mention} a été **MUTE** !")
    await ctx.message.delete()



@bot.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await member.send(f" Tu viens d'être **UNMUTED**{ctx.guild.name}")
    embed = discord.Embed(title="RebornOfLegends", description=f" **UNMUTED** ! | {member.mention}",colour=discord.Colour.red())
    await ctx.send(embed=embed)
    await ctx.message.delete()

@bot.command()
async def serverInfo(ctx):
    server = ctx.guild
    numberOfTextChannels = len(server.text_channels)
    numberOfVoiceChannels = len(server.voice_channels)
    serverDescription = server.description
    numberOfPerson = server.member_count
    serverName = server.name
    message = f"Le serveur **{serverName}** contient *{numberOfPerson}* personnes. \n la description du serveur est *{serverDescription}*. \n Ce serveur possède {numberOfTextChannels} salons écrit ainsi que {numberOfVoiceChannels} vocaux."
    await ctx.send(message)



@bot.command()
async def getinfo(ctx, info):
    server = ctx.guild
    if info == "memberCount":
        await ctx.send(server.member_count)
    elif info == "numberOfChannel":
        await ctx.send(len(server.voice_channels) + len(server.text_channels))
    elif info == "name":
        await ctx.send(server.name)
    else:
        await ctx.send("Etrange... Je ne connais pas cela")



@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, nombre : int):
    messages = [message async for message in ctx.channel.history(limit=nombre + 1)]
    for message in messages:
        await message.delete()



@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user : discord.Member, *reason):

    await user.send(f"{user.mention} Vous avez été **KICK** du *serveur* **RebornOfLegends** !")
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason = reason)
    await ctx.send(f"{user.mention} a bien été **KICK** !")
    await ctx.message.delete()



@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user : discord.Member, *reason):

    await user.send(f"{user.mention} Vous avez été **BAN** du *serveur* **RebornOfLegends** !")
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason = reason)
    await ctx.send(f"{user.mention} a bien été **BAN** !")
    await ctx.message.delete()



@bot.command(name='unban')
@commands.has_permissions(ban_members=True)
async def _unban(ctx, id: int):

    user = await bot.fetch_user(id)
    await ctx.channel.send(f'{user.mention} a bien été **UNBAN** !')
    await ctx.guild.unban(user)
    await ctx.message.delete()




bot.run(os.getenv("TOKEN"))