from pyrogram import Client, idle
from os.path import exists
# crea accanto a mMain.py il file myClientParameters.py con dentro queste tre variabili, io l'ho messo in .gitignore
from myClientParameters import t_id, t_hash, t_token, pushbullet_API_KEY as pushKey
from myplugins.myParameters import MY_ID, CHANNEL_ID, HEADER_ALLUSER, ALLUSER_PATH
from pushbullet import Pushbullet

'''
t_id = "id numerico"
t_hash = "hash alfanumerico"
t_token = "token ottenuto con botFather"
'''

# Crea il file se non esiste
if not exists(ALLUSER_PATH):
    open(ALLUSER_PATH, 'w').write(f"{HEADER_ALLUSER}\n")

pb = Pushbullet(pushKey)
plugins_path = dict(root="myplugins")
title = "MazzoBot"


async def main(dev=False):
    from os import environ
    from pyrogram.errors.exceptions.bad_request_400 import MessageNotModified
    if dev:
        environ['dev'] = '1'
    else:
        environ['dev'] = '0'

    # Leggi la variabile d'ambiente e convertila in booleano (numerico)
    # is_dev = os.getenv("dev", "0").lower() == "1"

    bot = Client(
        name=title,
        api_id=t_id,
        api_hash=t_hash,
        bot_token=t_token,
        plugins=plugins_path
    )

    await bot.start()

    if not dev:
        try:
            await bot.edit_message_text(CHANNEL_ID, message_id=2, text="ℹ️ BOT STATUS:\n\n    🟢 Online")
        except MessageNotModified:
            print("raise MessageNotModified: probabilmente il messaggio era già settato su \"online\"")
        pb.push_note(title, "Ready")

    else:
        await bot.send_message(MY_ID, "Ready")
        print("READY")

    await idle()

    if not dev:
        pb.push_note(title, "Stop")
        try:
            await bot.edit_message_text(CHANNEL_ID, message_id=2, text="ℹ️ BOT STATUS:\n\n    🔴 Offline")
        except MessageNotModified:
            print("raise MessageNotModified: probabilmente il messaggio era già settato su \"offline\"")
    else:
        await bot.send_message(MY_ID, "Stop")
        print("STOP")


if __name__ == "__main__":
    from sys import argv, exit

    if len(argv) > 2:
        print("Usage: python3 -u mMain.py [<parameter>]")
        exit(1)
    parameter = False
    if len(argv) == 2:
        if argv[1] == "dev":
            parameter = True
            print('dev on')
        else:
            print("parameters:\n\t[no parameter]\n\tdev")
            exit(1)

    from platform import python_version_tuple, system

    if system() == "Linux":
        import uvloop

        uvloop.install()

    if python_version_tuple() >= ("3", "11"):
        from asyncio import Runner

        with Runner() as runner:
            runner.get_loop().run_until_complete(main(parameter))
            
    else:
        from asyncio import new_event_loop

        loop = new_event_loop()
        loop.run_until_complete(main(parameter))
