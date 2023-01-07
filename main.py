import disnake, os
from disnake.ext import commands

intents = disnake.Intents.default()
intents.members = True
intents.message_content = True

activity = disnake.Activity(name="😐", type=disnake.ActivityType.listening)

bot = commands.InteractionBot(intents=intents, status=disnake.Status.idle, activity=activity)

@bot.event
async def on_ready():
    print(bot.user)

@bot.slash_command(description="Pong!")
async def ping(inter):
    pingerka = round(bot.latency*1000, 1)
    await inter.response.defer()
    await inter.edit_original_message(f"🏓 Pong! {pingerka} ms.")


bot.run(os.environ["token"])