from pyrogram import Client, idle
from os.path import exists

# crea accanto a main.py il file myClientParameters.py con dentro queste tre variabili, io l'ho messo in .gitignore
from myClientParameters import t_id, t_hash, t_token, pushbullet_API_KEY as pushKey
from plugins.myParameters import CHANNEL_ID
from pushbullet import Pushbullet
'''
t_id = "id numerico"
t_hash = "hash alfanumerico"
t_token = "token ottenuto con botFather"
'''

# Crea il file se non esiste
if not exists("../database/allUser.csv"):
    open("../database/allUser.csv", 'w').write("user_id;first_name;tag;datetime\n")

pb = Pushbullet(pushKey)
plugins = dict(root="plugins")
title = "MazzoBot"


async def main():
    bot = Client(
        name=title,
        api_id=t_id,
        api_hash=t_hash,
        bot_token=t_token,
        plugins=plugins
    )

    await bot.start()

    # await bot.send_message(chat_id=MY_ID, text="Ready")
    try:
        await bot.edit_message_text(chat_id=CHANNEL_ID, message_id=2, text="ℹ️ BOT STATUS:\n\n    🟢 Online")
    except:
        print("probabilmente il messaggio era già settato su \"online\"")
    pb.push_note(title, "Ready")
    # print("READY")
    await idle()

    pb.push_note(title, "Stop")
    try:
        await bot.edit_message_text(chat_id=CHANNEL_ID, message_id=2, text="ℹ️ BOT STATUS:\n\n    🔴 Offline")
    except:
        print("probabilmente il messaggio era già settato su \"offline\"")
    # await bot.send_message(chat_id=MY_ID, text="Stop")
    # await bot.stop()
    # print("Stop")

if __name__ == "__main__":
    import uvloop
    uvloop.install()
    from platform import python_version_tuple
    if python_version_tuple() >= ("3", "11"):
        from asyncio import Runner
        with Runner() as runner:
            runner.get_loop().run_until_complete(main())
    else:
        from asyncio import new_event_loop
        loop = new_event_loop()
        loop.run_until_complete(main())
