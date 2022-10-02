# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot
# Code par jarvis09 merci de mettre un crédit si vous l'utilisez :D

import time  # pour le bot.latency
import discord
from discord.ext import commands
import os
import random
from chocodico import *

intents = discord.Intents.all()  # intents, je ne sais pas trop à quoi ça sert, mais sans mon code marche pas
intents.members = True
bot = commands.Bot(command_prefix="-", intents=intents)  # le préfixe et leur truc barbare
bot.remove_command('help')  # j'ai ma propre commande help

# Constante (parce qu'on les met partout)
RICKROLL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
FOOTER = "Team Chocolatine"


###################################

def log(msg):
    with open("bot_logs.txt", "a+") as log_it:
        heure = time.ctime()  # Un truc utile pour mettre des heures dans les logs !
        log_it.write(f"{heure} | {msg}\n")


cant_use_cmd = discord.Embed(title="Attention, vous n'avez pas accès a cette commande", color=0xedf305)
cant_use_cmd.set_author(name="Vous ne pouvez pas utiliser cette commande !", url=RICKROLL)
cant_use_cmd.set_thumbnail(url="https://media.tenor.com/4qOJaZloJj4AAAAj/tag.gif")
cant_use_cmd.set_footer(text=FOOTER)


@bot.event
async def on_ready():
    print("Le Choco Bot est en ligne")
    log("Le Choco Bot est en ligne")
# rien de spécial, juste un msg pour dire que le bot est en ligne (qui est aussi envoyé dans la console !)


@bot.event
async def on_member_join(member):
    arrival: discord.TextChannel = bot.get_channel(1009442645162070066)
    rules: discord.TextChannel = bot.get_channel(1009411624991473785)
    embed = discord.Embed(title="**__Bienvenue !__**",
                          description=f"Bienvenue {member.mention} sur le serveur de la Team Chocolatine rends-toi dans le salon {rules.mention} pour avoir accès à l'entièreté du serveur",
                          color=0xe9c46a)
    embed.set_thumbnail(url="https://i.goopics.net/ghlhkb.png")
    embed.set_footer(text=FOOTER)
    await arrival.send(embed=embed)


@bot.event
async def on_member_remove(member):
    departure = bot.get_channel(1009442645162070066)
    embed = discord.Embed(title="**Au revoir !__**",
                          description=f"Au revoir {member.mention} et peut être à bientôt sur le serveur de la Team Chocolatine !",
                          color=0xBD3100)
    embed.set_thumbnail(url="https://i.goopics.net/ghlhkb.png")
    embed.set_footer(text=FOOTER)
    await departure.send(embed=embed)


@bot.command()  # commande help
async def help(ctx):
    log(f"commande help enclenchée par {ctx.author.name}")
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


@bot.command()
async def choco(ctx):
    rdm_choco = random.choice(list(dico))
    await ctx.send(dico[f"{rdm_choco}"])
    log(f"{ctx.author.name} a executé la commande choco, choco choisie:{rdm_choco} ")
    print(f"{ctx.author.name} a executé la commande choco, choco choisie: {rdm_choco} ")


@bot.command()
async def joke(ctx):
    joke_choice = random.choice(list(joke_dico))
    await ctx.send(joke_dico[f"{joke_choice}"])
    log(f"{ctx.author.name} a executé la commande joke, blague choisie:{joke_choice} ")
    print(f"{ctx.author.name} a executé la commande joke, blague choisie: {joke_choice} ")


@bot.command()
async def cristal_ball(ctx, *msg):
    msg = " ".join(msg)
    log(f"commande cristall_ball executée par {ctx.author.name} contenant . {msg}")
    print(f"commande cristall_ball executée par {ctx.author.name} contenant {msg}")
    rdm_cristal = random.choice(list(cristal_dico))
    embed = discord.Embed(title="**QUESTION:**", description=f"{msg}", color=0x8005fa)
    embed.set_author(name="8ball")
    embed.set_thumbnail(url="https://emojis.wiki/emoji-pics/microsoft/crystal-ball-microsoft.png")
    embed.add_field(name="RÉPONSE:", value=f"{cristal_dico[rdm_cristal]}", inline=True)
    embed.set_footer(text=FOOTER + " - Attention, les réponses sont aléatoires ne pas les prendre au sérieux !")
    await ctx.send(embed=embed)


