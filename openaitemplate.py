import discord
import openai

openai.api_key = ""  # Input OpenAI Key here in quotes as a string
discord_token = "DISCORD TOKEN HERE"  # Input Discord Token here
model_name = "ENGINE MODEL NAME HERE"  # Input Engine Model Name here 

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
            engine=model_name,  
            prompt=prompt,
            max_tokens=80,
            n=1,
            temperature=0.5,
            stop=["\n"]
        )
        generated_text = response["choices"][0]["text"]

        await message.channel.send(f'{generated_text}')

client.run(discord_token)  
