import discord
import random

a="yazı","tura"


intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yapıldı.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('ÆSA'):
        await message.channel.send("Aleyküm Selam!")
    if message.content.startswith('ÆHELP'):
        await message.channel.send("ÆSA--Aleyküm Selam!-- Diye Cevap Verir.")
        await message.channel.send("ÆYAZITURA--Yazı Tura Atar.")
        await message.channel.send("ÆHELP--Komutları Gösterir.")
    if message.content.startswith('ÆYAZITURA'):
        yazitura=random.choice(a)
        await message.channel.send(yazitura)
    else:
        await message.channel.send("*Geçersiz*")

    client.run("MTMwMTk1NjMyMjg0NTEzMDgxNA.G65MWN.SFtR6uBgv926w5QNSEMkZq4wDF1gEDP6rVdkpg")
































