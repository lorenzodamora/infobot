from pyrogram import Client
from myClientParameters import t_id, t_hash, t_token
from time import sleep
from myParameters import channel_id
plugins = dict(root="plugins")
bot = Client(
    name="my_infobot",
    api_id=t_id,
    api_hash=t_hash,
    bot_token=t_token,
    plugins=plugins
)

bot.start()
bot.edit_message_text(chat_id=channel_id, message_id=2, text="ℹ️ BOT STATUS:\n\n    🔴 Offline")
sleep(1)
bot.stop()
