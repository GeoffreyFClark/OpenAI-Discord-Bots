## In this Repository:
- Image-generating OpenAI Discord bot (openai_template_image_gen.py) </br>
- OpenAI and Tensorflow Discord chatbot generic templates (openaitemplate.py) (tensorflowtemplate.py) </br>
- OpenAI Discord Chatbot w/ basic reinforcement implementation via logprobs: (reinforceable_chatbot.py) </br>
- A sample training dataset of formatted web-scraped comments from Reddit's r/jokes (RedditTrainingData.jsonl) </br>

## Follow these steps to easily create your own OpenAI Discord bot:

1. Create a Discord Application:</br>
• Go to the Discord Developer Portal: https://discord.com/developers/applications.</br>
• Click on "New Application" and fill out the basic information, such as the application name and icon.</br>

2. Set Up the Bot:</br>
• In the application's side panel, select the "Bot" tab.</br>
• Choose your desired bot settings and click on "Add Bot."</br>
• Save the Discord Token generated for your bot, as you will need it later.</br>

3. Authorize the Bot:</br>
• In the side panel, select the "OAuth2" tab.</br>
• In the "Scopes" section, select "bot."</br>
• In the "Bot Permissions" section, choose the permissions you want to grant to your bot.</br>
• Use the generated URL to add the bot to your Discord servers.</br>

4. Obtain an OpenAI API Key:</br>
• Visit the OpenAI API Keys page: https://platform.openai.com/account/api-keys.</br>
• Create a new secret API key and save it, as you will need it later.</br>

5. Configure the Bot:</br>
• Clone or download the template from this repository.</br>
• Install dependencies e.g. 'openai' and 'discord' libraries, using the following command: "pip install openai discord"</br>
• Choose an OpenAI model/engine to use with your bot. You can either select one from the [OpenAI Models page](https://platform.openai.com/docs/models) (e.g. "text-davinci-002") or reference the [OpenAI API documentation](https://platform.openai.com/docs/api-reference) to fine-tune/train your own model/engine using your own dataset.</br>
• Input the Discord Token, OpenAI API key, and model/engine into the appropriate fields in the template.</br>

6. Run the Bot:</br>
• Run the Python script to start your bot.</br>
• Once the bot is running, you can interact with it on your Discord servers.</br>

Congratulations! You have successfully created your own OpenAI Discord bot. Enjoy interacting with your AI-powered bot on Discord!

## Sample Screenshots of the bots in action:
![image](https://user-images.githubusercontent.com/97141856/232136077-f46d58f5-2543-42e2-b563-2bb3bc3721f3.png)</br>
![image](https://user-images.githubusercontent.com/97141856/232140360-30bcc745-58da-4002-a5f1-913482bb7c66.png)</br>
![image](https://user-images.githubusercontent.com/97141856/232141544-bcc695b9-05e5-40c9-8371-51585bb7ee91.png)
![image](https://user-images.githubusercontent.com/97141856/232142257-338d62fe-2e99-40e9-ae92-9ee6932b45f6.png)</br>
![image](https://user-images.githubusercontent.com/97141856/232173908-812449e1-1b7a-48e0-b02a-8392ef97b5db.png)</br>
![image](https://user-images.githubusercontent.com/97141856/232136475-e73a064b-1890-410e-9b84-1ae3ae82ff64.png)</br>
![image](https://user-images.githubusercontent.com/97141856/232136640-5f126203-4b2b-4b2b-b0e9-21bb631203f0.png)lol</br>

Reinforcement functionality test (Bot does not watch anime --> Bot does watch anime): 
![image](https://user-images.githubusercontent.com/97141856/228354274-85183eef-9703-4f58-bc7c-5ec33e56c006.png)
