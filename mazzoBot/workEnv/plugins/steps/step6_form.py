"""
questo file contiene il form

step 6
"""
from pyrogram.types import Message as Msg, InlineKeyboardMarkup as Ikm, InlineKeyboardButton as Ikb
from ..lang import lc


async def step6(msg: Msg):
    await msg.reply(
        text="Abbiamo praticamente già finito, non è fantastico?!\n\n"
             "Compila questo questionario se vuoi la possibilità di essere scelto come nostro collaboratore!\n"
             "Se hai qualche dubbio prova a cliccare /form oppure contattami! @Ill_Magnus"
        if await lc(msg.chat.id)
        else "We've practically finished already, isn't it fantastic?!\n\n"
             "Fill out this questionnaire if you want the chance to be chosen as our collaborator!\n"
             "If you have any doubts, try clicking /form or contact me! @Ill_Magnus",
        reply_markup=Ikm([[
            Ikb(
                text="FORM",
                url="google.com/search?q=wip"
            )
        ]]),
        disable_web_page_preview=True,  # Disabilita l'anteprima del sito web se presente
    )


# /form
async def datisensibili(msg: Msg):
    """Invia una spiegazione sui dati sensibili richiesti nel form"""
    await msg.reply(
        text="Nel form sono richiesti alcuni dati sensibili, come il numero di telefono e altri..\n"
             "Se hai delle preoccupazioni in merito, voglio tranquillizzarti immediatamente:\n i tuoi dati sono "
             "tutelati dalla legge dal Regolamento Generale sulla Protezione dei Dati (GDPR) dell'Unione Europea.\n"
             "Saranno utilizzati esclusivamente per permetterci di contattarti tramite WhatsApp, "
             "dove avremo l'opportunità di approfondire la nostra conoscenza reciprocamente in un contesto amichevole"
             " e di completare il processo informativo.\n\nInoltre, non effettueremo controlli sulla correttezza dei "
             "dati forniti, confidiamo nella vostra onestà in questo senso.\n"
             "La tua privacy è importante per noi.\n\nAvevo in mente un discorso, perciò l'ho scritto:\n"
             " Per rendersi la vita come un film bisogna rischiare come in un film, perciò: hai paura di dare il "
             "numero di telefono? Meglio! significa che non sei stupido, avventato o poco sveglio.\n Ma solo chi si "
             "mette in gioco avrà i risultati che cerca nella vita. La scelta è tua."
        if await lc(msg.from_user.id) else
        "The form requires some sensitive data, such as your phone number and more.\n"
        "If you have concerns about this, I want to reassure you immediately:\n"
        "Your data is protected by the General Data Protection Regulation (GDPR) of the European Union.\n"
        "It will be used exclusively to contact you via WhatsApp, where we'll have the opportunity to deepen our "
        "mutual understanding in a friendly context and complete the information process.\n\n"
        "Furthermore, we won't verify the accuracy of the provided data, trusting your honesty in this regard.\n"
        "Your privacy is important to us.\n\n"
        "I had a thought, so I wrote it down:\n"
        "To make life like a movie, you must take risks as in a movie. So, are you afraid to give your phone number? "
        "Better! It means you're not foolish, reckless, or unaware.\n"
        " But only those who take risks will achieve the results they seek in life. The choice is yours."
    )
