"""
questo file contiene il secondo step informativo: workshop

step 4
"""
from pyrogram.types import (Message as Msg, ReplyKeyboardMarkup as Rkm,
                            InlineKeyboardMarkup as Ikm, InlineKeyboardButton as Ikb)
from ..lang import lc


async def step4(msg: Msg):
    await msg.reply(
        text="Sei carico per il prossimo video?" if await lc(msg.chat.id) else "Are you ready for the next video?",
        reply_markup=Rkm(
            keyboard=[
                [
                    "ASSOLUTAMENTE SI!" if await lc(msg.chat.id) else "ABSOLUTELY YES!",  # A1
                ],
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        ),
    )


async def workshop(msg: Msg):
    """Manda il workshop"""
    await msg.reply(
        text="/contact",
        reply_markup=Ikm([[
            Ikb(
                text="VIDEO",
                url="https://youtube.com/playlist?list=PLcm45GY4vpKBL4quIBcQPcYcQChPQ_aqA&si=ybee2BRhV70PduIT"
            )
        ]]),
        disable_web_page_preview=True,  # Disabilita l'anteprima del sito web se presente
    )
