from pyrogram import Client
from os.path import exists

# crea accanto a main.py il file myClientParameters.py con dentro queste tre variabili, io l'ho messo in .gitignore
from myClientParameters import t_id, t_hash, t_token, pushbullet_API_KEY as pushKey
from plugins.myParameters import channel_id
from pushbullet import Pushbullet
'''
t_id = "id numerico"
t_hash = "hash alfanumerico"
t_token = "token ottenuto con botFather"
'''

# Crea il file se non esiste
if not exists("../database/allUser.csv"):
    open("../database/allUser.csv", 'w').write("user_id;first_name;tag;datetime\r\n")
if not exists("../database/linkClick.txt"):
    open("../database/linkClick.txt", 'w').write("form:0\r\nwa mio:0\r\nig mio:0\r\n")

pb = Pushbullet(pushKey)
plugins = dict(root="plugins")
bot = Client(
    name="my_infobot",
    api_id=t_id,
    api_hash=t_hash,
    bot_token=t_token,
    plugins=plugins
)

with bot:
    try:
        bot.edit_message_text(chat_id=channel_id, message_id=2, text="ℹ️ BOT STATUS:\n\n    🟢 Online")
    except Exception as e:
        print("probabilmente il messaggio era già settato su \"online\"")
    finally:
        # print("READY")
        pb.push_note("Infobot", "Ready")

try:
    bot.run()
finally:
    # print("Stop")
    pb.push_note("Infobot", "Stop")
    bot.start()
    bot.edit_message_text(chat_id=channel_id, message_id=2, text="ℹ️ BOT STATUS:\n\n    🔴 Offline")
    bot.stop()
