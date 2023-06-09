import discord
from discord.ext import commands
import asyncio
from random import randint

intents= discord.Intents.all()

client = commands.Bot(command_prefix="!",help_command = None,intents=intents)

@client.event
async def on_ready():
    print("Bot Ready !")
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.playing, name = "Clash Of Clans"))


@client.command(pass_context=True, name="dice" , aliases = ["dé","dés","dices"])

async def dice(ctx,nb:int) :
    result = randint(1,nb)
    embed=discord.Embed(
        title = f"Tirage d'un dé de {nb} faces",
        description = f"Le dé tombe sur `{result}` ! ",
        color = 0xAE02A1
    )

    await ctx.send(f"Le dé tombe sur {result}")


@client.command(pass_context=True,name="help")

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


@client.command(pass_context = True, name = "ban", aliases = ["banuser"])
@commands.has_permissions(ban_members = True)
async def ban (ctx, member : discord.member, jours : int, *, raison=""):
    await member.ban(reason = raison, delete_message_days = jours)
    e = discord.Embed(
        title = f"{ctx.message.author.name} a été banni du serveur.",
        description = f"Raison du bannissement : {raison}",
        color = 0xff0A00
    )

    await ctx.send(embed=e)

@client.command(pass_context = True, name = "kick", aliases = ["kickuser"])
@commands.has_permissions(kick_members=True)
async def kick (ctx,member : discord.Member, *, raison = ""):
    await member.kick(reason=raison)
    e = discord.Embed(
        title = f"{ctx.message.author.name} a été kick.",
        description = f"Raison du kick : `{raison}`",
        color = 0xFF0500
        )

    await ctx.send(embed=e)


client.run("MTAyOTMxMzg3NDc1NjkxMTE3NQ.GGo6H3.GCGg07Yy7lO7KSWzt_lPFroVuh7-EQ-98Hzz0w")