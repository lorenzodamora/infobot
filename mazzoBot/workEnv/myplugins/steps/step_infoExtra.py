"""
questo file contiene uno step extra accessibile solo se conosci il comando univoco per utente.
un menù di informazioni extra e materiale

step 9
"""
from pyrogram.types import Message as Msg


async def step_(msg: Msg, lc: bool):
    """
    :param lc: lang check == is_ita
    :param msg: Messaggio che ha lanciato l'evento
    :type msg: Message
    """
    id_ = msg.chat.id
    await msg.reply(
        text="Benvenuto nella sezione segreta! di seguito l'indice di comandi per spulciare del materiale extra\n\n"
             f"/{id_} - questo menù\n"
             f"/{id_}bzNotion - manda il link di notion della bzone\n"
             f"/{id_}presentazioni - manda il link drive delle presentazioni multilingue\n"
             f"\n al momento non è presente altro materiale, contattami! @Ill_Magnus"
        if lc else
        "Welcome to the secret section! Below is the command index to explore extra material\n\n"
        f"/{id_} - this menu\n"
        f"/{id_}bzNotion - sends the link to the bzone Notion\n"
        f"/{id_}presentations - sends the Google Drive link for multilingual presentations\n"
        "\n Currently, there is no other material available. Contact me for more! @Ill_Magnus",
        disable_web_page_preview=True
    )


async def bznotion(msg: Msg):
    await msg.reply_text(
        text="https://bz-zone.notion.site/bz-zone/DRIVE-THE-TEAM-ded9dfce9816492d8cab8faf642097f2"
    )


async def presentazioni(msg: Msg):
    await msg.reply_text(
        text="https://drive.google.com/drive/folders/12WBfV5D7Z707_DzB1FwTES1s96SyE4RK"
    )
