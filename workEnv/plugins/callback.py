"""
questo file contiene la risposta alle callback query dei pulsanti presenti in ./replykeyboard.py
"""
from pyrogram import Client
from pyrogram.types import CallbackQuery as Cbq


async def add(u_id, data: str):
    """
    Aggiunge il click ai file

    Aggiunge il click ai file di log e file di conteggio click
    funzione chiamata per ogni query ricevuta

    :param u_id: user id
    :type u_id: Any
    :param data: data text della query
    :type data: str
    """
    from .linkClick import add_click as ac
    from .log import complete_log as clog
    from asyncio import create_task as ct
    _ = ct(ac(data))
    _ = ct(clog(u_id, "click", f"link: {data}"))


@Client.on_callback_query()
async def callback(_, query: Cbq) -> Cbq:
    """
    gestisce le callback query

    quando viene creata una callback query, viene gestita qua.\n
    al momento vengono chiesti solo link social, form, video

    :param _: Client, che al momento non serve
    :param query: la query creata
    :type query: CallbackQuery
    :return: ritorna la query originale, nel caso serva
    :rtype: Coroutine[Any, Any, CallbackQuery]
    """
    from pyrogram.enums import ParseMode as Pm
    from .replykeyboard import lcheck as lc

    # errore = False
    d = str(query.data)
    u_id = query.from_user.id
    m = Pm.MARKDOWN
    msg = query.message
    if d == "form":
        await msg.reply(
            text="**Form non ancora creato**" if await lc(u_id) else "eng text : q0",
            parse_mode=m
        )

    elif d == "wa mio":
        url = "https://wa.me/c/393286435255"
        await msg.reply(
            text=f"[Eccoti il link per contattarmi su whatsapp]({url})\n[{url}]({url})" if await lc(u_id)
            else "eng text : q1",
            parse_mode=m
        )

    elif d == "ig mio":
        url = "https://www.instagram.com/ill__lore?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
        await msg.reply(
            text=f"[Eccoti il link per contattarmi su instagram]({url})\n[{url}]({url})"
            if await lc(u_id) else "eng text : q2",
            parse_mode=m
        )

    elif d == "ig giorgio trabaldo":
        url = "https://www.instagram.com/giorgiotrabaldo?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
        await msg.reply(
            text=f"[Eccoti il link instagram di Giorgio Trabaldo]({url})\n[{url}]({url})"
            if await lc(u_id) else "eng text : q3",
            parse_mode=m
        )

    elif d == "ig matteo bianco":
        url = "https://www.instagram.com/matteobianco_papi?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
        await msg.reply(
            text=f"[Eccoti il link instagram di Matteo Bianco Papi]({url})\n[{url}]({url})"
            if await lc(u_id) else "eng text : q4",
            parse_mode=m
        )

    elif d == "ig mauro boccomino":
        url = "https://www.instagram.com/mauro_boccomino?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
        await msg.reply(
            text=f"[Eccoti il link instagram di Mauro Boccomino]({url})\n[{url}]({url})"
            if await lc(u_id) else "eng text : q5",
            parse_mode=m
        )

    elif d == "ig andrea traina":
        url = "https://www.instagram.com/andreatraina_?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
        await msg.reply(
            text=f"[Eccoti il link instagram di Andrea Traina]({url})\n[{url}]({url})"
            if await lc(u_id) else "eng text : q6",
            parse_mode=m
        )

    elif d == "ig matteo depretis":
        url = "https://www.instagram.com/matteo.depetris?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
        await msg.reply(
            text=f"[Eccoti il link instagram di Matteo Depetris]({url})\n[{url}]({url})"
            if await lc(u_id) else "eng text : q7",
            parse_mode=m
        )

    elif d == "ig dylan dagani":
        url = "https://www.instagram.com/dylandagani?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
        await msg.reply(
            text=f"[Eccoti il link instagram di Dylan Dagani]({url})\n[{url}]({url})"
            if await lc(u_id) else "eng text : q8",
            parse_mode=m
        )

    elif d == "ig marco manenti":
        url = "https://www.instagram.com/marcomanentii?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
        await msg.reply(
            text=f"[Eccoti il link instagram di Marco Manenti]({url})\n[{url}]({url})"
            if await lc(u_id) else "eng text : q9",
            parse_mode=m
        )

    elif d == "ig manuel mazzola":
        url = "https://www.instagram.com/manuel_mazzola_?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
        await msg.reply(
            text=f"[Eccoti il link instagram di Manuel Mazzola]({url})\n[{url}]({url})"
            if await lc(u_id) else "eng text : q10",
            parse_mode=m
        )

    elif d == "ig brandon zanchi":
        url = "https://www.instagram.com/brandon.zanchi?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
        await msg.reply(
            text=f"[Eccoti il link instagram di Brandon Zanchi]({url})\n[{url}]({url})"
            if await lc(u_id) else "eng text : q11",
            parse_mode=m
        )

    elif d == "my webinar ita":
        await msg.reply(
            text="**Webinar non ancora caricato**" if await lc(u_id) else "eng text : q12",
            parse_mode=m
        )

    elif d == "my webinar eng":
        await msg.reply(
            text="**Webinar non ancora caricato**" if await lc(u_id) else "eng text : q13",
            parse_mode=m
        )

    elif d == "webinar bianco":
        url = "https://youtube.com/playlist?list=PLcm45GY4vpKDqWQp99sPt-IL5SYnDSNwn&si=1_Jt-xGQvEUi_ovI"
        await msg.reply(
            text=f"[Eccoti il link youtube del webinar di Matteo Bianco]({url})\n[{url}]({url})"
            if await lc(u_id) else "eng text : q14",
            parse_mode=m
        )

    elif d == "ig bianco from webinar bianco":
        url = "https://www.instagram.com/matteobianco_papi?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
        await msg.reply(
            text=f"[Eccoti il link instagram di Matteo Bianco Papi]({url})\n[{url}]({url})"
            if await lc(u_id) else "eng text : q4",
            parse_mode=m
        )

    elif d == "tt bianco from webinar bianco":
        url = "https://www.tiktok.com/@biancomatteo?_t=8iduVPPtLou&_r=1"
        await msg.reply(
            text=f"[Eccoti il link tik-tok di Matteo Bianco Papi]({url})\n[{url}]({url})"
            if await lc(u_id) else "eng text : q15",
            parse_mode=m
        )

    elif d == "workshop gio&gia":
        url = "https://youtube.com/playlist?list=PLcm45GY4vpKCztVDHlfcPpyG4DPydaov0&si=YV8z-7uOrPKMpa7F"
        await msg.reply(
            text=f"[Eccoti il link youtube del whorkshop di gio&gia]({url})\n[{url}]({url})"
            if await lc(u_id) else "eng text : q16",
            parse_mode=m
        )

    elif d == "ig giorgio from gio&gia":
        url = "https://www.instagram.com/giorgiotrabaldo?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
        await msg.reply(
            text=f"[Eccoti il link instagram di Giorgio Trabaldo]({url})\n[{url}]({url})"
            if await lc(u_id) else "eng text : q3",
            parse_mode=m
        )

    elif d == "tt giorgio from gio&gia":
        url = "https://www.tiktok.com/@giorgiotrabaldo?_t=8ifrWVfS3yz&_r=1"
        await msg.reply(
            text=f"[Eccoti il link tik-tok di Giorgio Trabaldo]({url})\n[{url}]({url})"
            if await lc(u_id) else "eng text : q17",
            parse_mode=m
        )

    else:
        # errore
        await msg.reply_text(f"c'è stato un errore, contattami @ill_magnus" if await lc(u_id) else "eng text : q18"
                                                                                                   "\nerror")
        await add(u_id, f"ERRORE\nATTENZIONE\ndata:{d}\nRisolto?no")
        # errore = True
        return query

    # if not errore:
    await add(u_id, d)
    return query
