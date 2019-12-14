import discord
import random
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_role

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Bot is ready.')


@client.event
async def on_member_join(member):
    print(f'{member} has joined the network')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the network')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')


@client.command()
async def annon(ctx, member, x, *, message='are you alive!'):
    for y in range(int(x)):
        await ctx.send(f'{member} {message}')


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely",
                 "You may rely on it", "As I see it, yes", "Most Likely", "Outlook Good",
                 "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
                 "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
                 "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command()
@commands.has_role('GOD')
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)



client.run('NjU1NDI0MDQwMjU2OTI5ODAy.XfT5rQ.9Zks7ycKnN0AVy9CsRQHDupSnO0')
