"""
questo file contiene uno step extra accessibile solo se conosci il comando univoco per utente.
un menù di informazioni extra e materiale

step 9
"""
from pyrogram.types import Message as Msg
from ..lang import lc


async def step9(msg: Msg):
    """
    :param msg: Messaggio che ha lanciato l'evento
    :type msg: Message
    """
    id_ = msg.chat.id
    await msg.reply(
        text="Benvenuto nella sezione segreta! di seguito l'indice di comandi per spulciare del materiale extra\n\n"
             f"/{id_} - questo menù\n"
             f"/{id_}bzNotion - manda il link di notion della bzone\n"
             f"\n al momento non è presente altro materiale, contattami! @Ill_Magnus"
        if await lc(id_) else "eng text : 9.1",
        disable_web_page_preview=True
    )


async def bznotion(msg: Msg):
    await msg.reply_text(
        text="https://bz-zone.notion.site/bz-zone/DRIVE-THE-TEAM-ded9dfce9816492d8cab8faf642097f2"
    )
