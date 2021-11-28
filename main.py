import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.command()
async def say(ctx, *, msg="leer"):
    await ctx.send(f"Deine Nachricht war: `{msg}`")
    print(f"{ctx.author} hat die Nachricht `{msg}` gesendet!")


bot.run("YourToken")
