"""
questo file contiene il primo step informativo: il webinar

step 3
"""
from pyrogram.types import Message as Msg, InlineKeyboardMarkup as Ikm, InlineKeyboardButton as Ikb
from asyncio import sleep
from ..lang import lc
from ..handler import mycontact


async def step3(msg: Msg):
    """Manda il link video della startUp"""
    await msg.reply(
        text="Ovviamente per iniziare a vivere la vita da film che sogni!\n"
             "Il modo più veloce per entrambi è guardare questo video!\n/contatto" if await lc(msg.chat.id) else
        "Of course, to start living the movie-like life you dream of!\n"
        "The fastest way for both is to watch this video!\n/contact",
        reply_markup=Ikm([[
                Ikb(
                    text="VIDEO",
                    url="https://youtube.com/playlist?list=PLcm45GY4vpKDxuBf0nSZJ5j3EmLcabQyj&si=26d5TtvaQ-z3mGmb"
                )
            ]]),
        disable_web_page_preview=True,  # Disabilita l'anteprima del sito web se presente
    )
    await sleep(20)
    await mycontact(msg)
