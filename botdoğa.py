mport discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('Æyokolmasüre'):
        await message.channel.send("Strafor 5000 yil - 2 Milyon yıl")
        await message.channel.send("Cam Şişe 4000 yıl")
        await message.channel.send("Plastik 1000 yıl")
        await message.channel.send("Poliüretan (Sentetik fiberler, yapıştırıcılar, halıların alt kısmı ve sert plastik contalar) 1000 yıl")
        await message.channel.send("Telefon Kartı 1000 yıl")
        await message.channel.send("Kaset 100 yıl - 1000 yıl")
        await message.channel.send("Su Boruları 1000 yıl")
        await message.channel.send("Balık Oltası 600 yıl")
        await message.channel.send("Pil 300 yıl")
        await message.channel.send("Çiklet 5 yıl - 25 yıl")
        await message.channel.send("Sigara İzmariti 1 yıl - 2 yıl")
        await message.channel.send("Mendil 2-4 hafta")

    if message.content.startswith('!help'):
        await message.channel.send("!video")
        await message.channel.send("Æyokolmasüre")  

    await bot.process_commands(message)  

@bot.command()
async def video(ctx):
    video_url = "https://www.youtube.com/watch?v=n7AfJVUaNeQ"
    await ctx.send(video_url)

bot.run(The Token)
