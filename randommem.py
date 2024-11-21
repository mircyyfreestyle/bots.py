import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


def m1():
    return 'https://i.pinimg.com/enabled_lo_mid/736x/a3/17/5e/a3175e2e49eb6d2acb3eef523d751c52.jpg'

def m2():
    return 'https://digitalsynopsis.com/wp-content/uploads/2017/12/funny-agency-life-creative-designer-copywriter-memes-1.jpg'

def m3():
    return 'https://i.pinimg.com/236x/be/22/b5/be22b56fe2c445ef382b31ca2e37491b.jpg'

def m4():
    return 'https://i.pinimg.com/200x/d5/40/31/d540317deab496587fd683168de632af.jpg'

def m5():
    return 'https://i.pinimg.com/enabled_lo_mid/736x/b8/0a/cd/b80acd70a2293cfec875a0f7f98ea73e.jpg'

def m6():
    return 'https://img.delicious.com.au/WqbvXLhs/del/2016/06/more-the-merrier-31380-2.jpg'

def m7():
    return 'https://media.tenor.com/QCo9jylxToUAAAAM/funny-meme.gif'

def m8():
    return 'https://i.pinimg.com/enabled_lo_mid/736x/0b/be/9d/0bbe9d0c4aad2784d0a092dc075cc0d5.jpg'

@bot.command('randommem')
async def randommem(ctx):

    z = random.randint(1, 36)

    if z == 1:
        mem = m1
    elif z in [2, 3]:
        mem = m2
    elif z in [4, 5, 6]:
        mem = m3
    elif z in [7, 8, 9, 10]:
        mem = m4
    elif z in [11, 12, 13, 14, 15]:
        mem = m5
    elif z in [16, 17, 18, 19, 20, 21]:
        mem = m6
    elif z in [22, 23, 24, 25, 26, 27, 28]:
        mem = m7
    else:  
        mem = m8


    image_url = mem()
    await ctx.send(image_url)


bot.run("")
