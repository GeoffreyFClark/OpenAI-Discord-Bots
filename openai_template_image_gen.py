import discord
import requests
import json

api_key = "OPEN AI API KEY HERE"  # Obtain from openAI platform

# Discord bot setup
client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.content.startswith('!generate_image'):
        prompt = message.content[15:]
        # Make a request to the DALL·E API
        response = requests.post(
            "https://api.openai.com/v1/images/generations",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            },
            data=json.dumps({
                "model": "image-alpha-001",
                "prompt": prompt,
                "num_images": 1,
                "size": "1024x1024",
                "response_format": "url"
            })
        )
        # Check if the request was successful
        if response.status_code == 200:
            image_url = response.json()["data"][0]["url"]
            # Send the generated image in the Discord channel
            await message.channel.send(image_url)
        else:
            await message.channel.send("Failed to generate image. Please try again later.")

client.run("DISCORD BOT TOKEN HERE")  # Obtain from Discord Developer Portal
