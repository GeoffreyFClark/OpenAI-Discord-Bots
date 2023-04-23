import discord
import openai

# Note placeholders for OpenAI Key and Discord Token

openai.api_key = "OPENAI KEY HERE"  # Replace

intents = discord.Intents().all()
client = discord.Client(intents=intents)

responses = {}


@client.event
async def on_ready():
    print(f'SUCCESSFULLY logged in as {client.user}')

    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'bots.shutdown':  # replace with your custom command
        await message.channel.send('Shutting down...')
        await client.close()
    if message.content.startswith('!'):
        prompt = message.content[1:]
        response = openai.Completion.create(
            engine="davinci:ft-personal-2023-03-05-12-27-58",  # Replace my trained model with yours or a base model
            prompt=prompt + ' ->',
            max_tokens=100,
            n=1,
            temperature=0.8,
            stop=["\n"]
        )
        print(response["choices"][0]["text"])
        message_to_send = response["choices"][0]["text"]
        await message.channel.send(message_to_send)


@client.event
async def on_reaction_add(reaction, user):
    # Check if the reaction was to a message from the bot
    if reaction.message.author == client.user:
        # Check if the reaction is a thumbs-up or thumbs-down
        if str(reaction.emoji) == "👍" or str(reaction.emoji) == "👎":
            prompt = reaction.message.content
            response = openai.Completion.create(
                engine="davinci:ft-personal-2023-03-05-12-27-58",
                prompt=prompt,
                max_tokens=100,
                n=1,
                temperature=0.8,
                stop="\n",
                logprobs=10 # increase the number of logprobs to improve the accuracy of the reward signal
            )
            if len(response.choices) > 0:
                logprobs = response.choices[0].logprobs.token_logprobs
                reward = 1 if str(reaction.emoji) == "👍" else -1
                for i, token_logprobs in enumerate(logprobs):
                    token = response.choices[0].text[i]
                    if isinstance(token_logprobs, dict):
                        token_reward = token_logprobs[token]["token_logprob"] * reward
                        openai.Completion.create(
                            engine="davinci:ft-personal-2023-03-05-12-27-58",
                            prompt=prompt + token,
                            max_tokens=0,
                            n=1,
                            logprobs=10,
                            echo=True,
                            stop="\n",
                            temperature=0,
                            stop_sequence="\n",
                            presence_penalty=0.0,
                            frequency_penalty=0.0,
                            stop_penalty=0.0,
                            logit_bias={token: token_reward} # update the logit_bias with the reward signal
                        )
                if reward == 1:
                    await reaction.message.channel.send(f'{user} reinforced the response: "{prompt}"')
                else:
                    await reaction.message.channel.send(f'{user} penalized the response: "{prompt}"')


client.run("DISCORD TOKEN HERE")  # replace
