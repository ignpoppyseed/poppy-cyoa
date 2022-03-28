from ast import Import
import discord
from discord import Client, Intents, Embed
import random
from discord_ui import UI, LinkButton, Button
from discord_slash import SlashCommand, SlashContext
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import (
    ComponentContext,
    create_actionrow,
    create_button,
    wait_for_component
)
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.ext import commands
from discord import guild
from bottoken import TOKEN

# Initialize Bot and Denote The Command Prefix
bot = commands.Bot(case_insensitive=True, command_prefix=">", activity= discord.Activity(type=discord.ActivityType.watching, name="Zork playthroughs"), status=discord.Status.online)
slash = SlashCommand(bot, sync_commands=True)
ui = UI(bot)
bot.remove_command('help') #disables the built in help command

# Runs when Bot Succesfully Connects
@bot.event
async def on_ready():
    print(f'ready to start the adventure!')

@bot.command()
async def adventure(ctx):
        msg = await ctx.channel.send("**West Of House**\nYou are standing in an open field west of a white house, with a boarded front door.\nThere is a small mailbox here.", components=[
            Button("Open mailbox", color="blurple", custom_id="1111")],
        )
        try:
            btn = await msg.wait_for("button", bot, by=ctx.author)
            await btn.respond("Opening the small mailbox reveals a leaflet.", components=[
            Button("Take leaflet", color="blurple", custom_id="2222")],
            )   
            try:
                btn = await msg.wait_for("button", bot, by=ctx.author)
                await btn.respond("**(Taken)**\n\n\"WELCOME TO ZORK!\n\n\n\nZORK is a game of adventure, danger, and low cunning. In it you will explore some of the most amazing territory ever seen by mortals. No computer should be without one!\"", components=[
                Button("Drop leaflet", color="blurple", custom_id="3333")],
            )
            except TimeoutError:
                await msg.delete()

        except TimeoutError:
                await msg.delete()


#**(Taken)**\n\n\"WELCOME TO ZORK!\n\n\n\nZORK is a game of adventure, danger, and low cunning. In it you will explore some of the most amazing territory ever seen by mortals. No computer should be without one!\"

#@bot.command()
#async def adventure(ctx: ComponentContext):
#    actionrow = create_actionrow(
#        *[
#            create_button(
#                label="Open mailbox", custom_id="box", style=ButtonStyle.primary
#            ),
#        ]
#    )
#    await ctx.send('**West Of House**\nYou are standing in an open field west of a white house, with a boarded front door.\nThere is a small mailbox here.', components=[actionrow])
    # note: this will only catch one button press, if you want more, put this in a loop
#    button_ctx: ComponentContext = await wait_for_component(bot, components=actionrow)
#    await button_ctx.send(content="You pressed a button!")

bot.run(TOKEN)