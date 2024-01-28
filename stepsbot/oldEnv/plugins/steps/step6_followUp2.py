"""
questo file contiene un secondo momento feedback

step 6
"""
from pyrogram.types import Message as Msg


async def step6(msg: Msg):
    """
    :param msg: Messaggio che ha lanciato l'evento
    :type msg: Message
    """
    from pyrogram.types import ReplyKeyboardMarkup as Rkm
    from ..lang import lc
    id_ = msg.chat.id
    await msg.reply(
        text="Ti meriti un'altro piccolo break!\n"
             "Dopo aver visto questi altri due video sarai carico, oppure semplicemente incuriosito, e non vorrai "
             "sicuramente perdere tutte le risposte che cerchi.\n In ogni caso, contattami e dimmi cosa ti è "
             "piaciuto o ti è interessato di più di questi video che hai appena visto!\n"
             "Sono qui apposta per capire per quale motivo secondo te, tu dovresti diventare un mio collaboratore in "
             "questo grande progetto!"
        if await lc(id_) else "eng text : 6.1",
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
    # handler invia il messaggio di contatto dopo 3 secondi

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
            text="Per proseguire chiedi a @Ill_Magnus !" if await lc(id_) else "eng text : 6.2",
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
        print(f"file: step_followUp2.py | funzione: continua | errore in msg.reply\n\nmsg:\n{vars(msg)}\n\n\n{vars(e)}")
