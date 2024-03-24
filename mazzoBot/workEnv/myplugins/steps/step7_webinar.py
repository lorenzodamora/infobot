"""
questo file contiene il primo step informativo: il webinar

step 7
"""
from pyrogram.types import Message as Msg, InlineKeyboardMarkup as Ikm, InlineKeyboardButton as Ikb


async def step7(msg: Msg, lc: bool):
    """Manda il webinar di matteo bianco"""
    await msg.reply(
        text="SE CERCHI ALTRE INFORMAZIONI:" if lc
        else "IF YOU ARE LOOKING FOR ADDITIONAL INFORMATION:",
        reply_markup=Ikm([[
            Ikb(
                text="WEBINAR",
                url="https://youtube.com/playlist?list=PLcm45GY4vpKDqWQp99sPt-IL5SYnDSNwn&si=1_Jt-xGQvEUi_ovI"
            )
        ]]),
        disable_web_page_preview=True,  # Disabilita l'anteprima del sito web se presente
    )
