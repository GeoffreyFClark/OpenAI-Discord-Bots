## In this Repository:
- OpenAI Discord Chatbot template <br>
- Image-generating OpenAI Discord bot template <br>
- Training dataset sample of formatted web-scraped comments from Reddit's r/jokes <br>
- OpenAI Discord Chatbot w/ basic reinforcement implementation via logprobs <br>

## Follow these steps to easily create your own OpenAI Discord bot:

1. Create a Discord Application:<br>
• Go to the Discord Developer Portal: https://discord.com/developers/applications.<br>
• Click on "New Application" and fill out the basic information, such as the application name and icon.<br>

2. Set Up the Bot:</br>
• In the application's side panel, select the "Bot" tab.<br>
• Choose your desired bot settings and click on "Add Bot."<br>
• Save the Discord Token generated for your bot, as you will need it later.<br>

3. Authorize the Bot:</br>
• In the side panel, select the "OAuth2" tab followed by "URL Generator."<br>
• In the "Scopes" section, select "bot."<br>
• In the "Bot Permissions" section, choose the permissions you want to grant to your bot.<br>
• Use the generated URL to add the bot to your Discord servers.<br>

4. Obtain an OpenAI API Key:<br>
• Visit the OpenAI API Keys page: https://platform.openai.com/account/api-keys.<br>
• Create a new secret API key and save it, as you will need it later.<br>

5. Configure the Bot:<br>
• Clone or download the template from this repository.<br>
• Install dependencies, e.g., the `openai` and `discord` libraries, using the following command: `pip install openai discord`<br>
• Choose an OpenAI model/engine to use with your bot. You can either select one from the [OpenAI Models page](https://platform.openai.com/docs/models) (e.g. "text-davinci-002") or reference the [OpenAI API documentation](https://platform.openai.com/docs/api-reference) to fine-tune/train your own model using your own dataset.<br>
• Input the Discord Token, OpenAI API key, and model/engine into the appropriate fields in the template.<br>

Congratulations! You have successfully created your own OpenAI Discord bot. Run the Python script to bring your bot online, and enjoy interacting with your AI-powered bot on Discord!

## Sample Screenshots of the bots in action:
![image](https://user-images.githubusercontent.com/97141856/232136077-f46d58f5-2543-42e2-b563-2bb3bc3721f3.png)<br>
![image](https://user-images.githubusercontent.com/97141856/235572349-cdb30669-8730-4c13-9e99-6288920c90c5.png)<br>
![image](https://user-images.githubusercontent.com/97141856/235577458-8441ff0c-0eaf-4ff5-89f4-7b7451e4bad8.png)<br>
![image](https://user-images.githubusercontent.com/97141856/235574791-a071a70d-7ced-4d08-a23b-d12f8ca18f6d.png) ![image](https://user-images.githubusercontent.com/97141856/232142257-338d62fe-2e99-40e9-ae92-9ee6932b45f6.png)<br>
![image](https://user-images.githubusercontent.com/97141856/235583094-7b6f43c4-9a26-4829-b93d-efae02b507df.png)<br>
![image](https://user-images.githubusercontent.com/97141856/232173908-812449e1-1b7a-48e0-b02a-8392ef97b5db.png)<br>
![image](https://user-images.githubusercontent.com/97141856/235572603-82dadf61-421c-4654-bc5f-9e1376a8f02e.png)<br>
![image](https://user-images.githubusercontent.com/97141856/232136475-e73a064b-1890-410e-9b84-1ae3ae82ff64.png)<br>
![image](https://user-images.githubusercontent.com/97141856/232136640-5f126203-4b2b-4b2b-b0e9-21bb631203f0.png) (image bot's attempt with words lol)<br> 

Reinforcement functionality test (Bot does not watch anime --> Bot does watch anime): 
![image](https://user-images.githubusercontent.com/97141856/228354274-85183eef-9703-4f58-bc7c-5ec33e56c006.png)
