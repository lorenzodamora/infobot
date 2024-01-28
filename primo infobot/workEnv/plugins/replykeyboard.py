"""
questo file gestisce le risposte per messaggio e la replykeyboard
ogni evento fa un log
"""
from pyrogram import Client, filters as f
from pyrogram.types import (ReplyKeyboardMarkup as Rkm, InlineKeyboardMarkup as Ikm, InlineKeyboardButton as Ikb,
                            Message as Msg)
from .log import complete_log as clog
from asyncio import create_task as ct


# lang_check
async def lcheck(u_id) -> bool:
    """
    controlla la lingua dell'utente

    @see :func:'./lang.py/get_ulang'

    :param u_id: id utente
    :return: true se italiano, false inglese
    :rtype: bool
    """
    from .lang import get_ulang as glang
    if await glang(u_id) == "I":
        return True
    return False


@Client.on_message(f.regex(r"^Italiano$") | f.regex(r"^English$"), group=1)
async def set_lang(_, msg: Msg):
    """
    evento per settare la lingua e inviare lo start della ReplyKeyboard

    :param _: Client, che al momento non serve
    :param msg: messaggio contenente la lingua
    :type msg: Message
    """
    from .lang import set_ulang as slang
    name = msg.from_user.first_name
    u_id = msg.from_user.id
    # from pyrogram.types import BotCommand
    if msg.text == "Italiano":
        await msg.reply_text(f"Grazie per avermi insegnato l'italiano, {name} !!")
        await slang(user_id=u_id, lang="I")
        await lang_start(None, msg)

    else:
        await msg.reply_text(f"eng text : r0 {name}!\nwarning\nEnglish is not implemented yet")
        await slang(user_id=u_id, lang="E")

    # await lang_start(None, msg)
    _ = ct(clog(u_id, "testo", f"id:{msg.id}\n\ttext:{msg.text}"))


async def lang_start(_, msg: Msg):
    """
    vero start del bot, chiamato dal set-lingua e dai back-menu

    :param _: Client, che al momento non serve
    :param msg: Messaggio che ha lanciato l'evento
    :type msg: Message
    """
    await msg.reply(
        text="Questi bottoni ti aiuteranno a navigare tra le mie funzionalità" if await lcheck(msg.from_user.id)
        else "eng text : r1",
        reply_markup=Rkm(
            keyboard=[
                [
                    "Form",  # A1
                ],
                [
                    "❔ FAQ / Q&A ❓",  # B1
                    "🎦 Info & Video ℹ️",  # B2
                ],
                [
                    "Set Language 🌐" if await lcheck(msg.from_user.id) else "Imposta Lingua 🌐",  # C1
                ],
                [
                    "Contatto 👤" if await lcheck(msg.from_user.id) else "Contact 👤",  # D1
                ]
            ],
            one_time_keyboard=False,
            resize_keyboard=True
        )
    )


@Client.on_message(f.regex(r"^Form$"), group=0)
async def form(_, msg):
    """
    Invia il form

    :param _: Client, che al momento non serve
    :param msg:
    :type msg: Message
    """
    u_id = msg.from_user.id
    text = (f"Compila questo form se vuoi essere contattato per capire come iniziare la tua attività.\n"
            "\nSaremmo lieti di poter parlare insieme a te!") if await lcheck(u_id) \
        else f"eng text : r2"
    await msg.reply(
        text=text,
        reply_markup=Ikm([
            [Ikb(text="FORM",
                 # url=url
                 callback_data="form")]
        ]),
        disable_web_page_preview=True,  # Disabilita l'anteprima del sito web se presente
    )
    _ = ct(clog(u_id, "testo", f"id:{msg.id}\n\ttext:{msg.text}"))


@Client.on_message(f.regex(r"^Contatto 👤$") | f.regex(r"^Contact 👤$"), group=0)
async def contact(_, msg):
    """
    invia il mio contatto
    """
    u_id = msg.from_user.id
    tme = "https://t.me/Ill_Magnus"
    text = (f"Per qualsiasi problema o domanda:\nEcco [il mio contatto telegram]({tme})\n"
            f"\nAltri contatti:") if await lcheck(u_id) \
        else f"eng text : r3"
    from pyrogram.enums import ParseMode as Pm
    await msg.reply(
        text=text,
        parse_mode=Pm.MARKDOWN,  # Usa la formattazione Markdown
        reply_markup=Ikm([
            [Ikb(text="Telegram", url=tme)],
            [Ikb(text="Whatsapp",
                 # url="https://wa.me/c/393286435255"
                 callback_data="wa mio")],
            [Ikb(text="Instagram",
                 # url="https://www.instagram.com/ill__lore?
                 #     "utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
                 callback_data="ig mio")],
        ]),
        disable_web_page_preview=True,  # Disabilita l'anteprima del sito web se presente
    )
    _ = ct(clog(u_id, "testo", f"id:{msg.id}\n\ttext:{msg.text}"))


