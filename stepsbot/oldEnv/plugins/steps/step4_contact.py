"""
questo file contiene un momento feedback

step 4
"""
from pyrogram.types import Message as Msg


async def step4(msg: Msg):
    """
    :param msg: Messaggio che ha lanciato l'evento
    :type msg: Message
    """
    from pyrogram.types import ReplyKeyboardMarkup as Rkm
    from ..lang import lc
    id_ = msg.chat.id
    await msg.reply(
        text="Ti meriti un piccolo break!\n"
             "Dopo aver visto il video sarai pieno di domande, oppure semplicemente sei stanco "
             "di ricevere tutte queste informazioni nuove.\n In ogni caso, contattami e dimmi cosa ti è "
             "piaciuto o ti è interessato di più del video che hai appena visto!\n"
             "Mi farebbe molto piacere parlare con te!"
        if await lc(id_) else "eng text : 4.1",
        reply_markup=Rkm(
            keyboard=[
                [
                    "Contatto 👤" if await lc(id_) else "Contact 👤",  # A!
                ],
            ],
            one_time_keyboard=False,
            resize_keyboard=True
        )
    )
    # handler invia il messaggio di contatto dopo 1 secondo

    # def continua
    from ..myParameters import MY_ID
    if id_ != MY_ID:
        from asyncio import sleep
        await sleep(60 * 10)  # 10 min di attesa
    else:
        from asyncio import sleep
        await sleep(3.5)

    try:
        await msg.reply(
            text="Scrivi qua il messaggio che ti ha rivelato @Ill_Magnus" if await lc(id_) else "eng text : 4.2",
            reply_markup=Rkm(
                keyboard=[
                    [
                        "Contatto 👤" if await lc(id_) else "Contact 👤",  # B1
                    ],
                ],
                one_time_keyboard=False,
                resize_keyboard=True
            )
        )
    except Exception as e:
        print(f"file: step_contact.py | funzione: continua | errore in msg.reply\n\nmsg:\n{vars(msg)}\n\n\n{vars(e)}")
