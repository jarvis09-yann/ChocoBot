# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot
# Code par jarvis09 merci de mettre un crédit si vous l'utilisez :D

import time  # pour le bot.latency
import discord
from discord.ext import commands
import random
from chocodico import *

intents = discord.Intents.all()  # intents, je ne sais pas trop à quoi ça sert, mais sans mon code marche pas
intents.members = True
intents.bans = True
intents.message_content = True
bot = commands.Bot(command_prefix="-", intents=intents)  # le préfixe et leur truc barbare
bot.remove_command('help')  # j'ai ma propre commande help

# Constante (parce qu'on les met partout)
RICKROLL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
FOOTER = "Team Chocolatine"
LOGO_CHOCOBOT = "https://i.goopics.net/ghlhkb.png"
BAN_HAMMER = "https://cdn.discordapp.com/emojis/961270811644289094.webp?size=128&quality=lossless"
CHANNEL_LOGS_ID = 1026517685007306773

###################################


cant_use_cmd = discord.Embed(title="Attention, vous n'avez pas accès a cette commande", color=0xedf305)
cant_use_cmd.set_author(name="Vous ne pouvez pas utiliser cette commande !", url=RICKROLL)
cant_use_cmd.set_thumbnail(url="https://media.tenor.com/4qOJaZloJj4AAAAj/tag.gif")
cant_use_cmd.set_footer(text=FOOTER)

""" A VOIR SI PRATIQUE OU MIEUX DE FAIRE DANS CHAQUE CODE (pour l'instant je fais dans chaque code
async def log(ctx):
	logs_channel = bot.get_channel(CHANNEL_LOGS_ID)
	log_embed = discord.Embed(title="**__Bienvenue !__**",
							  description=f"Bienvenue {ctx.author.mention} sur le serveur de la Team Chocolatine rends-toi dans le salon {ctx.author.mention} pour avoir accès à l'entièreté du serveur",
							  color=0xe9c46a)
	log_embed.set_author(url=ctx.author.avatar, name=ctx.author.name)
	log_embed.set_footer(text=FOOTER)
	await logs_channel.send(embed=log_embed)
"""


@bot.event
async def on_ready():
	logs = bot.get_channel(CHANNEL_LOGS_ID)
	print("Le Choco Bot est en ligne")
	await logs.send("Le Choco Bot est en ligne")


# rien de spécial, juste un msg pour dire que le bot est en ligne (qui est aussi envoyé dans la console !)


@bot.event
async def on_message(message):
	role = discord.utils.get(message.author.roles, id=1018205772737417278)
	logs = bot.get_channel(CHANNEL_LOGS_ID)
	# ID Dans l'ordre : Chocobot - Dyno - RaidProtect
	if role is None:
		for words in banned_words:
			if message.content.lower() == words:
				await message.delete(delay=False)
				await message.channel.send(f"{message.author.mention} Ici on dit Chocolatine :innocent:")
				await logs.send(f"{message.author.mention} a dit Pain Au Chocolat !")
				print("anti pac" + str(role))

	print("pas anti pac " + str(role))
	await bot.process_commands(message)


@bot.event
async def on_message_edit(before, after):
	logs = bot.get_channel(CHANNEL_LOGS_ID)
	print("before ", before.content)
	print("after ", after.content)
	for words in banned_words:
		if after.content.lower() in words:
			await after.delete(delay=False)
			channel = bot.get_channel(after.channel.id)
			await channel.send(f"{after.author.mention} Ici on dit Chocolatine :innocent:")
			await logs.send(f"{after.author.mention} a edit un message en Pain Au Chocolat")


@bot.event
async def on_member_join(member):
	logs = bot.get_channel(CHANNEL_LOGS_ID)
	arrival: discord.TextChannel = bot.get_channel(1009442645162070066)
	rules: discord.TextChannel = bot.get_channel(1009411624991473785)
	embed = discord.Embed(title="**__Bienvenue !__**",
						  description=f"Bienvenue {member.mention} sur le serveur de la Team Chocolatine rends-toi dans le salon {rules.mention} pour avoir accès à l'entièreté du serveur",
						  color=0xe9c46a)
	embed.set_thumbnail(url=LOGO_CHOCOBOT)
	embed.set_footer(text=FOOTER)
	await arrival.send(embed=embed)
	await logs.send(embed=embed)


@bot.event
async def on_member_remove(member):
	logs = bot.get_channel(CHANNEL_LOGS_ID)
	departure = bot.get_channel(1009442645162070066)
	embed = discord.Embed(title="**__Au revoir !__**",
						  description=f"Au revoir {member.mention} et peut être à bientôt sur le serveur de la Team Chocolatine !",
						  color=0xBD3100)
	embed.set_thumbnail(url=LOGO_CHOCOBOT)
	embed.set_footer(text=FOOTER)
	await departure.send(embed=embed)
	await logs.send(embed=embed)


