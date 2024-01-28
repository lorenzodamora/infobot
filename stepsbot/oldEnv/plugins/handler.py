"""
questo file è l'event handler, evito di usare i filter per evitare certi strani bug
"""
from pyrogram import Client
from pyrogram.types import Message as Msg
from asyncio import create_task as ct
from .log import complete_log as clog


def check_cmd(cmd: str, comandi: dict[str, str]) -> bool:
    """
    Controlla se l'input dell'utente corrisponde a uno dei comandi specificati.

    Fa una corrispondenza key sensitive.

    :param cmd: Testo di input. già lower
    :type cmd: str
    :param comandi: Dizionario contenente coppie key-value, dove:
        - Key (str): il testo del comando da cercare.
        - Value (str): il tipo di check da effettuare sul comando.
          - '^$': 'only' cerca una corrispondenza esatta.
          - '/': 'command' cerca se la stringa inizia con il testo del comando.
          - '': 'within' cerca se è presente
    :type comandi: dict[str, str]
    :return: True se c'è una corrispondenza, False altrimenti.
    :rtype: bool
    :raises ValueError: Se il dizionario contiene un valore non valido per il tipo di check.
    """
    for key, value in comandi.items():
        key = key.lower()
        # cmd = cmd.lower()
        if value == '^$':
            if cmd == key:
                return True
        elif value == '/':
            if cmd.startswith(key):
                return True
        elif value == '':
            if key in cmd:
                return True
        else:
            raise ValueError(f"Il dizionario contiene un valore non valido per il tipo di check: {value}\n"
                             f"per i valori validi leggi la documentazione")
    return False


async def mycontact(msg: Msg):
    """ invia il mio contatto """
    from .lang import lc
    id_ = msg.from_user.id
    tme = "https://t.me/Ill_Magnus"
    from pyrogram.enums import ParseMode as Pm
    from pyrogram.types import InlineKeyboardMarkup as Ikm, InlineKeyboardButton as Ikb
    await msg.reply(
        text=f"Per qualsiasi problema o domanda:\nEcco [il mio contatto telegram]({tme})\n"
             f"\nAltri contatti:" if await lc(id_) else f"eng text : 0.1",
        parse_mode=Pm.MARKDOWN,  # Usa la formattazione Markdown
        reply_markup=Ikm([
            [Ikb(text="Telegram", url=tme)],
            [Ikb(text="Whatsapp", callback_data="wa mio")],
            [Ikb(text="Instagram", callback_data="ig mio")],
        ]),
        disable_web_page_preview=True,  # Disabilita l'anteprima del sito web se presente
    )


