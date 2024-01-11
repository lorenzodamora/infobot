import sys

sys.path.append('/home/ubuntu/Magnus/PycharmProj/infobot/python/python3.12/site-packages')

# Ora puoi importare i moduli Pyrogram e TgCrypto

# Resto del tuo script...


from pyrogram import Client
from myClientParameters import t_id, t_hash, t_token, pushbullet_API_KEY as pushKey
from plugins.myParameters import channel_id
from pushbullet import Pushbullet
plugins = dict(root="plugins")
bot = Client(
    name="my_infobot",
    api_id=t_id,
    api_hash=t_hash,
    bot_token=t_token,
)
bot.start()
bot.edit_message_text(chat_id=channel_id, message_id=2, text="ℹ️ BOT STATUS:\n\n    🔴 Offline")
bot.stop()
Pushbullet(pushKey).push_note("Infobot", "Stop")
