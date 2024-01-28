"""
questo file contiene il workshop gio&gia, fatto apposta per i genitori

step 7
"""
from pyrogram.types import Message as Msg, ReplyKeyboardMarkup as Rkm
from ..lang import lc


async def step7(msg: Msg):
    """
    :param msg: Messaggio che ha lanciato l'evento
    :type msg: Message
    """
    id_ = msg.chat.id
    await msg.reply(
        text="Questo step è tranquillamente skippabile, ti verrà dato un video molto simile ai precedenti, ma fatto "
             "apposta per i genitori, così che tutti possano capire di cosa si tratta questo grande progetto!"
        if await lc(id_) else "eng text : 7.1",
        reply_markup=Rkm(
            keyboard=[
                [
                    "Mi interessa",  # A1
                ],
                [
                    "Non mi interessa",  # B1
                ],
                [
                    "Set Language 🌐" if await lc(id_) else "Imposta Lingua 🌐",  # C1
                    "Contatto 👤" if await lc(id_) else "Contact 👤",  # C2
                ],
            ],
            one_time_keyboard=False,
            resize_keyboard=True
        )
    )


async def workshop_gio_gia(msg: Msg):
    """invia il workshop di gio&gia"""
    from pyrogram.types import InlineKeyboardMarkup as Ikm, InlineKeyboardButton as Ikb
    id_ = msg.from_user.id
    msg = await msg.reply(
        text="Questo video è una registrazione di una live di dicembre, ed è stata fatta veramente bene.\n"
             "Consiglio vivamente a tutti di guardarla almeno una volta!"
        if await lc(id_) else f"eng text : 7.2",
        reply_markup=Ikm([
            [Ikb(text="WORKSHOP",
                 # url="https://youtube.com/playlist?list=PLcm45GY4vpKCztVDHlfcPpyG4DPydaov0&si=YV8z-7uOrPKMpa7F",
                 callback_data="workshop gio&gia")],
            [Ikb(text="INSTAGRAM GIORGIO TRABALDO",
                 # url="https://www.instagram.com/giorgiotrabaldo?"
                 # "utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA==",
                 callback_data="ig giorgio from gio&gia")],
            [Ikb(text="TIK-TOK GIORGIO TRABALDO",
                 # url="https://www.tiktok.com/@giorgiotrabaldo?_t=8ifrWVfS3yz&_r=1",
                 callback_data="tt giorgio from gio&gia")],
        ]),
        disable_web_page_preview=True,
    )
    from asyncio import sleep
    await sleep(0.1)
    await msg.reply(
        text="Oppure prosegui, che abbiamo quasi finito!" if await lc(id_) else "eng text : 7.3",
        reply_markup=Rkm(
            keyboard=[
                [
                    "Step 8",  # A1
                ],
                [
                    "Contatto 👤" if await lc(id_) else "Contact 👤",  # B1
                ],
            ],
            one_time_keyboard=False,
            resize_keyboard=True
        )
    )
