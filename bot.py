import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} kimi sistemə daxil olduq!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!salam'):
        await message.channel.send('Aleykum salam, qardaş!')

# Botun tokenini bura yazacağıq
client.run("SƏNİN_BOT_TOKENİN")
