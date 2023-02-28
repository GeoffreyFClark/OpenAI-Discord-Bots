import discord
import tensorflow as tf
import numpy as np

# Load the pre-trained model
model = tf.keras.models.load_model("model.h5")

# Function to generate answers
def generate_answer(input_text, model):
    input_seq = np.zeros((1, max_len), dtype=int)
    for i, word in enumerate(input_text.split()):
        if word in word_index:
            input_seq[0, i] = word_index[word]
    chat_response = model.predict(input_seq, verbose=0)[0]
    chat_response = np.argmax(chat_response)
    response = ''
    for word, index in word_index.items():
        if index == chat_response:
            response = word
            break
    return response

# Discord client
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!'):  
        input_text = message.content[1:]  
        response = generate_answer(input_text, model)
        await message.channel.send(response)

client.run("DISCORD BOT TOKEN HERE")  # Obtain from Discord Developer Portal