@Client.on_message(f.regex(r"^FAQ$"), group=0)
@Client.on_message(f.regex(r"^Q&A$"), group=0)
@Client.on_message(f.regex(r"^❔ FAQ / Q&A ❓$"), group=0)
async def faq(_, msg):
    """invia le FAQ"""
    u_id = msg.from_user.id
    await msg.reply(
        text="Non sono esattamente un motore di ricerca ma eccoti alcuni risultati:" if await lcheck(u_id)
        else "eng text : r4",
        reply_markup=Rkm(
            keyboard=[
                [
                    "Perché mi chiede il numero di telefono?" if await lcheck(u_id) else "eng text : r5",  # A1
                ],
                [
                    "Dati sensibili" if await lcheck(u_id) else "eng text : r6",  # B1
                ],
                [
                    "🔙 Menù",  # C1
                    "Contatto 👤" if await lcheck(u_id) else "Contact 👤",  # C2
                ],
            ],
            one_time_keyboard=False,
            resize_keyboard=True
        )
    )
    _ = ct(clog(u_id, "testo", f"id:{msg.id}\n\ttext:{msg.text}"))


@Client.on_message(f.regex(r"^🔙 Menù$"), group=0)
async def menu(_, msg):
    """Torna al menù iniziale"""
    await lang_start(None, msg)
    _ = ct(clog(msg.from_user.id, "testo", f"id:{msg.id}\n\ttext:{msg.text}"))


@Client.on_message(
    f.regex(r"^Perché mi chiede il numero di telefono?$") |
    f.regex(r"^Dati sensibili$"),
    group=0)
async def datisensibili(_, msg):
    """Invia una spiegazione sui dati sensibili richiesti nel form"""
    u_id = msg.from_user.id
    await msg.reply(
        text=("Nel form sono richiesti alcuni dati sensibili, come il numero di telefono e altri..\n"
              "Se hai delle preoccupazioni in merito, voglio tranquillizzarti immediatamente:\n i tuoi dati sono "
              "tutelati dalla legge dal Regolamento Generale sulla Protezione dei Dati (GDPR) dell'Unione Europea.\n"
              "Saranno utilizzati esclusivamente per permetterci di contattarti tramite WhatsApp, "
              "dove avremo l'opportunità di approfondire la nostra conoscenza reciprocamente in un contesto amichevole"
              " e di completare il processo informativo.\n\nInoltre, non effettueremo controlli sulla correttezza dei "
              "dati forniti, confidiamo nella vostra onestà in questo senso.\n"
              "La tua privacy è importante per noi.\n\nAvevo in mente un discorso, perciò l'ho scritto:\n"
              " Per rendersi la vita come un film bisogna rischiare come in un film, perciò: hai paura di dare il "
              "numero di telefono? Meglio! significa che non sei stupido, avventato o poco sveglio.\n Ma solo chi si "
              "mette in gioco avrà i risultati che cerca nella vita. La scelta è tua.") if await lcheck(u_id)
        else "eng text : r7"
    )
    _ = ct(clog(u_id, "testo", f"id:{msg.id}\n\ttext:{msg.text}"))


@Client.on_message(f.regex(r"^🎦 Info & Video ℹ️$"), group=0)
async def info(_, msg):
    """Manda la tab dei video"""
    u_id = msg.from_user.id
    await msg.reply(
        text="è proprio come youtube!!" if await lcheck(u_id)
        else "eng text : r8",
        reply_markup=Rkm(
            keyboard=[
                [
                    "Guarda il Webinar",  # A1
                ],
                [
                    "WorkShop",  # B1
                ],
                [
                    "Altre Info" if await lcheck(u_id) else "Other Info",  # C1
                ],
                [
                    "Quanto vale tutto questo?" if await lcheck(u_id) else "eng text : r5",  # D1
                ],
                [
                    "🔙 Menù",  # E1
                    "Contatto 👤" if await lcheck(u_id) else "Contact 👤",  # E2
                ],
            ],
            one_time_keyboard=False,
            resize_keyboard=True
        )
    )
    _ = ct(clog(u_id, "testo", f"id:{msg.id}\n\ttext:{msg.text}"))


