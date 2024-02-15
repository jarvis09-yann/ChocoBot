# Version éxpérimentale du ChocoBot
# Code par jarvis09 & Fifolker merci de respecter les droits d'auteur :D

import discord  # n'utilise pas discord.py mais py-cord, un fork qui lui continue d'être mis a jour
from discord.ext import commands
import random  # pour faire des choix dans le chocodico
from ChocoDicoExperimental import *
import datetime


# Constantes
RICKROLL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
FOOTER = "Team Chocolatine"
LOGO_CHOCOBOT = "https://i.goopics.net/ghlhkb.png"
BAN_HAMMER = "https://cdn.discordapp.com/emojis/961270811644289094.webp?size=128&quality=lossless"
GUILD = 1009410836814639134
CHANNEL_LOGS_ID = 1026517685007306773

cant_use_cmd = discord.Embed(title="Attention, vous n'avez pas accès a cette commande", color=0xedf305)
cant_use_cmd.set_author(name="Vous ne pouvez pas utiliser cette commande !", url=RICKROLL)
cant_use_cmd.set_thumbnail(url="https://media.tenor.com/4qOJaZloJj4AAAAj/tag.gif")
cant_use_cmd.set_footer(text=FOOTER)

##############################

bot = discord.Bot()
logs = bot.get_channel(CHANNEL_LOGS_ID)
now = datetime.datetime.now()  # sert a avoir une heure pour les logs et la console


@bot.event
async def on_ready():
    print("Le ChocoBot est en ligne")
    #await logs.send("Le Choco Bot est en ligne")


@bot.event
async def on_member_remove(member):
    departure = bot.get_channel(1009442645162070066)
    embed = discord.Embed(title="**__Au revoir !__**", description=f"Au revoir {member.mention} et peut être à bientôt sur le serveur de la Team Chocolatine !", color=0xBD3100)
    embed.set_thumbnail(url=LOGO_CHOCOBOT)
    embed.set_footer(text=FOOTER + f" | membres :{member.guild.member_count}")
    #await departure.send(embed=embed)
    #await logs.send(embed=embed)


@bot.event
async def on_member_ban(guild, user):
    arrival_departure: discord.TextChannel = bot.get_channel(1009442645162070066)
    embed = discord.Embed(title="**__BAN !__**", description=f"{user.mention} s'est fait bannir du serveur {guild.name} !", color=0xBD3100)
    embed.set_author(name="ban", icon_url=BAN_HAMMER)
    embed.set_thumbnail(url=LOGO_CHOCOBOT)
    embed.set_footer(text=FOOTER + f" | membres : {guild.member_count}")
    #await arrival_departure.send(embed=embed)
    #await logs.send(embed=embed)


@bot.slash_command(name="help", description="affiche l'aide relative aux commandes", guilds_id=GUILD)
async def help(ctx):
    #await logs.send(f"commande help enclenchée par {ctx.author.name}")
    print(f"commande help enclenchée par {ctx.author.name}")  # les logs de la console
    embed = discord.Embed(description="""
                *Préfixe:* _**-**_\n
        **UTILITAIRE:**
         -info: affiche le nombre de membres sur le serveur
         -about: donne des informations à propos du bot
         -ping: permet de connaitre la latence du bot\n					
        **MODÉRATION:**
        ***NOTE: les commandes de la section MODÉRATION sont uniquement utilisables par les Administrateurs***       
         -ban [@utilisateur] [raison]: ban l'utilisateur mentionné
         -unban [@utilisateur] [raison]: déban l'utilisateur mentionné
         -mute [@utilisateur] [raison]: rend muet l'utilisateur mentionné
         -unmute [@utilisateur]: démute la personne mentionnée
         -kick [@utilisateur] [raison]: expulse l'utilisateur mentionné\n
         **FUN:**
        *ces commandes peuvent être utilisées par tout les utilisateurs*
        -cristal_ball [texte]: répond a vos questions (texte après la cmd) a l'aide de sa boule magique...
        -say [texte] renvoie que vous avez écrit après la commande
        -choco envoie une image de chocolatine aléatoirement
        -joke envoie une blague (nulle) aléatoire
            """, color=0x008000)
    embed.set_author(name="AIDE RELATIVE AUX COMMANDES", url=RICKROLL)
    embed.set_thumbnail(url="https://media.tenor.com/GXMu0NRMHQgAAAAC/question-mark.gif")
    embed.set_footer(text=FOOTER)
    await ctx.respond(embed=embed)


@bot.slash_command(name="choco", description="Envoie une image de chocolatine aléatoirement", guilds_id=GUILD)
async def choco(ctx):
    rdm_choco = random.choice(list(dico))
    await ctx.respond(dico[f"{rdm_choco}"])
    #await logs.send(f"{ctx.author.name} a exécuté la commande choco, choco choisie:{rdm_choco} ")
    print(f"{ctx.author.name} a exécuté la commande choco, choco choisie: {rdm_choco} ")


