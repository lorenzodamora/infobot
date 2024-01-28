"""
questo file contiene i comandi /start e /help

step 1
"""
from pyrogram import Client
from pyrogram.types import Message as Msg
from ..lang import lc


async def start_command(client: Client, msg: Msg, my_id: int):
    """
    comando /start, manda la tab delle linugue

    :param client:
    :type client: Client
    :param msg: messaggio contenente /start
    :type msg: Message
    :param my_id:
    :type my_id: int
    """
    from pyrogram.types import User
    from asyncio import create_task as ct

    async def adduser(user: User):
        """
        funzione locale per controllare e aggiungere nuovi utenti

        :param user: istanza utente contenente le info necessarie per il log
        :type user: User
        """
        from ..newuser import update_all_user as up
        b = await up(user.id, user.first_name, f"@{user.username}" if user.username is not None else '@ None tag')
        if b[0]:
            from pyrogram.enums import ParseMode
            text = f"id:{b[1]['user_id']}\nf name:{b[1]['first_name']}\ntag:{b[1]['tag']}"
            await client.send_message(chat_id=my_id, text=f"new user! \n{text}\n\n#newUser",
                                      parse_mode=ParseMode.DISABLED)
    # End local def
    # Invia il messaggio di risposta
    await client.send_message(
        chat_id=msg.chat.id,
        text="🇮🇹🇮🇹 Ciao! Grazie per avermi acceso, ti stavo aspettando! 🇮🇹🇮🇹\n"
             "Questo bot ti guiderà passo-passo per darti tutte le informazioni che cerchi!\n"
             "Oppure puoi chiedere direttamente a @Ill_Magnus se preferisci"
             "\n\nquesto bot non è ancora pronto (w.i.p.)"
    )
    await client.send_message(
        chat_id=msg.chat.id,
        text="🇬🇧🇬🇧 Hi! Thanks you for Power-On me! I'm waiting for you! 🇬🇧🇬🇧\n"  # eng text : 1.1
             "warning\nEnglish is not implemented yet\n\nthis bot is in w.i.p."
    )
    _ = ct(adduser(msg.from_user))


async def help_command(msg: Msg):
    """
    comando /help

    :param msg: messaggio contenente /help
    :type msg: Message
    """
    await msg.reply_text(
        "clicca /start per accendermi\nOppure contatta il mio creatore @ill_Magnus" if await lc(msg.from_user.id)
        else f"eng text : 1.2"
    )