@bot.event
async def on_member_ban(guild, user):
	logs = bot.get_channel(CHANNEL_LOGS_ID)
	arrival_departure: discord.TextChannel = bot.get_channel(1009442645162070066)
	embed = discord.Embed(title="**__BAN !__**",
						  description=f"{user.mention} s'est fait bannir du serveur {guild.name} !", color=0xBD3100)
	embed.set_author(name="ban", icon_url=BAN_HAMMER)
	embed.set_thumbnail(url=LOGO_CHOCOBOT)
	embed.set_footer(text=FOOTER)
	await arrival_departure.send(embed=embed)
	await logs.send(embed=embed)


@bot.command(name="help")  # commande help
async def help(ctx):
	logs = bot.get_channel(CHANNEL_LOGS_ID)
	await logs.send(f"commande help enclenchée par {ctx.author.name}")
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
	await ctx.send(embed=embed)


@bot.command(name="choco")
async def choco(ctx):
	logs = bot.get_channel(CHANNEL_LOGS_ID)
	rdm_choco = random.choice(list(dico))
	await ctx.send(dico[f"{rdm_choco}"])
	await logs.send(f"{ctx.author.name} a exécuté la commande choco, choco choisie:{rdm_choco} ")
	print(f"{ctx.author.name} a exécuté la commande choco, choco choisie: {rdm_choco} ")


@bot.command()
async def joke(ctx):
	logs = bot.get_channel(CHANNEL_LOGS_ID)
	joke_choice = random.choice(list(joke_dico))
	await ctx.send(joke_dico[f"{joke_choice}"])
	await logs.send(f"{ctx.author.name} a exécuté la commande joke, blague choisie:{joke_choice} ")
	print(f"{ctx.author.name} a exécuté la commande joke, blague choisie: {joke_choice} ")


@bot.command(name="cristal_ball")
async def cristal_ball(ctx, *msg):
	logs = bot.get_channel(CHANNEL_LOGS_ID)
	msg = " ".join(msg)
	await logs.send(f"commande cristall_ball exécutée par {ctx.author.name} contenant . {msg}")
	print(f"commande cristall_ball exécutée par {ctx.author.name} contenant {msg}")
	rdm_cristal = random.choice(list(cristal_dico))
	embed = discord.Embed(title="**QUESTION:**", description=f"{msg}", color=0x8005fa)
	embed.set_author(name="8ball")
	embed.set_thumbnail(url="https://emojis.wiki/emoji-pics/microsoft/crystal-ball-microsoft.png")
	embed.add_field(name="RÉPONSE:", value=f"{cristal_dico[rdm_cristal]}", inline=True)
	embed.set_footer(text=FOOTER + " - Attention, les réponses sont aléatoires ne pas les prendre au sérieux !")
	await ctx.send(embed=embed)


@bot.command(name="about")
async def about(ctx):  # commande about
	logs = bot.get_channel(CHANNEL_LOGS_ID)
	await logs.send(f"commande about exécutée par {ctx.author.name}")
	embed = discord.Embed(
		title="Le Choco bot est un bot discord dédié au serveur Team Chocolatine (https://discord.gg/wZ5aNWk33y) il a été développé par jarvis09#1787 & FiFolker#9350",
		color=0xff0000)
	embed.set_author(name="A propos du Choco Bot", url="https://discord.gg/wZ5aNWk33y")
	embed.set_thumbnail(url="https://media.tenor.com/b7HjoHE1K4QAAAAj/i%CC%87nfo-icon.gif")
	embed.set_footer(text=FOOTER)
	await ctx.send(embed=embed)


@bot.command(name="rick")
async def rick(ctx):  # ma commande (qui rickroll, marche que pour mon ID et celui de fifolker)
	logs = bot.get_channel(CHANNEL_LOGS_ID)
	if ctx.author.id == 721399612526559245 or 237588446397333505:
		await ctx.message.delete(
		)  # pour cacher les preuves, après y a les logs du discord et le shell biensur
		await ctx.send("**Vous avez été rickrollé !** ")
		await ctx.send(
			"\n https://tenor.com/view/rickroll-roll-rick-never-gonna-give-you-up-never-gonna-gif-22954713"
		)
		print(f"commande help enclanchée par {ctx.author.name} !")
		await logs.send(f"commande rickroll enclanchée par {ctx.author.name}")


