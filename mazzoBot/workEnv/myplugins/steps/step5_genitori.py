"""
questo file contiene il workshop gio&gia, fatto apposta per i genitori

step 5
"""
from pyrogram.types import (Message as Msg, ReplyKeyboardMarkup as Rkm,
                            InlineKeyboardMarkup as Ikm, InlineKeyboardButton as Ikb)


async def step5(msg: Msg, lc: bool):
    await msg.reply(
        text="Questo step è tranquillamente skippabile, ti verrà dato un video molto simile ai precedenti, "
             "ma fatto apposta per i genitori, così che tutti possano capire di cosa si tratta questo grande progetto!"
        if lc
        else "This step is easily skippable; you'll be given a video very similar to the previous ones, "
             "but made specifically for parents so that everyone can understand what this great project is about!",
        reply_markup=Rkm(
            keyboard=[
                [
                    "Mi interessa" if lc else "I'm interested",  # A1
                ],
                [
                    "Non mi interessa" if lc else "I'm not interested",  # B1
                ],
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )


async def workshop_gio_gia(msg: Msg, lc: bool):
    """invia il workshop di gio&gia"""
    await msg.reply(
        text="Questo video è una registrazione di una live di dicembre, ed è stata fatta veramente bene.\n"
             "Consiglio vivamente a tutti di guardarla almeno una volta!" if lc
        else "This video is a recording of a live stream from December, and it's really well done.\n"
             "I highly recommend everyone to watch it at least once!",
        reply_markup=Ikm([[
            Ikb(
                text="VIDEO",
                url="https://youtube.com/playlist?list=PLcm45GY4vpKCztVDHlfcPpyG4DPydaov0&si=YV8z-7uOrPKMpa7F"
            )
        ]]),
        disable_web_page_preview=True,  # Disabilita l'anteprima del sito web se presente
    )