async def valore(msg: Msg):
    """Invia il testo sul valore e le inline per gli ig dei grossi leader"""
    from pyrogram.types import InlineKeyboardMarkup as Ikm, InlineKeyboardButton as Ikb
    from .lang import lc
    id_ = msg.from_user.id
    await msg.reply(
        text="Quanto vale tutto questo?\n\n"
             "Purtroppo anche solo rispondere a questa domanda, qui per messaggio, è estremamente riduttivo..\n"
             "Perché invece non me lo chiedete in pvt? @Ill_Magnus\n"
             "Oppure potete andare a vedere i social dei miei collaboratori più veterani (in ordine di importanza):"
        if await lc(id_) else "eng text : 0.-",
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


@Client.on_message()
async def event_handler(client: Client, msg: Msg):
    from .lang import lc
    from .myParameters import CHANNEL_ID, MY_ID

    cmd = msg.text.lower()
    c_id = msg.chat.id
    ltype = "\\"

    # region noreply
    if c_id == CHANNEL_ID:
        # se il canale manda un messaggio ignoralo
        ltype = "noreply channel"

        '''
    elif c_id == MY_ID and not check_cmd(cmd, {f'/{MY_ID}': '/'}):
        # se io mando un messaggio ignoralo
        _ = ct(clog(my_id, "noreply self", f"id:{msg.id}\n\ttext:{msg.text}"))
        '''
    # endregion

    # region step 1
    elif check_cmd(cmd, {'/start': '/'}):
        from .steps.startCommands import start_command
        from asyncio import sleep
        from .steps.step2_lang import imposta_lingua
        await start_command(client, msg, MY_ID)
        await sleep(1)
        await imposta_lingua(msg)
        ltype = "comando"

    elif check_cmd(cmd, {'/h': '/', '/?': '/', '/help': '/'}):
        from .steps.startCommands import help_command
        await help_command(msg)
        ltype = "comando"
    # endregion

    elif check_cmd(cmd, {
        '/instagram': '/', '/valore': '/',
        'ig': '^$', 'intagram': '^$', 'valore': '^$'
    }):
        await valore(msg)
        ltype = "comando" if '/' == cmd[0] else "testo"

    # region step 2
    elif check_cmd(cmd, {
        '/lingua': '/', '/language': '/',
        'Set Language 🌐': '^$', 'Imposta Lingua 🌐': '^$'
    }):
        from .steps.step2_lang import imposta_lingua
        await imposta_lingua(msg)
        ltype = "comando" if '/' == cmd[0] else "testo"

    elif check_cmd(cmd, {'Other': '^$'}):
        from .steps.step2_lang import msg_other
        await msg_other(msg)
        ltype = "testo"

    elif check_cmd(cmd, {'Italiano': '^$', 'English': '^$'}):
        from .steps.step2_lang import set_lang
        await set_lang(msg)
        ltype = "testo"
    # endregion

    # region contatto
    elif check_cmd(cmd, {'/contatto': '/', '/contact': '/'}):
        await mycontact(msg)
        ltype = "comando"

    elif check_cmd(cmd, {'Contatto 👤': '^$', 'Contact 👤': '^$'}):
        await mycontact(msg)
        ltype = "testo"
    # endregion

    # region step 3
    elif check_cmd(cmd, {'Step 3': '^$', '3': '^$'}):
        from .steps.step3_webinar import step3
        await step3(msg)
        ltype = "testo"

    elif check_cmd(cmd, {'Guardo il video!': '^$', 'Webinar': '^$', '🔙 Torna ai video': '^$'}):
        from .steps.step3_webinar import tabwebinar
        await tabwebinar(msg)
        ltype = "testo"

    elif check_cmd(cmd, {'Il mio webinar Ita': '^$', 'My webinar Ita': '^$'}):
        from .steps.step3_webinar import webinarita
        await webinarita(msg)
        ltype = "testo"

    elif check_cmd(cmd, {'Il mio webinar Eng': '^$', 'My webinar Eng': '^$'}):
        from .steps.step3_webinar import webinareng
        await webinareng(msg)
        ltype = "testo"

    elif check_cmd(cmd, {'🇮🇹Webinar di Matteo Bianco': '^$', '🇮🇹Matteo Bianco\'s Webinar': '^$'}):
        from .steps.step3_webinar import webinarbianco
        await webinarbianco(msg)
        ltype = "testo"
    # endregion

    elif check_cmd(cmd, {'Vai allo step 4': '^$', 'Step 4': '^$', '4': '^$'}):
        from .steps.step4_contact import step4
        from asyncio import sleep, create_task
        _ = create_task(step4(msg))
        await sleep(3)
        await mycontact(msg)
        ltype = "testo"

    # region step 5
    elif check_cmd(cmd, {'Step 5': '^$', '5': '^$',
                         'Scrivi qua il messaggio che ti ha rivelato @Ill_Magnus': ''}):
        from .steps.step5_workshop import step5
        await step5(msg)
        ltype = "testo"

    elif check_cmd(cmd, {'ASSOLUTAMENTE SI!': '^$', 'WorkShop': '^$'}):
        from .steps.step5_workshop import workshop
        await workshop(msg)
        ltype = "testo"

    elif check_cmd(cmd, {'by Manenti': '^$', 'Mane': '^$'}):
        from .steps.step5_workshop import workshop_manenti
        await workshop_manenti(msg)
        ltype = "testo"

    elif check_cmd(cmd, {'by Trabaldo': '^$', 'GT': '^$', 'Giorgio': '^$', 'Trabaldo': '^$'}):
        from .steps.step5_workshop import workshop_giorgio
        await workshop_giorgio(msg)
        ltype = "testo"
    # endregion

    # region step 6-7-8
    elif check_cmd(cmd, {'Step 6': '^$', '6': '^$', 'Vai allo step 6': '^$'}):
        from .steps.step6_followUp2 import step6
        await step6(msg)
        ltype = "testo"

    elif check_cmd(cmd, {'Step 7': '^$', '7': '^$'}):
        from .steps.step7_genitori import step7
        await step7(msg)
        ltype = "testo"

    elif check_cmd(cmd, {'Mi interessa': '^$', 'gio&gia': '^$'}):
        from .steps.step7_genitori import workshop_gio_gia
        await workshop_gio_gia(msg)
        ltype = "testo"

    elif check_cmd(cmd, {'Step 8': '^$', '8': '^$', 'Non mi interessa': '^$'}):
        from .steps.step8_form import step8
        await step8(msg)
        ltype = "testo"

    elif check_cmd(cmd, {'Compilo il Form': '/'}):
        from .steps.step8_form import form
        await form(msg)
        ltype = "testo"

    elif check_cmd(cmd, {'/form': '/'}):
        from .steps.step8_form import datisensibili
        await datisensibili(msg)
        ltype = "comando"
    # endregion

    # region end
    elif check_cmd(cmd, {'/end': '/'}):
        from pyrogram.types import ReplyKeyboardMarkup as Rkm
        await msg.reply(
            text="Complimenti, hai usato il comando /end !",
            reply_markup=Rkm(
                keyboard=[
                    [
                        "🎉"
                    ],
                    [
                        "Set Language 🌐" if await lc(c_id) else "Imposta Lingua 🌐",  # A1
                        "Contatto 👤" if await lc(c_id) else "Contact 👤",  # A2
                    ],
                ],
                one_time_keyboard=False,
                resize_keyboard=True
            )
        )
        ltype = "comando"

    elif check_cmd(cmd, {'🎉': ''}):
        await msg.reply_text("🎉")
    # endregion

    # region extra
    elif check_cmd(cmd, {f'/{c_id}': '/'}):
        if check_cmd(cmd, {f'/{c_id}': '^$'}):
            from .steps.step9_infoExtra import step9
            await step9(msg)
            ltype = "sezione segreta"

        elif check_cmd(cmd, {f'/{c_id}bzNotion': '/'}):
            from .steps.step9_infoExtra import bznotion
            await bznotion(msg)
            ltype = "sezione segreta"

        else:
            await msg.reply_text(f"Comando non valido\nprova /{c_id}" if await lc(c_id) else f"eng text : 0.-")
            ltype = "sezione segreta non valida"
    # endregion

    else:
        await msg.reply_text("Comando non valido\nprova /start" if await lc(c_id) else f"eng text : 0.-")
        ltype = "messaggio non valido"

    # logga ogni on_message
    _ = ct(clog(c_id, ltype, f"id:{msg.id}\n\ttext:{msg.text}"))


@Client.on_edited_message()
async def on_edited_message(_, msg):
    _ = ct(clog(msg.chat.id, "messaggio modificato", f"id:{msg.id}\n\ttext:{msg.text}"))
