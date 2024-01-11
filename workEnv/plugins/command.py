"""
questo file contiene i /comandi e i log
"""
from pyrogram import Client, filters as f
from pyrogram.types import Message as Msg, User
from .replykeyboard import lcheck as lc
from .log import complete_log as clog
from asyncio import create_task as ct
from .myParameters import channel_id, my_id


# Definisci una funzione per gestire il comando /start
@Client.on_message(f.command("start"), group=0)
async def start_command(client: Client, msg: Msg):
    """
    comando /start

    :param client:
    :type client: Client
    :param msg: messaggio contenente /start
    :type msg: Message
    """
    async def adduser(user: User):
        """
        funzione locale per controllare e aggiungere nuovi utenti

        :param user: istanza utente contenente le info necessarie per il log
        :type user: User
        """
        from .newuser import update_all_user as up
        from datetime import datetime as dt
        b = await up(user.id, user.first_name, f"@{user.username}" if user.username is not None else "@ None tag",
                     dt.now())
        if b[0]:
            text = f"id:{b[1]['user_id']}\nf name:{b[1]['first_name']}\ntag:{b[1]['tag']}"
            await client.send_message(chat_id=my_id, text=f"new user! \n{text}\n\n#newUser")
    # End local def
    # Invia il messaggio di risposta
    await client.send_message(
        chat_id=msg.chat.id,
        text="Ciao! Grazie per avermi acceso, ti stavo aspettando!\n\nquesto bot non è ancora pronto (w.i.p.)"
        if await lc(msg.from_user.id) else "eng text : c0\nwarning\nEnglish is not implemented yet\n"
                                           "\nthis bot is in w.i.p."
    )
    _ = ct(adduser(msg.from_user))
    _ = ct(clog(msg.from_user.id, "comando", f"id:{msg.id}\n\ttext:{msg.text}"))


@Client.on_message(f.command("h"), group=0)
@Client.on_message(f.command("?"), group=0)
@Client.on_message(f.command("help"), group=0)
async def help_command(_, msg: Msg):
    """
    comando /help

    :param _: Client, che al momento non serve
    :param msg: messaggio contenente /help
    :type msg: Message
    """
    await msg.reply_text(
        "clicca /start per accendermi\nOppure contatta il mio creatore @ill_Magnus" if await lc(msg.from_user.id)
        else f"eng text : c1"
    )
    _ = ct(clog(msg.from_user.id, "comando", f"id:{msg.id}\n\ttext:{msg.text}"))


filter_list = (
    f.command("h") | f.command("?") | f.command("help") | f.command("start") |
    f.regex(r"^Italiano$") | f.regex(r"^English$") | f.regex(r"^Other$") |
    f.regex(r"^Set Language 🌐$") | f.regex(r"^Imposta Lingua 🌐$") |
    f.regex(r"^🔙 Menù$") | f.regex(r"^Contatto 👤$") | f.regex(r"^Contact 👤$") |
    f.regex(r"^Form$") | f.regex(r"^❔ FAQ / Q&A ❓$") | f.regex(r"^FAQ$") | f.regex(r"^Q&A$") |
    f.regex(r"^🎦 Info & Video ℹ️$") |
    f.regex(r"^Guarda il Webinar$") | f.regex(r"^🇮🇹Webinar di Matteo Bianco$") | f.regex(r"^🇮🇹Matteo Bianco's Webinar$")
    | f.regex(r"^Il mio webinar Eng$") | f.regex(r"^My webinar Eng$") |
    f.regex(r"^Il mio webinar Ita$") | f.regex(r"^My webinar Ita$") |
    f.regex(r"^WorkShop$") | f.regex(r"^gio&gia, lungo e completo$") |
    f.regex(r"^Perché mi chiede il numero di telefono?$") | f.regex(r"^Dati sensibili$") |
    f.regex(r"^Quanto vale tutto questo?$") | f.regex(r"^Altre Info$") | f.regex(r"^Other Info$")
)
"""
lista di filtri che hanno già un altra funzione associata
"""


@Client.on_message(~filter_list)
async def log_msg(_, msg: Msg):
    """
    manda il log del messaggio non valido

    :param _: Client, che al momento non serve
    :param msg:
    :type msg: Message
    """
    await msg.reply_text(
        "Comando non valido\nprova /start" if await lc(msg.from_user.id) else f"eng text : c2"
    )
    _ = ct(clog(msg.from_user.id, "messaggio non valido", f"id:{msg.id}\n\ttext:{msg.text}"))


@Client.on_message(f.chat(channel_id), group=-1)
async def msg_channel(_, msg):
    """
    se il canale manda un messaggio ignoralo

    :param _: Client, che al momento non serve
    :param msg:
    :type msg: Message
    """
    _ = ct(clog(channel_id, "noreply channel", f"id:{msg.id}\n\ttext:{msg.text}"))
    msg.stop_propagation()


@Client.on_message(f.chat(my_id), group=-1)
async def msg_my(_, msg):
    """
    se io mando un messaggio ignoralo

    :param _: Client, che al momento non serve
    :param msg:
    :type msg: Message
    """
    _ = ct(clog(my_id, "noreply self", f"id:{msg.id}\n\ttext:{msg.text}"))
    msg.stop_propagation()


@Client.on_edited_message()
async def on_edited_message(_, msg):
    _ = ct(clog(msg.chat.id, "messaggio modificato", f"id:{msg.id}\n\ttext:{msg.text}"))