@bot.command(name="ping")  # la commande ping, celle qui utilise le module time
async def ping(ctx):
	logs = bot.get_channel(CHANNEL_LOGS_ID)
	embed = discord.Embed(title=f"latence de {bot.latency}ms !", color=0x340cf3)
	embed.set_author(name="Pong !", url=RICKROLL)
	embed.set_thumbnail(url="https://media.tenor.com/c9WptHOa_LMAAAAM/pong.gif")
	embed.set_footer(text=FOOTER)
	await ctx.send(embed=embed)
	print(f"commande ping enclenchée par {ctx.author.name} !")
	await logs.send(f"commande ping enclenchée par {ctx.author.name}, la latence du bot est de {bot.latency}ms")


@bot.command(name="info")
async def info(ctx):  # quelques infos à propos du serveur
	logs = bot.get_channel(CHANNEL_LOGS_ID)
	serveur = ctx.guild
	serv_name = serveur.name
	nb_of_members = serveur.member_count
	msg = f"Le serveur **{serv_name}** a **{nb_of_members}** membres !"
	await ctx.send(msg)
	print(f"commande info enclenchée par {ctx.author.name} !")
	await logs.send(f"commande info exécutée par {ctx.author.name}")


@bot.command(name="say")  # un truc pr le fun comme ça
async def say(ctx, *, txt="Il faut rentrer un message dans le -say"):
	logs = bot.get_channel(CHANNEL_LOGS_ID)
	for words in banned_words:
		if txt.lower() == words:
			await ctx.send(f"{ctx.author.mention} Ici on dit Chocolatine :innocent:")
			break
		else:
			await ctx.send(f"{txt}")
			break
	await ctx.message.delete()
	print(f"commande say enclenchée par {ctx.author.name} contenant: {txt} !")
	await logs.send(f"commande say enclenchée par {ctx.author.name} contenant: {txt}")


@bot.command(name="kick")  # pour kick les gens, même si bon sans se mentir le kick de discord fait le job
async def kick(ctx, user: discord.User, *reason):
	logs = bot.get_channel(CHANNEL_LOGS_ID)
	if ctx.message.author.guild_permissions.administrator:
		reason = " ".join(reason)
		await ctx.guild.kick(user, reason=reason)
		embed = discord.Embed(title=f"{user} a été kick pour la raison {reason}, que cela lui serve de leçon !",
							  color=0xedf305)
		embed.set_author(name="KICK !", url=RICKROLL,
						 icon_url=BAN_HAMMER)
		embed.set_thumbnail(url="https://media.tenor.com/sWGfjLcAEDwAAAAC/kick-cartoon.gif")
		embed.set_footer(text=FOOTER)
		await ctx.send(embed=embed)
		ctx.send(embed=embed)

		print(f"{ctx.author.name} a expulsé {user} pour la raison {reason}")
		await logs.send(f"{ctx.author.name} a expulsé {user} pour la raison {reason}")
	else:
		await ctx.send(embed=cant_use_cmd)
		print(f"{ctx.author.name} a tenté d'utiliser la commande kick sur {user} pour la raison {reason} !")
		await logs.send(f"""{ctx.author.name} a tenté d'utiliser la commande kick sur {user} pour la raison {reason}, 
		mais il n'avait pas la permission administrateur donc la commande a échouée.""")


@bot.command(name="ban")  # pour ban
async def ban(ctx, user: discord.User, *reason):
	logs = bot.get_channel(CHANNEL_LOGS_ID)
	reason = " ".join(reason)
	if ctx.message.author.guild_permissions.administrator:
		await ctx.guild.ban(user, reason=reason)
		ban_embed = discord.Embed(title=f"{user} a été banni pour la raison: {reason} que cela lui serve de leçon !",
								  color=0xff0000)
		ban_embed.set_author(name="BAN !", url=RICKROLL,
							 icon_url=BAN_HAMMER)
		ban_embed.set_thumbnail(url="https://media.tenor.com/Kt1irdU_daUAAAAS/ban-admin.gif")
		ban_embed.set_footer(text=FOOTER)
		await ctx.send(embed=ban_embed)
		print(f"{ctx.author.name} a utilisé la commande ban sur {user} pour la raison {reason} !")
		await logs.send(f"{ctx.author.name} a tenté d'utiliser la commande ban sur {user} pour la raison {reason} !")
	else:
		await ctx.send(embed=cant_use_cmd)
		await logs.send(f"""{ctx.author.name} a tenté d'utiliser la commande ban sur {user} pour la raison {reason},
		mais il n'avait pas la permission administrateur donc la commande a échouée.""")
		print(f"""{ctx.author.name} a tenté d'utiliser la commande ban sur {user} pour la raison {reason},
		mais il n'avait pas la permission administrateur donc la commande a échouée.""")