@bot.command()
async def about(ctx):  # commande about
    log(f"commande about exécutée par {ctx.author.name}")
    embed = discord.Embed(
        title="Le Choco bot est un bot discord dédié au serveur Team Chocolatine (https://discord.gg/wZ5aNWk33y) il a été développé par jarvis09#1787 & FiFolker#9350",
        color=0xff0000)
    embed.set_author(name="A propos du Choco Bot", url="https://discord.gg/wZ5aNWk33y")
    embed.set_thumbnail(url="https://media.tenor.com/b7HjoHE1K4QAAAAj/i%CC%87nfo-icon.gif")
    embed.set_footer(text=FOOTER)
    await ctx.send(embed=embed)


@bot.command()
async def rick(ctx):  # ma commande (qui rickroll, marche que pour mon ID et celui de fifolker)
    if ctx.author.id == 721399612526559245 or 237588446397333505:
        await ctx.message.delete(
        )  # pour cacher les preuves, après y a les logs du discord et le shell biensur
        await ctx.send("**Vous avez été rickrollé !** ")
        await ctx.send(
            "\n https://tenor.com/view/rickroll-roll-rick-never-gonna-give-you-up-never-gonna-gif-22954713"
        )
        print(f"commande help enclanchée par {ctx.author.name} !")
        log(f"commande help enclanchée par {ctx.author.name}")


@bot.command()  # la commande ping, celle qui utilise le module time
async def ping(ctx):
    embed = discord.Embed(title=f"latence de {bot.latency}ms !", color=0x340cf3)
    embed.set_author(name="Pong !", url=RICKROLL)
    embed.set_thumbnail(url="https://media.tenor.com/c9WptHOa_LMAAAAM/pong.gif")
    embed.set_footer(text=FOOTER)
    await ctx.send(embed=embed)
    print(f"commande ping enclanchée par {ctx.author.name} !")
    log(f"commande ping enclanchée par {ctx.author.name}, la latene du bot est de {bot.latency}ms")


@bot.command()
async def info(ctx):  # quelques infos à propos du serveur
    serveur = ctx.guild
    serv_name = serveur.name
    nb_of_members = serveur.member_count
    msg = f"Le serveur **{serv_name}** a **{nb_of_members}** membres !"
    await ctx.send(msg)
    print(f"commande info enclenchée par {ctx.author.name} !")
    log(f"commande info exécutée par {ctx.author.name}")


@bot.command()  # un truc pr le fun comme ça
async def say(ctx, *txt):
    await ctx.send(" ".join(txt))
    print(f"commande say enclenchée par {ctx.author.name} contenant: {txt} !")
    log(f"commande say enclenchée par {ctx.author.name} contenant: {txt}")


@bot.command()  # pour kick les gens, même si bon sans se mentir le kick de discord fait le job
async def kick(ctx, user: discord.User, *reason):
    if ctx.message.author.guild_permissions.administrator:
        reason = " ".join(reason)
        await ctx.guild.kick(user, reason=reason)
        embed = discord.Embed(title=f"{user} a été kick pour la raison {reason}, que cella lui serve de leçon !",
                              color=0xedf305)
        embed.set_author(name="KICK !", url=RICKROLL,
                         icon_url="https://cdn.discordapp.com/emojis/961270811644289094.webp?size=128&quality=lossless")
        embed.set_thumbnail(url="https://media.tenor.com/sWGfjLcAEDwAAAAC/kick-cartoon.gif")
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)
        ctx.send(embed=embed)

        print(f"{ctx.author.name} a expulsé {user} pour la raison {reason}")
        log(f"{ctx.author.name} a expulsé {user} pour la raison {reason}")
    else:
        await ctx.send(embed=cant_use_cmd)
        print(f"{ctx.author.name} a tenté d'utiliser la commande kick sur {user} pour la raison {reason} !")
        log(f"""{ctx.author.name} a tenté d'utiliser la commande kick sur {user} pour la raison {reason},
            mais il n'avait pas la permission administrateur donc la commande a échouée.""")


