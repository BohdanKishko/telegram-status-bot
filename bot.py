from telethon import TelegramClient, events
from telethon.tl.types import UserStatusOnline, UserStatusOffline

api_id = 'YOUR_API_ID' # Вставь свой api_id
api_hash = 'YOUR_API_HASH' # Вставь свой api_hash
bot_token = 'YOUR_BOT_TOKEN' # Вставь свой bot_token
chat_id = YOUR_CHAT_ID # Встав ь свой Telegram ID

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

user_statuses = {}

async def get_user_name(user_id):
 user = await client.get_entity(user_id)
 return user.first_name or "Unknown"

@client.on(events.UserUpdate)
async def handler(event):
 user_id = event.user_id
 if user_id == 12345678: # Замени на ID отслеживаемого пользователя
 user_name = await get_user_name(user_id)
 if isinstance(event.status, UserStatusOnline):
 if user_id not in user_statuses or not isinstance(user_statuses[user_id], UserStatusOnline):
 await client.send_message(chat_id, f"{user_name} теперь в сети! 🟢")
 elif isinstance(event.status, UserStatusOffline):
 if user_id not in user_statuses or not isinstance(user_statuses[user_id], UserStatusOffline):
 await client.send_message(chat_id, f"{user_name} вышел из сети. 🔴")
 user_statuses[user_id] = event.status

client.start()
client.run_until_disconnected()
