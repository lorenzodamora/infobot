"""
questo file contiene il primo step informativo: il webinar

step 3
"""
from pyrogram.types import Message as Msg
from ..lang import lc


async def step3(msg: Msg):
    """
    :param msg: Messaggio che ha lanciato l'evento
    :type msg: Message
    """
    from pyrogram.types import ReplyKeyboardMarkup as Rkm
    c_id = msg.chat.id
    msg = await msg.reply(
        text="**Innanzitutto**, ti starai chiedendo a cosa serve questo bot, vero?"
        if await lc(c_id) else "eng text : 3.-",
        reply_markup=Rkm(
            keyboard=[
                [
                    "Contatto 👤" if await lc(c_id) else "Contact 👤",  # B1
                ],
            ],
            one_time_keyboard=False,
            resize_keyboard=True
        )
    )
    from asyncio import sleep
    await sleep(3)
    msg = await msg.reply_text(
        "__Beh__, è tutto più semplice di quanto sembri! **Questo bot** è qui per guidarti --passo-passo--, apposta "
        "per __farti comprendere__ meglio di cosa parlavo nel video che ti ha portato fino a qui!"
        if await lc(c_id) else "eng text : 3.-"
    )
    await sleep(6)
    msg = await msg.reply_text(
        "Ora, capisco che tutto questo --non sia proprio per tutti--, avrai comunque l'opportunità di ricevere "
        "__informazioni__ che assolutamente non sono per tutti.\n"
        "Dopodichè, se sei curioso, interessato o persino un po' annoiato, fammelo sapere! __Intanto__ bando alle "
        "ciance e diamo inizio allo step 3!" if await lc(c_id) else "eng text : 3.-"
    )
    await sleep(12)
    msg = await msg.reply(
        text="Vedi quanto stai andando veloce? Sei già al **3o step**: guardare il video!\n" if await lc(c_id)
        else "eng text : 3.-",
        reply_markup=Rkm(
            keyboard=[
                [
                    "Guardo il video!",  # A1
                ],
                [
                    "Set Language 🌐" if await lc(c_id) else "Imposta Lingua 🌐",  # B1
                    "Contatto 👤" if await lc(c_id) else "Contact 👤",  # B2
                ],
            ],
            one_time_keyboard=False,
            resize_keyboard=True
        )
    )
    await sleep(4)
    await msg.reply_text(
        "Immagino che invece __tu__ voglia che ti venga spiegato per quale motivo perdere il tuo tempo in questo "
        "noiosissimo video.." if await lc(c_id) else "eng text : 3.-"
    )
    await sleep(5)
    await msg.reply_text(
        "Beh, **innanzitutto** non è così noioso, dico sul serio! __Ma comunque__, la risposta è molto semplice, ti "
        "invito a rivedere il brevissimo video che ti ha consigliato di accendermi, secondo me una **possibilità** "
        "puoi darmela, se non al video almeno a me in privata, conosciamoci molto volentieri!\n"
        "Contattami con /contatto oppure @Ill_Magnus !"
        if await lc(c_id) else "eng text : 3.-"
    )


async def tabwebinar(msg: Msg):
    """Manda la tab dei webinar"""
    from pyrogram.types import ReplyKeyboardMarkup as Rkm
    u_id = msg.from_user.id
    await msg.reply(
        text="Scegli quale webinar guardare. Tutti i webinar spiegano pressapoco le stesse cose." if await lc(u_id)
        else "eng text : 3.2",
        reply_markup=Rkm(
            keyboard=[
                [
                    "Il mio webinar Ita" if await lc(u_id) else "My webinar Eng",  # A1
                    "Il mio webinar Eng" if await lc(u_id) else "My webinar Ita",  # A2
                ],
                [
                    "🇮🇹Webinar di Matteo Bianco" if await lc(u_id)
                    else "🇮🇹Matteo Bianco's webinar",  # B1
                ],
            ],
            one_time_keyboard=False,
            resize_keyboard=True
        )
    )


async def webinarita(msg: Msg):
    """invia il mio webinar italiano"""
    from pyrogram.types import InlineKeyboardMarkup as Ikm, InlineKeyboardButton as Ikb
    u_id = msg.from_user.id
    await msg.reply(
        text=f"Questo webinar è stato registrato in italiano da me, apposta per voi, "
             f"così che possiate informarvi in breve e senza "
             f"giri di parole su quello che volete e dovete sapere:" if await lc(u_id) else f"eng text : 3.3",
        reply_markup=Ikm([
            [Ikb(text="WEBINAR",
                 callback_data="my webinar ita")]
        ]),
        disable_web_page_preview=True,
    )
    await continua(msg)


async def webinareng(msg: Msg):
    """invia il mio webinar inglese"""
    from pyrogram.types import InlineKeyboardMarkup as Ikm, InlineKeyboardButton as Ikb
    u_id = msg.from_user.id
    await msg.reply(
        text=f"Questo webinar è stato registrato in inglese da me, apposta per voi, "
             f"così che possiate informarvi in breve e senza "
             f"giri di parole su quello che volete e dovete sapere:" if await lc(u_id) else f"eng text : 3.4",
        reply_markup=Ikm([
            [Ikb(text="WEBINAR",
                 callback_data="my webinar eng")],
        ]),
        disable_web_page_preview=True,
    )
    await continua(msg)


async def webinarbianco(msg: Msg):
    from pyrogram.types import InlineKeyboardMarkup as Ikm, InlineKeyboardButton as Ikb
    """invia il vecchio webinar di matteo bianco"""
    u_id = msg.from_user.id
    await msg.reply(
        text=f"Questo webinar è stato registrato un pò di tempo fa da parte di uno dei nostri leader per informarvi su "
             f"quello che volete e dovete sapere:" if await lc(u_id) else f"eng text : 3.5",
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
    await continua(msg)


async def continua(msg: Msg):
    """
    :param msg: Messaggio che ha lanciato l'evento
    :type msg: Message
    """
    from pyrogram.types import ReplyKeyboardMarkup as Rkm
    id_ = msg.chat.id
    from ..myParameters import MY_ID
    if id_ != MY_ID:
        from asyncio import sleep
        await sleep(60*10)  # 10 min di webinar

    try:
        await msg.reply(
            text="Dopo aver visto il video sarai pieno di domande,\n"
                 "passa al prossimo step per non perdere le risposte che cerchi!"
            if await lc(id_) else "eng text : 3.6",
            reply_markup=Rkm(
                keyboard=[
                    [
                        "Vai allo step 4",  # A1
                    ],
                    [
                      "🔙 Torna ai video"  # B1
                    ],
                ],
                one_time_keyboard=False,
                resize_keyboard=True
            )
        )
    except Exception as e:
        print(f"file: step_webinar.py | funzione: continua | errore in msg.reply\n\nmsg:\n{vars(msg)}\n\n\n{vars(e)}")
