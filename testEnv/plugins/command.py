from pyrogram import Client, filters as f
from .replykeyboard import lcheck as lc
from .log import async_log as alog
from asyncio import create_task as ct

channel_id = -1002054102325
my_id = 649363031


async def adduser(user, client):
    from .newuser import update_all_user as up
    from datetime import datetime as dt
    b = await up(user.id, user.first_name, f"@{user.username}" if user.username is not None else "@ None tag", dt.now())
    if b[0]:
        text = f"id:{b[1]['user_id']}\nf name:{b[1]['first_name']}\ntag:{b[1]['tag']}"
        await client.send_message(chat_id=my_id, text=f"new user! \n{text}\n\n#newUser")


# Definisci una funzione per gestire il comando /start
@Client.on_message(f.command("start"), group=0)
async def start_command(client, msg):
    # Invia il messaggio di risposta
    await client.send_message(
        chat_id=msg.chat.id,
        text="Ciao! Grazie per avermi acceso, ti stavo aspettando!\n\nquesto bot non è ancora pronto (w.i.p.)"
        if lc(msg.from_user.id) else "eng text : c0\nwarning\nEnglish is not implemented yet\n\nthis bot is in w.i.p."
    )
    _ = ct(adduser(msg.from_user, client))
    alog(msg.from_user.id, "comando", f"id:{msg.id}\n\ttext:{msg.text}")


@Client.on_message(f.command("h"), group=0)
@Client.on_message(f.command("?"), group=0)
@Client.on_message(f.command("help"), group=0)
async def help_command(_, msg):
    text = "clicca /start per accendermi\nOppure contatta il mio creatore @ill_Magnus" if lc(msg.from_user.id)\
        else f"eng text : c1"
    await msg.reply_text(text)
    alog(msg.from_user.id, "comando", f"id:{msg.id}\n\ttext:{msg.text}")


filter_list = (
    f.command("h") | f.command("?") | f.command("help") | f.command("start") |
    f.regex("Italiano") | f.regex("English") | f.regex("Other") |
    f.regex("Set Language 🌐") | f.regex("Imposta Lingua 🌐") |
    f.regex("🔙 Menù") | f.regex("Contatto 👤") | f.regex("Contact 👤") |
    f.regex("Form") | f.regex("❔ FAQ / Q&A ❓") | f.regex("FAQ") | f.regex("Q&A") |
    f.regex("🎦 Info & Video ℹ️") | f.regex("WorkShop") |
    f.regex("Guarda il Webinar") | f.regex("🇮🇹Webinar di Matteo Bianco") | f.regex("🇮🇹Matteo Bianco's Webinar") |
    f.regex("Il mio webinar Eng") | f.regex("My webinar Eng") |
    f.regex("Il mio webinar Ita") | f.regex("My webinar Ita") |
    f.regex("Perché mi chiede il numero di telefono?") | f.regex("Dati sensibili") |
    f.regex("Quanto vale tutto questo?") | f.regex("Altre Info") | f.regex("Other Info")
)


@Client.on_message(~filter_list)
async def log(client, msg):
    await client.send_message(
        chat_id=msg.chat.id,
        text="Comando non valido\nprova /start" if lc(msg.from_user.id) else f"eng text : c2"
    )
    alog(msg.from_user.id, "messaggio non valido", f"id:{msg.id}\n\ttext:{msg.text}")


@Client.on_message(f.chat(channel_id), group=-1)
def msg_channel(_, msg):
    alog(channel_id, "noreply channel", f"id:{msg.id}\n\ttext:{msg.text}")
    msg.stop_propagation()


@Client.on_message(f.chat(my_id), group=-1)
def msg_my(_, msg):
    alog(my_id, "noreply self", f"id:{msg.id}\n\ttext:{msg.text}")
    msg.stop_propagation()


'''
# a quanto pare non funziona
@Client.on_user_status()
def on_user_status(_, user):
    from pyrogram.enums import UserStatus
    add_log(user.id, create_log_line(
        "user status",
        f"{"ONLINE" if user.status == UserStatus.ONLINE else "OFFLINE"}"
    ))
'''


'''
@Client.on_deleted_messages()
def on_deleted_messages(_, msg_list):
    if isinstance(msg_list, list):
        for msg in msg_list:
            #user_id = search_user(msg.id)
            add_log(user_id=0, messaggio=create_log_line(
                "messaggio eliminato ", f"id:{msg.id}"
            ))
            add_log(user_id=0, messaggio=create_log_line(
                "messaggi eliminati", f"id:{msg.id}\n\ttext:{msg.text}"
            ))
    else:
        add_log(msg_list.chat.id, create_log_line(
            "messaggio eliminato", f"id:{msg_list.id}\ntext:{msg_list.text}"
        ))
'''


@Client.on_edited_message()
def on_edited_message(_, msg):
    alog(msg.chat.id, "messaggio modificato", f"id:{msg.id}\n\ttext:{msg.text}")
