"""
questo file contiene il video del piano compensi di BE (inglese)

step 8
"""
from pyrogram.types import Message as Msg, InlineKeyboardMarkup as Ikm, InlineKeyboardButton as Ikb


async def step8(msg: Msg, lc: bool):
    await msg.reply(
        text="SE CERCHI INFORMAZIONI TECNICHE:" if lc
        else "IF YOU ARE LOOKING FOR TECHNICAL INFORMATION:",
        reply_markup=Ikm([[
            Ikb(
                text="BE COMPENSATION PLAN | ENG",
                url="https://youtube.com/playlist?list=PLcm45GY4vpKAPLRYHAkjWI6AI90NBiAti&si=39uQwf8zVcTNsiZq"
            )
        ]]),
        disable_web_page_preview=True,  # Disabilita l'anteprima del sito web se presente
    )