@Client.on_message(f.regex(r"^Quanto vale tutto questo?$"))
async def valore(_, msg):
    """Invia il testo sul valore e le inline per gli ig dei grossi leader"""
    u_id = msg.from_user.id
    await msg.reply(
        text=(
            "Purtroppo anche solo rispondere a questa domanda, qui per messaggio, è estremamente riduttivo..\n"
            "Perché invece non me lo chiedete in pvt? @Ill_Magnus\n"
            "Oppure potete andare a vedere i social dei miei collaboratori più veterani (in ordine di importanza):"
        ) if await lcheck(u_id) else "eng text : r6",
        reply_markup=Ikm([
            [Ikb(text="GIORGIO TRABALDO",
                 # url="https://www.instagram.com/giorgiotrabaldo?"
                 #     "utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
                 callback_data="ig giorgio trabaldo")],
            [Ikb(text="MATTEO BIANCO",
                 # url="https://www.instagram.com/matteobianco_papi?"
                 #     "utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
                 callback_data="ig matteo bianco")],
            [Ikb(text="MAURO BOCCOMINO",
                 # url="https://www.instagram.com/mauro_boccomino?"
                 #     "utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
                 callback_data="ig mauro boccomino")],
            [Ikb(text="ANDREA TRAINA",
                 # url="https://www.instagram.com/andreatraina_?"
                 #     "utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
                 callback_data="ig andrea traina")],
            [Ikb(text="MATTEO DEPRETIS",
                 # url="https://www.instagram.com/matteo.depetris?"
                 #     "utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
                 callback_data="ig matteo depretis")],
            [Ikb(text="DYLAN DAGANI",
                 # url="https://www.instagram.com/dylandagani?"
                 #     "utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
                 callback_data="ig dylan dagani")],
            [Ikb(text="MARCO MANENTI",
                 # url="https://www.instagram.com/marcomanentii?"
                 #     "utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
                 callback_data="ig marco manenti")],
            [Ikb(text="MANUEL MAZZOLA",
                 # url="https://www.instagram.com/manuel_mazzola_?"
                 #     "utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
                 callback_data="ig manuel mazzola")],
            [Ikb(text="BRANDON ZANCHI",
                 # url="https://www.instagram.com/brandon.zanchi?"
                 #     "utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
                 callback_data="ig brandon zanchi")],
            [Ikb(text="LORENZO D'AMORA (io)",
                 # url="https://www.instagram.com/ill__lore?"
                 #     "utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA=="
                 callback_data="ig mio")],
        ]),
        disable_web_page_preview=True,
    )
    _ = ct(clog(u_id, "testo", f"id:{msg.id}\n\ttext:{msg.text}"))


@Client.on_message(f.regex(r"^Guarda il Webinar$"))
async def webinar(_, msg):
    """Manda la tab dei webinar"""
    u_id = msg.from_user.id
    await msg.reply(
        text="Scegli quale webinar guardare. tutti i webinar spiegano pressapoco le stesse cose." if await lcheck(u_id)
        else "eng text : r7",
        reply_markup=Rkm(
            keyboard=[
                [
                    "Il mio webinar Ita" if await lcheck(u_id) else "My webinar Eng",  # A1
                    "Il mio webinar Eng" if await lcheck(u_id) else "My webinar Ita",  # A2
                ],
                [
                    "🇮🇹Webinar di Matteo Bianco" if await lcheck(u_id)
                    else "🇮🇹Matteo Bianco's webinar",  # B1
                ],
                [
                    "🔙 Menù",  # C1
                    "🎦 Info & Video ℹ️",  # C2
                ],
            ],
            one_time_keyboard=False,
            resize_keyboard=True
        )
    )
    _ = ct(clog(u_id, "testo", f"id:{msg.id}\n\ttext:{msg.text}"))


@Client.on_message(f.regex(r"^Il mio webinar Ita$") | f.regex(r"^My webinar Ita$"))
async def webinarita(_, msg):
    """invia il mio webinar italiano"""
    u_id = msg.from_user.id
    text = (f"Questo webinar è stato registrato apposta per informarvi in breve e senza giri di parole su "
            f"quello che volete e dovete sapere:\n") if await lcheck(u_id) \
        else f"eng text : r8"
    await msg.reply(
        text=text,
        reply_markup=Ikm([
            [Ikb(text="WEBINAR",
                 # url=url,
                 callback_data="my webinar ita")],
        ]),
        disable_web_page_preview=True,
    )
    _ = ct(clog(u_id, "testo", f"id:{msg.id}\n\ttext:{msg.text}"))


