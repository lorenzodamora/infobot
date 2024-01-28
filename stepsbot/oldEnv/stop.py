from pyrogram import Client
from myClientParameters import t_id, t_hash, t_token, pushbullet_API_KEY as pushKey
from plugins.myParameters import my_id
from pushbullet import Pushbullet
plugins = dict(root="plugins")
title = "StepsBot"
bot = Client(
    name=title,
    api_id=t_id,
    api_hash=t_hash,
    bot_token=t_token,
)
bot.start()
# bot.edit_message_text(chat_id=channel_id, message_id=2, text="ℹ️ BOT STATUS:\n\n    🔴 Offline")
bot.send_message(chat_id=my_id, text="Stop")
bot.stop()
Pushbullet(pushKey).push_note(title, "Stop")
