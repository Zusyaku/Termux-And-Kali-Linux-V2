try:
    import discord, asyncio, os, re, time, sys, random, requests
    from discord.ext import commands
    from re import search
except:
    print("Please Install All Packages..")
    time.sleep(2)
    input("PRESS ENTER TO CLOSE..")
    sys.exit()
logo = """
╔═══════════════════════════════════════════════════════╗
║  ____  _                       _                      ║
║ |  _ \(_)___  ___ ___  _ __ __| |  ___ ___  _ __ ___  ║
║ | | | | / __|/ __/ _ \| '__/ _` | / __/ _ \| '_ ` _ \ ║
║ | |_| | \__ \ (_| (_) | | | (_| || (_| (_) | | | | | |║
║ |____/|_|___/\___\___/|_|  \__,_(_)___\___/|_| |_| |_|║
║                 Coded by Amine Mrx                   ║
╚═══════════════════════════════════════════════════════╝                                                                """

ballpoll_responses = ['Yes', "no way", 'nah', 'ok boomer', 'i prefer to say no', 'yessir', 'hell nah']

try:
    f = open('config.extremedev', 'r+')
    f.close
except:
    try:
        f = open('config.extremedev', 'a+').write('bot_prefix: "bot prefix",\nbot_token: "bot token",\nbot_status: "Bot Status",\nbot_owner: "your id"')
        print("Config file created('config.extremedev'), now please verify it and add values into it..")
        time.sleep(2)
        input("Press ENTER to quit..")
        sys.exit()
    except:
        print("Please copy all files from our github\n\nhttps://github.com/ExtremeDude-tech/")
        time.sleep(2)
        input("Press ENTER to quit..")
        sys.exit()

try:
    config_load = open('config.extremedev', 'r+', encoding='utf-8').readlines()
    if len(config_load) == 4:
        for line in config_load:
            line_after = line
            
            try:
                if "bot_prefix" in line_after:
                    bot_prefix = re.search(r'bot_prefix: "(.*?)",', str(line_after)).group(1)
                elif "bot_token" in line_after:
                    bot_token = re.search(r'bot_token: "(.*?)",', str(line_after)).group(1)
                elif "bot_owner" in line_after:
                    owner = re.search(r'bot_owner: "(.*?)"', str(line_after)).group(1)
                elif "bot_status" in line_after:
                    bot_status = re.search(r'bot_status: "(.*?)",', str(line_after)).group(1)
                else:
                    print("ERROR IN 'config.extremedev', PLEASE EDIT THE FILE AND COME BACK AFTER..")
                    time.sleep(5)
                    input("Please press ENTER to quit..")
                    sys.exit()
            except Exception as e:
                print("ERROR IN 'config.extremedev', PLEASE EDIT THE FILE AND COME BACK AFTER..\n\n{}".format(e))
                time.sleep(5)
                input("Please press ENTER to quit..")
                sys.exit()
    else:
        print("ERROR IN 'config.extremedev', PLEASE EDIT THE FILE AND COME BACK AFTER..\n(more or less then 3 values in folder)")
        time.sleep(5)
        input("Please press ENTER to quit..")
        sys.exit()
except:
    print("Error..")
    time.sleep(5)
    input("Press ENTER to quit..")
    sys.exit()
print("Loaded all values succesfully")
client = commands.Bot(command_prefix=bot_prefix)






@client.command()
@commands.has_permissions(administrator=True)
async def status(ctx, *args):
    mesg = ' '.join(args)
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(mesg))
    status1122 = ('Status changed to:' + f"**{mesg}**")
    await ctx.send(status1122)

@client.event
async def on_ready():
    os.system('title Bot Online..')
    os.system('cls')
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(bot_status))
    print()
    print(logo)
    print()
    print("Bot Running..")




@client.command()
async def prefix(ctx):
    if ctx.author.id == int(owner):
        await ctx.send('{} is my prefix\nType {}help to get the help command'.format(ctx.prefix, ctx.prefix))
    else:
        await ctx.send("You cannot do that, only <@!{}> can..".format(owner))

@client.event
async def on_command_error(ctx, error):
    if not isinstance(error, commands.CheckFailure):
        await ctx.send("Invalid Command\n\nError: {}".format(error)) 


@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member:discord.Member = None, *args):
    if not member:
        await ctx.send("Please specify a member")
        return
    try:
        mesg = ' '.join(args)
        await member.kick()
        await ctx.send("{} got kicked, reason: `{}`".format(member.mention, mesg))
    except:
        await member.kick()
        await ctx.send(f"{member.mention} got kicked, reason: `None`")
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have `administrator permissions`")

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member:discord.Member = None, *args):
    if not member:
        await ctx.send("Please specify a member..\nhttps://i.imgur.com/RkIfjMP.gif")
        return
    try:
        mesg = ' '.join(args)
        await member.ban()
        await ctx.send("{} got banned, reason: `{}`".format(member.mention, mesg))
    except:
        await member.kick()
        await ctx.send(f"{member.mention} got banned, reason: `None`")
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have `administrator permissions`")