@Client.on_message(f.regex(r"^Il mio webinar Eng$") | f.regex(r"^My webinar Eng$"))
async def webinareng(_, msg):
    """invia il mio webinar inglese"""
    u_id = msg.from_user.id
    text = (f"Questo webinar è stato registrato apposta per informarvi in breve e senza giri di parole su "
            f"quello che volete e dovete sapere:\n") if await lcheck(u_id) \
        else f"eng text : r8"
    await msg.reply(
        text=text,
        reply_markup=Ikm([
            [Ikb(text="WEBINAR",
                 # url=url,
                 callback_data="my webinar eng")],
        ]),
        disable_web_page_preview=True,
    )
    _ = ct(clog(u_id, "testo", f"id:{msg.id}\n\ttext:{msg.text}"))


@Client.on_message(f.regex(r"^🇮🇹Webinar di Matteo Bianco$") | f.regex(r"^🇮🇹Matteo Bianco's Webinar$"))
async def webinarbianco(_, msg):
    """invia il vecchio webinar di matteo bianco"""
    u_id = msg.from_user.id
    text = (f"Questo webinar è stato registrato un pò di tempo fa da parte di uno dei nostri leader per informarvi su "
            f"quello che volete e dovete sapere:\n") if await lcheck(u_id) \
        else f"eng text : r9"
    await msg.reply(
        text=text,
        reply_markup=Ikm([
            [Ikb(text="WEBINAR",
                 # url="https://youtube.com/playlist?list=PLcm45GY4vpKDqWQp99sPt-IL5SYnDSNwn&si=1_Jt-xGQvEUi_ovI",
                 callback_data="webinar bianco")],
            [Ikb(text="INSTAGRAM MATTEO BIANCO",
                 # url="https://www.instagram.com/matteobianco_papi?"
                 # "utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA==",
                 callback_data="ig bianco from webinar bianco")],
            [Ikb(text="TIK-TOK MATTEO BIANCO",
                 # url="https://www.tiktok.com/@biancomatteo?_t=8iduVPPtLou&_r=1",
                 callback_data="tt bianco from webinar bianco")],
        ]),
        disable_web_page_preview=True,
    )
    _ = ct(clog(u_id, "testo", f"id:{msg.id}\n\ttext:{msg.text}"))


@Client.on_message(f.regex(r"^WorkShop$"))
async def workshop(_, msg):
    """Manda la tab dei WorkShop"""
    u_id = msg.from_user.id
    await msg.reply(
        text="Scegli quale WorkShop guardare. "
             "in questo caso i due workshop spiegano cose diverse." if await lcheck(u_id) else "eng text : r10",
        reply_markup=Rkm(
            keyboard=[
                [
                    "gio&gia, lungo e completo" if await lcheck(u_id) else "eng text : r11",  # A1
                ],
                [
                    "Manenti, corto e abbastanza vecchio" if await lcheck(u_id) else "eng text : r12",  # B1
                ],
                [
                    "🔙 Menù",  # C1
                    "🎦 Info & Video ℹ️",  # C2
                ],
            ],
            one_time_keyboard=False,
            resize_keyboard=True)
    )
    _ = ct(clog(u_id, "testo", f"id:{msg.id}\n\ttext:{msg.text}"))


@Client.on_message(f.regex(r"^gio&gia, lungo e completo$"))
async def long_workshop(_, msg):
    """invia il workshop di gio&gia"""
    u_id = msg.from_user.id
    text = (f"Questo workshop è stato registrato da parte di uno dei nostri leader per informarvi su "
            f"quello che volete e dovete sapere:\n") if await lcheck(u_id) \
        else f"eng text : r13"
    await msg.reply(
        text=text,
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
    _ = ct(clog(u_id, "testo", f"id:{msg.id}\n\ttext:{msg.text}"))


@Client.on_message(f.regex(r"^Altre Info$") | f.regex(r"^Other Info$"))
async def other_info(_, msg):
    """invia le other info, non ancora implementate (non mi ricordo che ci volevo mettere)"""
    await msg.reply_text("\\")
    _ = ct(clog(msg.from_user.id, "testo", f"id:{msg.id}\n\ttext:{msg.text}"))
