# Telegram bot for shop
## Изменить язык: [Русский](README.md)
***
Telegram bot for providing information about the company and accepting applications.
## [LIVE](https://t.me/outfit_item_bot)
## [DEMO](README.demo.md)
## Functionality:
1. Provides information on various aspects of the company's activities
2. Contains links to social networks and contacts
3. Accepts applications according to the scenario, depending on the responses of users
4. Notifies managers about abandoned applications
5. Controls the presence of a username in telegram
## Installation and use:
- Install dependencies:
```sh
pip install -r requirements.txt
```
- specify in the .env file:
   - Bot telegram token: **TELEGRAM_TOKEN**=TOKEN
   - Bot ID: **BOT_ID**=ID (first digits from bot token, before :)
   - Manager ID: **MANAGER_ID**=MANAGER_ID; will have the right to execute the /update command, he will receive notifications - to receive notifications, the manager needs to activate the bot from his account (press the "start" button)
   > To determine the user ID, you need to send any message from the corresponding account to the next [bot] (https://t.me/getmyid_bot). Value contained in **Your user ID** - User ID
- set the following variables in the config.py file:\
**MANAGER_USERNAME**=example (specified without @) - manager's nickname\
**INSTAGRAM** - link to instagram\
**WEB_URL** - link to the site\
**TELEGRAM_CHANNEL** - link to telegram channel\
**WHATSAPP** - link to whatsapp profile\
**REVIEWS_IMAGE** - id of the image displayed when going to the reviews section, or a link to it\
**INSTRUCTION_IMAGE** - instruction image id or a link to it
- run the project:
```sh
python3 main.py
```