@bot.command(name="joke", description="Envoie une blague (nulle) aléatoirement", guilds_id=GUILD)
async def joke(ctx):
	joke_choice = random.choice(list(joke_dico))
	await ctx.respond(joke_dico[f"{joke_choice}"])
	#await logs.send(f"{ctx.author.name} a exécuté la commande joke, blague choisie:{joke_choice} ")
	print(f"{ctx.author.name} a exécuté la commande joke, blague choisie: {joke_choice} ")


@bot.command(name="cristal_ball", description="Répond a vos questions grâce a sa boule de cristal", guilds_id=GUILD)
async def cristal_ball(ctx, *message: discord.Option(str, "écrivez ce que vous vous voulez demander a la boule de cirstal", required = True, default = "la boule de cristal ne peuut pas deviner votre demande !")):
	message = " ".join(msg)
	#await logs.send(f"commande cristall_ball exécutée par {ctx.author.name} contenant . {msg}")
	print(f"commande cristall_ball exécutée par {ctx.author.name} contenant {message}")
	rdm_cristal = random.choice(list(cristal_dico))
	embed = discord.Embed(title="**QUESTION:**", description=f"{message}", color=0x8005fa)
	embed.set_author(name="8ball")
	embed.set_thumbnail(url="https://emojis.wiki/emoji-pics/microsoft/crystal-ball-microsoft.png")
	embed.add_field(name="RÉPONSE:", value=f"{cristal_dico[rdm_cristal]}", inline=True)
	embed.set_footer(text=FOOTER + " - Attention, les réponses sont aléatoires ne pas les prendre au sérieux !")
	await ctx.respond(embed=embed)


@bot.command(name="about", description = "Donne des informations relatives au ChocoBot", guilds_id=GUILD)
async def about(ctx):  # commande about
	#await logs.send(f"commande about exécutée par {ctx.author.name}")
	embed = discord.Embed(title="Le Choco bot est un bot discord dédié au serveur Team Chocolatine (https://discord.gg/wZ5aNWk33y) il a été développé par jarvis09#1787 & FiFolker#9350", color=0xff0000)
	embed.set_author(name="A propos du Choco Bot", url="https://discord.gg/wZ5aNWk33y")
	embed.set_thumbnail(url="https://media.tenor.com/b7HjoHE1K4QAAAAj/i%CC%87nfo-icon.gif")
	embed.set_footer(text=FOOTER)
	await ctx.respond(embed=embed)


# ICI CMD RICK (A FIX, il faut que elle soit invisible au commun des mortels)


@bot.command(name="ping", description = "Renvoie la latence du bot", guilds_id=GUILD)  # la commande ping, celle qui utilise le module time
async def ping(ctx):
	embed = discord.Embed(title=f"latence de {round(bot.latency, 3)}ms !", color=0x340cf3)
	embed.set_author(name="Pong !", url=RICKROLL)
	embed.set_thumbnail(url="https://media.tenor.com/c9WptHOa_LMAAAAM/pong.gif")
	embed.set_footer(text=FOOTER)
	await ctx.respond(embed=embed)
	print(f"commande ping enclenchée par {ctx.author.name} !")
	#await logs.send(f"commande ping enclenchée par {ctx.author.name}, la latence du bot est de {bot.latency}ms")



@bot.command(name="info", description = "Donne des informations a propos du serveur sur lequel elle est executée", guilds_id=GUILD)
async def info(ctx):  # quelques infos à propos du serveur
	serveur = ctx.guild
	serv_name = serveur.name
	nb_of_members = serveur.member_count
	await ctx.respond(f"Le serveur **{serv_name}** a **{nb_of_members}** membres !")
	print(f"commande info enclenchée par {ctx.author.name} !")
	#await logs.send(f"commande info exécutée par {ctx.author.name}")


@bot.command(name="say", description = "Renvoie ce que vous écrivez dans la commande", guilds_id = GUILD)  # un truc pr le fun comme ça
async def say(ctx, *, message: discord.Option(str,"écrivez ce que vous voulez que le bot dise", required = True, default = "")):
	if message == "":
		message = "Le chocobot ne peux pas deviner ce que vous voulez dire :blink:"
	#for words in banned_words:
	#	if message.lower() == words:
	#		await ctx.send(f"{ctx.author.mention} Ici on dit Chocolatine :innocent:")
	#		break
	#	else:
	#		await ctx.send(f"{message}")
	#		break
	#await ctx.message.delete()
	print(f"commande say enclenchée par {ctx.author.name} contenant: {message} !")
	#await logs.send(f"commande say enclenchée par {ctx.author.name} contenant: {message}")
	await message.respond(message)



bot.run("Oh fuck i forgot to remove it...")