@bot.command(name="unban")
async def unban(ctx, member: discord.User, *, reason=None):
	logs = bot.get_channel(CHANNEL_LOGS_ID)
	if ctx.message.author.guild_permissions.administrator:
		if reason is None:
			reason = f"Aucune raison donnée"
		await ctx.guild.unban(member, reason=reason)
		embed = discord.Embed(title=f"{member} a été unban par {ctx.author.name} pour la raison: {reason} !",
							  color=0x1111e8)
		embed.set_author(name="UNBAN", url=RICKROLL)
		# embed.set_thumbnail(url=member.avatar_url) marche pas a revoir
		embed.add_field(name="Modérateur", value=f"{ctx.author}", inline=True)
		embed.set_footer(text=FOOTER)
		await ctx.send(embed=embed)
		print(f"{ctx.author.name} a utilisé la commande deban ban sur {member} pour la raison {reason} !")
		await logs.send(f"{ctx.author.name} a utilisé la commande deban sur {member} pour la raison {reason}")
		print(f"Deban réussi {member.name}")
	else:
		await ctx.send(embed=cant_use_cmd)
		print(f"""{ctx.author.name} a tenté d'utiliser la commande unban sur {member} pour la raison {reason} mais il 
		n'avait pas la permission administrateur donc la commande a échouée.""")
		await logs.send(f"""{ctx.author.name} a tenté d'utiliser la commande unban sur {member} pour la raison {reason} 
		mais il n'avait pas la permission administrateur donc la commande a échouée.""")


@bot.command(name="mute")  # juste le mute
async def mute(ctx, member: discord.Member, *, reason=None):
	logs = bot.get_channel(CHANNEL_LOGS_ID)
	guild = ctx.guild
	muted_role = discord.utils.get(guild.roles, name="Muted")

	if ctx.message.author.guild_permissions.administrator:
		if not muted_role:
			muted_role = await guild.create_role(name="Muted")

			for channel in guild.channels:
				await channel.set_permissions(muted_role, speak=False, send_messages=False, read_message_history=True,
											  read_messages=False)
		await member.add_roles(muted_role, reason=reason)
		embed = discord.Embed(title=f"{member} a été mute pour la raison: {reason}, que cela lui serve de leçon !",
							  color=0x1111e8)
		embed.set_author(name="MUTE !", url=RICKROLL)
		embed.set_thumbnail(url="https://media.tenor.com/FWh2E4AQyTEAAAAM/mute.gif")
		embed.set_footer(text=FOOTER)
		await ctx.send(embed=embed)
		await logs.send(f"{ctx.author.name} a rendu muet {member}* pour la raison **{reason}")
		print(f"**{ctx.author.name} a rendu muet {member.mention} pour la raison:** *{reason}*")
		await member.send(
			f"Vous avez été rendu muet sur le serveur **{guild.name}** pour la raison: **{reason}**")
	else:
		await ctx.send(embed=cant_use_cmd)
		await logs.send(f"""{ctx.author.name} a tenté de rendre muet {member} pour la raison {reason},
		mais il n'avait pas la permission administrateur donc la commande a échouée.""")


@bot.command(name="unmute")  # unmute
async def unmute(ctx, member: discord.Member):
	logs = bot.get_channel(CHANNEL_LOGS_ID)
	if ctx.message.author.guild_permissions.administrator:
		muted_role = discord.utils.get(ctx.guild.roles, name="Muted")

		await member.remove_roles(muted_role)
		embed = discord.Embed(title=f"{member} a été unmute par {ctx.author.name} !", color=0x1111e8)
		embed.set_author(name="UNMUTE", url=RICKROLL)
		embed.set_thumbnail(url="https://media.tenor.com/rZRx_DyeF8sAAAAi/symbols.gif")
		embed.set_footer(text=FOOTER)
		await ctx.send(embed=embed)
		await member.send(f"Vous avez été unmute du serveur **{ctx.guild.name}** par **{ctx.author.name}**")
		await logs.send(f"Vous avez été unmute du serveur **{ctx.guild.name}** par **{ctx.author.name}**")
	else:
		await ctx.send(embed=cant_use_cmd)
		await logs.send(f"""{ctx.author.name} a tenté de unmute {member},
		mais il n'avait pas la permission administrateur donc la commande a échouée.""")


bot.run("MTAxODIwMzQ4NjY2NTU4NDc1MQ.GTbWxn.UFpARrCDkfNcb9zWikd3htT6MkDSw1OR-4rYHs")
#bot.run("OTA5MTE4MTM2OTI0NjU1NzA3.GcQSzf.OLRMge260C8tw5H6LZTMtjXnfZx2pddO6k5WP8") Testing bot
