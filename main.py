import uuid
import discord
from settings import *

client = discord.Client()

@client.event
async def on_ready():
    print("\nBot is operational as {0.user}".format(client))

@client.event
async def on_message(message):
    embeds = message.embeds
    embed_message = ""

    for embed in embeds:
        embed_message += str(embed.to_dict())

    if words_to_scan in embed_message and message.author!=client.user:
        print(embed_message)
        embed_message = embed_message.split("'description': ",1)[1]
        embed_message = embed_message.split("'title'",1)[0]
        channel = client.get_channel(NowPlayingChannelID)

        if message.author.id == HypeBotID:
            embed = discord.Embed(title = words_to_scan,
                                description = embed_message[:-3],
                                color = 0xd96c00)
            embed.set_author(name="Rave-Stadium")
            embed.set_thumbnail(url=img_url)
            embed.set_footer(text = "Concave Co-op - The world's best kept secret.", icon_url = img_url)

        elif message.author.id == VibesBotID:
            embed = discord.Embed(title = words_to_scan,
                                description = embed_message[:-3],
                                color = 0x04d900)
            embed.set_author(name="Cave-Stadium")
            embed.set_thumbnail(url=img_url)
            embed.set_footer(text = "Concave Co-op - The world's best kept secret.", icon_url = img_url)
            print("Embed two : ", embed)
            
        await channel.send(embed=embed)
        

client.run(discordBotToken)