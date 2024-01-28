"""
questo file contiene i comandi /start e /help

step 1
"""
from pyrogram import Client
from pyrogram.types import Message as Msg, User
from asyncio import create_task as ct


async def start_command(client: Client, msg: Msg, my_id: int):
    """comando /start, manda la tab delle lingue"""

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
    await client.send_message(
        chat_id=msg.chat.id,
        text="🇮🇹🇮🇹 Ciao! Grazie per avermi acceso, ti stavo aspettando!\n"
    )
    await client.send_message(
        chat_id=msg.chat.id,
        text="🇬🇧🇬🇧 Hi! Thanks you for Power-On me! I'm waiting for you!\n"
    )
    _ = ct(adduser(msg.from_user))


async def help_command(msg: Msg):
    from ..lang import lc
    await msg.reply_text(
        "clicca /start per accendermi\nOppure contatta il mio creatore @Ill_Magnus" if await lc(msg.chat.id) else
        "Click /start to turn me on.\nOr contact my creator @Ill_Magnus."
    )
