"""
questo file contiene la risposta alle callback query degli inlinekeyboard button
"""
from pyrogram import Client
from pyrogram.types import CallbackQuery as Cbq


async def add(id_, data: str):
    """
    Aggiunge il click ai file

    Aggiunge il click ai file di log e file di conteggio click
    funzione chiamata per ogni query ricevuta

    :param id_: user id
    :type id_: Any
    :param data: data text della query
    :type data: str
    """
    from .linkClick import add_click
    from .log import complete_log
    from asyncio import create_task
    _ = create_task(add_click(data))
    _ = create_task(complete_log(id_, "click", f"link: {data}"))


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
    from .lang import lc

    # errore = False
    d = str(query.data)
    id_ = query.from_user.id
    msg = query.message
    text = '\\'

    # region contatto
    if d == "wa mio":
        url = "https://wa.me/c/393286435255"
        text = (f"[Eccoti il link per contattarmi su whatsapp]({url})\n\n[{url}]({url})"
                if await lc(id_) else "eng text : q-")

    elif d == "ig mio":
        url = "https://www.instagram.com/ill__lore?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
        text = (f"[Eccoti il link per contattarmi su instagram]({url})\n\n[{url}]({url})"
                if await lc(id_) else "eng text : q-")
    # endregion

    # region webinar
    elif d == "my webinar ita":
        text = "**Webinar non ancora caricato**" if await lc(id_) else "eng text : q-"

    elif d == "my webinar eng":
        text = "**Webinar non ancora caricato**" if await lc(id_) else "eng text : q-"

    elif d == "webinar bianco":
        url = "https://youtube.com/playlist?list=PLcm45GY4vpKDqWQp99sPt-IL5SYnDSNwn&si=1_Jt-xGQvEUi_ovI"
        text = (f"[Eccoti il link youtube del webinar di Matteo Bianco]({url})\n\n[{url}]({url})"
                if await lc(id_) else "eng text : q-")

    elif d == "ig bianco from webinar bianco":
        url = "https://www.instagram.com/matteobianco_papi?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
        text = (f"[Eccoti il link instagram di Matteo Bianco Papi]({url})\n\n[{url}]({url})"
                if await lc(id_) else "eng text : q-")

    elif d == "tt bianco from webinar bianco":
        url = "https://www.tiktok.com/@biancomatteo?_t=8iduVPPtLou&_r=1"
        text = (f"[Eccoti il link tik-tok di Matteo Bianco Papi]({url})\n\n[{url}]({url})"
                if await lc(id_) else "eng text : q-")
    # endregion

    # region workshop
    elif d == "workshop giorgio":
        url = "https://youtube.com/playlist?list=PLcm45GY4vpKBL4quIBcQPcYcQChPQ_aqA&si=ybee2BRhV70PduIT"
        text = (f"[Eccoti il link youtube del workshop di Giorgio Trabaldo]({url})\n\n[{url}]({url})"
                if await lc(id_) else "eng text : q-")

    elif d == "ig giorgio from workshop":
        url = "https://www.instagram.com/giorgiotrabaldo?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
        text = (f"[Eccoti il link instagram di Giorgio Trabaldo]({url})\n\n[{url}]({url})"
                if await lc(id_) else "eng text : q-")

    elif d == "tt giorgio from workshop":
        url = "https://www.tiktok.com/@giorgiotrabaldo?_t=8ifrWVfS3yz&_r=1"
        text = (f"[Eccoti il link tik-tok di Giorgio Trabaldo]({url})\n\n[{url}]({url})"
                if await lc(id_) else "eng text : q-")

    elif d == "workshop gio&gia":
        url = "https://youtube.com/playlist?list=PLcm45GY4vpKCztVDHlfcPpyG4DPydaov0&si=YV8z-7uOrPKMpa7F"
        text = (f"[Eccoti il link youtube del workshop di Giorgio Trabaldo e Giorgia Vitaloni]({url})\n\n"
                f"[{url}]({url})"
                if await lc(id_) else "eng text : q-")

    elif d == "ig giorgio from gio&gia":
        url = "https://www.instagram.com/giorgiotrabaldo?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
        text = (f"[Eccoti il link instagram di Giorgio Trabaldo]({url})\n\n[{url}]({url})"
                if await lc(id_) else "eng text : q-")

    elif d == "tt giorgio from gio&gia":
        url = "https://www.tiktok.com/@giorgiotrabaldo?_t=8ifrWVfS3yz&_r=1"
        text = (f"[Eccoti il link tik-tok di Giorgio Trabaldo]({url})\n\n[{url}]({url})"
                if await lc(id_) else "eng text : q-")
    # endregion

    elif d == "form":
        text = "**Form non ancora creato**" if await lc(id_) else "eng text : q-"

    # region valore
    elif d == "ig giorgio trabaldo":
        url = "https://www.instagram.com/giorgiotrabaldo?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
        text = f"[Eccoti il link instagram di Giorgio Trabaldo]({url})\n\n[{url}]({url})" \
            if await lc(id_) else "eng text : q-"

    elif d == "ig matteo bianco":
        url = "https://www.instagram.com/matteobianco_papi?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
        text = f"[Eccoti il link instagram di Matteo Bianco Papi]({url})\n\n[{url}]({url})"\
            if await lc(id_) else "eng text : q-"

    elif d == "ig mauro boccomino":
        url = "https://www.instagram.com/mauro_boccomino?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
        text = f"[Eccoti il link instagram di Mauro Boccomino]({url})\n\n[{url}]({url})"\
            if await lc(id_) else "eng text : q-"

    elif d == "ig andrea traina":
        url = "https://www.instagram.com/andreatraina_?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
        text = f"[Eccoti il link instagram di Andrea Traina]({url})\n\n[{url}]({url})"\
            if await lc(id_) else "eng text : q-"

    elif d == "ig matteo depretis":
        url = "https://www.instagram.com/matteo.depetris?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
        text = f"[Eccoti il link instagram di Matteo Depetris]({url})\n\n[{url}]({url})"\
            if await lc(id_) else "eng text : q-"

    elif d == "ig dylan dagani":
        url = "https://www.instagram.com/dylandagani?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
        text = f"[Eccoti il link instagram di Dylan Dagani]({url})\n\n[{url}]({url})"\
            if await lc(id_) else "eng text : q-"

    elif d == "ig marco manenti":
        url = "https://www.instagram.com/marcomanentii?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
        text = f"[Eccoti il link instagram di Marco Manenti]({url})\n\n[{url}]({url})"\
            if await lc(id_) else "eng text : q-"

    elif d == "ig manuel mazzola":
        url = "https://www.instagram.com/manuel_mazzola_?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
        text = f"[Eccoti il link instagram di Manuel Mazzola]({url})\n\n[{url}]({url})"\
            if await lc(id_) else "eng text : q-"

    elif d == "ig brandon zanchi":
        url = "https://www.instagram.com/brandon.zanchi?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
        text = f"[Eccoti il link instagram di Brandon Zanchi]({url})\n\n[{url}]({url})"\
            if await lc(id_) else "eng text : q-"
    # endregion

    else:
        # errore
        await msg.reply_text(f"c'è stato un errore, contattami @ill_magnus"
                             if await lc(id_) else "eng text : q-\nerror")
        await add(id_, f"ERRORE\nATTENZIONE\ndata:{d}\nRisolto?no")
        return query

    from pyrogram.enums import ParseMode
    await msg.reply(text=text, parse_mode=ParseMode.MARKDOWN)
    await add(id_, d)
    return query
