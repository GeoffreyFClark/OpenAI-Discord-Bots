import discord
import openai

api_key = "OPENAI API KEY HERE"

# Discord bot setup
intents = discord.Intents().all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.content.startswith('%'):
        prompt = message.content[1:]
        # Make a request to the DALL·E API
        try:
            response = openai.Image.create(
                model="image-alpha-001",
                prompt=prompt,
                num_images=1,
                size="512x512",
                response_format="url"
            )
            image_url = response['data'][0]['url']
            # Send the generated image in the Discord channel
            file = discord.File(io.BytesIO(requests.get(image_url).content), filename="image.jpg")
            await message.channel.send(file=file)
        except (requests.exceptions.RequestException, json.JSONDecodeError, openai.error.OpenAIError) as e:
            print(e)
            await message.channel.send("Failed to generate image. Please try again later.")

client.run("DISCORD BOT TOKEN HERE")