@bot.command()  # pour ban
async def ban(ctx, user: discord.User, *reason):
    reason = " ".join(reason)
    if ctx.message.author.guild_permissions.administrator:
        await ctx.guild.ban(user, reason=reason)
        ban_embed = discord.Embed(title=f"{user} a été banni pour la raison: {reason} que cella lui serve de leçon !",
                                  color=0xff0000)
        ban_embed.set_author(name="BAN !", url=RICKROLL,
                             icon_url="https://cdn.discordapp.com/emojis/961270811644289094.webp?size=128&quality=lossless")
        ban_embed.set_thumbnail(url="https://media.tenor.com/Kt1irdU_daUAAAAS/ban-admin.gif")
        ban_embed.set_footer(text=FOOTER)
        await ctx.send(embed=ban_embed)
        print(f"{ctx.author.name} a utilisé la commande ban sur {user} pour la raison {reason} !")
        log(f"{ctx.author.name} a tenté d'utiliser la commande ban sur {user} pour la raison {reason} !")
    else:
        await ctx.send(embed=cant_use_cmd)
        log(f"""{ctx.author.name} a tenté d'utiliser la commande ban sur {user} pour la raison {reason},
        mais il n'avait pas la permission administrateur donc la commande a échouée.""")
        print(f"""{ctx.author.name} a tenté d'utiliser la commande ban sur {user} pour la raison {reason},
        mais il n'avait pas la permission administrateur donc la commande a échouée.""")


@bot.command()  # pour déban
async def unban(ctx, user, *reason):
    if ctx.message.author.guild_permissions.administrator:
        reason = " ".join(reason)
        nom, user_id = user.split("#")
        banned_users = await ctx.guild.bans()
        member = discord.Member
        for i in banned_users:
            if i.user.name == nom and i.user.discriminator == user_id:
                await ctx.guild.unban(i.user.discriminator, reason=reason)
                embed = discord.Embed(title=f"{member} a été unban par {ctx.author.name} pour la raison: {reason} !",
                                      color=0x1111e8)
                embed.set_author(name="UNBAN", url=RICKROLL)
                embed.set_thumbnail(url="https://media.tenor.com/_4K_0sndwtEAAAAi/green-white.gif")
                embed.set_footer(text=FOOTER)
                await ctx.send(embed=embed)
                print(f"{ctx.author.name} a utilisé la commande deban ban sur {user} pour la raison {reason} !")
                log(f"{ctx.author.name} a utilisé la commande deban sur {user} pour la raison {reason}")
                return
        await ctx.send(f"L'utilisateur {user} n'est pas dans la banlist !")
        print(
            f"{ctx.author.name} a utilisé la commande deban sur {user} pour la raison {reason} mais il n'était pas dans la banlist !")
        log(f"{ctx.author.name} a tenté d'utilisé la commande deban sur {user} pour la raison {reason} mais il n'était pas dans la banlist")
    else:
        await ctx.send(embed=cant_use_cmd)
        print(f"""{ctx.author.name} a tenté d'utiliser la commande unban sur {user} pour la raison {reason}
            mais il n'avait pas la permission administrateur donc la commande a échouée.""")


@bot.command()  # juste le mute
async def mute(ctx, member: discord.Member, *, reason=None):
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
        log(f"{ctx.author.name} a rendu muet {member}* pour la raison **{reason}")
        print(f"**{ctx.author.name} a rendu muet {member.mention} pour la raison:** *{reason}*")
        await member.send(
            f"Vous avez été rendu muet sur le serveur **{guild.name}** pour la raison: **{reason}**")
    else:
        await ctx.send(embed=cant_use_cmd)
        log(f"""{ctx.author.name} a tenté de rendre muet {member} pour la raison {reason},
            mais il n'avait pas la permission administrateur donc la commande a échouée.""")


@bot.command()  # unmute
async def unmute(ctx, member: discord.Member):
    if ctx.message.author.guild_permissions.administrator:
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")

        await member.remove_roles(muted_role)
        embed = discord.Embed(title=f"{member} a été unmute par {ctx.author.name} !", color=0x1111e8)
        embed.set_author(name="UNMUTE", url=RICKROLL)
        embed.set_thumbnail(url="https://media.tenor.com/rZRx_DyeF8sAAAAi/symbols.gif")
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)
        await member.send(f"Vous avez été unmute du serveur **{ctx.guild.name}** par **{ctx.author.name}**")
    else:
        await ctx.send(embed=cant_use_cmd)
        log(f"""{ctx.author.name} a tenté de unmute {member},
        mais il n'avait pas la permission administrateur donc la commande a échouée.""")


bot.run("MTAxODIwMzQ4NjY2NTU4NDc1MQ.GTbWxn.UFpARrCDkfNcb9zWikd3htT6MkDSw1OR-4rYHs")
