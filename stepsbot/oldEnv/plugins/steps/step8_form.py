"""
questo file contiene il form

step 8
"""
from pyrogram.types import Message as Msg
from ..lang import lc


async def step8(msg: Msg):
    """
    :param msg: Messaggio che ha lanciato l'evento
    :type msg: Message
    """
    from pyrogram.types import ReplyKeyboardMarkup as Rkm
    id_ = msg.chat.id
    await msg.reply(
        text="Abbiamo praticamente già finito, non è fantastico?!\n"
             "Ora devi solo compilare questo form, se hai dei dubbi chiedi direttamente a @Ill_Magnus"
        if await lc(id_) else "eng text : 8.1",
        reply_markup=Rkm(
            keyboard=[
                [
                    "Compilo il Form!!",  # A1
                ],
                [
                    "Set Language 🌐" if await lc(id_) else "Imposta Lingua 🌐",  # C1
                    "Contatto 👤" if await lc(id_) else "Contact 👤",  # C2
                ],
            ],
            one_time_keyboard=False,
            resize_keyboard=True
        )
    )


async def form(msg: Msg):
    """
    :param msg:
    :type msg: Message
    """
    from pyrogram.types import InlineKeyboardMarkup as Ikm, InlineKeyboardButton as Ikb
    msg = await msg.reply(
        text="Compila questo questionario se vuoi la possibilità di essere scelto come nostro collaboratore!\n"
             "Se hai qualche dubbio prova a cliccare /form oppure contattami! @Ill_Magnus"
        if await lc(msg.from_user.id) else f"eng text : 8.2",
        reply_markup=Ikm([[Ikb(text="FORM", callback_data="form")]]),
        disable_web_page_preview=True,  # Disabilita l'anteprima del sito web se presente
    )
    from asyncio import sleep
    await sleep(1)
    await msg.reply_text("Una volta compilato il form verrai contattato dal nostro personale per ricevere l'esito!\n"
                         "Fatti vedere disponibile!")


# /form
async def datisensibili(msg: Msg):
    """Invia una spiegazione sui dati sensibili richiesti nel form"""
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
              "mette in gioco avrà i risultati che cerca nella vita. La scelta è tua.")
        if await lc(msg.from_user.id) else "eng text : 8.3"
    )
