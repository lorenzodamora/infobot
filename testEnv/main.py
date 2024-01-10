from pyrogram import Client
import os

# crea accanto a main.py il file myClientParameters.py con dentro queste tre variabili, io l'ho messo in .gitignore
from clientParameters import t_id, t_hash, t_token
'''
t_id = "id numerico"
t_hash = "hash alfanumerico"
t_token = "token ottenuto con botFather"
'''

plugins = dict(root="plugins")

my_id = 649363031
channel_id = -1002054102325

# Crea il file se non esiste
if not os.path.exists("../database/allUser.csv"):
    with open("../database/allUser.csv", 'w') as au:
        au.write("user_id;first_name;tag;datetime\n")
        au.close()
if not os.path.exists("../database/linkClick.txt"):
    with open("../database/linkClick.txt", 'w') as flc:
        flc.write("form:0\nwa mio:0\nig mio:0\nig giorgio trabaldo:0\nig matteo bianco:0\nig mauro boccomino:0\n"
                  "ig andrea traina:0\nig matteo depretis:0\nig dylan dagani:0\nig marco manenti:0\n"
                  "ig manuel mazzola:0\nig brandon zanchi:0\nmy webinar ita:0\nmy webinar eng:0\nwebinar bianco:0\n"
                  "ig bianco from webinar bianco:0\ntt bianco from webinar bianco:0\n")
        flc.close()

bot = Client(
    name="my_infobot",
    api_id=t_id,
    api_hash=t_hash,
    bot_token=t_token,
    plugins=plugins
)

with bot:
    # app.send_message(chat_id=my_id, text="Ready")
    try:
        bot.edit_message_text(chat_id=channel_id, message_id=2, text="ℹ️ BOT STATUS:\n\n    🟢 Online")
    except Exception as e:
        print("probabilmente il messaggio era già settato su \"online\"")
    finally:
        print("READY")

try:
    bot.run()
finally:
    bot.start()
    bot.edit_message_text(chat_id=channel_id, message_id=2, text="ℹ️ BOT STATUS:\n\n    🔴 Offline")
    from time import sleep
    sleep(1)
    bot.stop()