@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Please specify a member")
        return
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.add_roles(role)
    await ctx.send('Member muted! https://gph.is/2bDfI0R')
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to mute people")

@client.command()
async def pfp(ctx, member: discord.Member=None):
    if member is None:
        try:
            await ctx.send("Server PFP: {}".format(ctx.guild.icon_url))
        except:
            await ctx.send("Error.. Please try again later..")
    else:
        try:
            await ctx.send("PFP Found: {}".format(member.avatar_url))
        except:
            await ctx.send("Error.. Please try again later..")

@client.command(aliases=['usd->btc', 'usd-btc', 'usdtobtc', 'usd btc'])
async def usdbtc(ctx, price0:int=None):
    if price0 is None:
        await ctx.send("Please add a value")
    else:
        sess = requests.Session()
        get = sess.get('https://blockchain.info/ticker')
        price2 = int(get.json()['USD']['last'])
        price1 = price2/price0
        try:
            await ctx.send("USD({}) -> BTC({})".format(price0, price1))
        except:
            await ctx.send("Error.. Please try again..")

@client.command(aliases=['btc->usd', 'btc-usd', 'btctousd', 'btc usd'])
async def btcusd(ctx, price0:int=None):
    if price0 is None:
        await ctx.send("Please add a value")
    else:
        sess = requests.Session()
        get = sess.get('https://blockchain.info/ticker')
        price2 = int(get.json()['USD']['last'])
        price1 = price0*price2
        try:
            await ctx.send("BTC({}) -> USD({})".format(price0, price1))
        except:
            await ctx.send("Error.. Please try again..")

@client.command()
async def btc(ctx):
    sess = requests.Session()
    price0 = sess.get('https://blockchain.info/ticker')
    price = int(price0.json()['USD']['last'])
    price1 = 1*price
    try:
        await ctx.send("Bitcoin Price: {}".format(price1))
    except:
        await ctx.send("Error.. Please try again..")
@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Please specify a member")
        return
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.remove_roles(role)
    await ctx.send('Member unmuted!')

@mute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to unmute people")

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    if "@everyone" or "@here"in mesg:
        await ctx.send("<@!{}> go ping ur mother not whole server :|".format(ctx.author.id))
    else:
        await ctx.send(mesg)


@client.command()
async def stop(ctx):
    if ctx.author.id == int(owner):
        await ctx.send("Closing in 2 seconds")
        time.sleep(2)
        sys.exit()
    else:
        await ctx.send("You don't have perms to do that")

@client.command(pass_context = True)
async def embed(ctx, *args):
    mesg = ' '.join(args)
    if "@everyone" or "@here"in mesg:
        await ctx.send("<@!{}> go ping ur mother not whole server :|".format(ctx.author.id))
    else:
        embed = discord.Embed(description=mesg, color=0x50bdfe)
        await ctx.send(embed=embed)    

@client.command(aliases=['8ball'])
async def ballpoll(ctx, *args):
    mesg = ' '.join(args)
    if "@everyone" or "@here"in mesg:
        await ctx.send("<@!{}> go ping ur mother not whole server :|".format(ctx.author.id))
    else:
        embed = discord.Embed(description="Question: {}\nResponse: {}".format(mesg, random.choice(ballpoll_responses)), color=0x50bdfe)
        await ctx.send(embed=embed)   

@client.command(aliases=['nickname', 'rename', 'newname'])
@commands.has_permissions(administrator=True)
async def nick(ctx, *, new: str=None):
    if new is None:
        await ctx.send(f"Usage: {ctx.prefix}nick <new name>")
    elif len(new) < 1:
        await ctx.send("Name need to have atleast 1 characters")
    else:
        try:
            await ctx.author.edit(nick=new)
            await ctx.send("Changed <@!{}> nickname to: {}".format(ctx.author.id, new))
        except:
            await ctx.send("Exception in code..")

# By editing next lines you disagree license, if you get caught you have to pay 
# start
@client.command(aliases=['_author', 'creator'])
async def author(ctx):
    await ctx.send("Bot Author: `ExtremeDev#1023`\nID: 455786583681925160")

@client.command(aliases=['sourcecode', 'src'])
async def source(ctx):
    await ctx.send("Source Code: https://github.com/ExtremeDude-tech/")

@client.command(aliases=['amowner', 'iamowner', 'Imowner?'])
async def amiowner(ctx):
    if ctx.author.id == 455786583681925160:
        await ctx.send("Well you are the coder of this bot..")
    elif ctx.author.id == int(owner):
        await ctx.send("You are the owner of the bot")
    else:
        await ctx.send("You are not..")
# end


@client.command()
async def coinflip(ctx):
    questions = ['head', 'tails']
    response = random.choice(questions)
    try:
        if response == 'head':
            await ctx.send("HEAD")
        else:
            await ctx.send("TAILS")
    except:
        await ctx.send("Error.. Try Again Later..")

try:
    client.run(str(bot_token), bot=True)
except Exception as e:
    print("Invalid token..\n\nException: {}\n\nToken: {}".format(e, bot_token))
    input()
    sys.exit()
