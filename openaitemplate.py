import discord
import openai

openai.api_key = "OPEN AI API KEY HERE"  # Obtain from openAI platform

intents = discord.Intents().all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'SUCCESSFULLY logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!'):
        prompt = message.content[1:]
        response = openai.Completion.create(  # See API documentation for further parameters
            engine="",  # Select a base model or your own model here
            prompt=prompt,
            max_tokens=80,
            n=1,
            temperature=0.5,
        )
        generated_text = response["choices"][0]["text"]

        # Add further logic here to manipulate string responses if required.

        await message.channel.send(f'{generated_text}')

client.run("DISCORD BOT TOKEN HERE")  # Obtain from Discord Developer Portal


# To fine tune your own model using openAI's API, see https://platform.openai.com/docs/guides/fine-tuning
