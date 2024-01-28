"""
questo file è l'event handler, evito di usare i filter per evitare certi strani bug
"""
from pyrogram import Client
from pyrogram.types import Message as Msg
from asyncio import create_task as ct
from .log import complete_log as clog


def check_cmd(cmd: str, comandi: dict[str, int]) -> bool:
    """
    Controlla se l'input dell'utente corrisponde a uno dei comandi specificati.

    Fa una corrispondenza key sensitive.

    :param cmd: Testo di input. già lower
    :type cmd: str
    :param comandi: Dizionario contenente coppie key-value, dove:
        - Key (str): il testo del comando da cercare.
        - Value (int): il tipo di check da effettuare sul comando.
          - 1 '^$': 'only' cerca una corrispondenza esatta.
          - 2 '/': 'command' cerca se la stringa inizia con il testo del comando.
          - 3 '': 'within' cerca se è presente
    :type comandi: dict[str, int]
    :return: True se c'è una corrispondenza, False altrimenti.
    :rtype: bool
    :raises ValueError: Se il dizionario contiene un valore non valido per il tipo di check.
    """
    for key, value in comandi.items():
        key = key.lower()
        # cmd = cmd.lower()
        match value:
            case 1:
                if cmd == key:
                    return True
            case 2:
                if cmd.startswith(key):
                    return True
            case 3:
                if key in cmd:
                    return True
            case _:
                raise ValueError(f"Il dizionario contiene un valore non valido per il tipo di check: {value}\n"
                                 f"per i valori validi leggi la documentazione")
    return False


async def mycontact(msg: Msg):
    """ invia il mio contatto """
    from .lang import lc
    tme = "https://t.me/Ill_Magnus"
    from pyrogram.enums import ParseMode as Pm
    from pyrogram.types import InlineKeyboardMarkup as Ikm, InlineKeyboardButton as Ikb
    await msg.reply(
        text=f"Per qualsiasi problema o domanda:\nEcco [il mio contatto telegram]({tme})\n"
             "\nAltri contatti:" if await lc(msg.from_user.id) else
        f"For any issues or questions:\nHere's [my Telegram contact]({tme})\n"
        "\nOther contacts:",
        parse_mode=Pm.MARKDOWN,  # Usa la formattazione Markdown
        reply_markup=Ikm([
            [Ikb(text="Whatsapp", url="https://wa.me/message/WEMT77WGHU4WF1")],
            [Ikb(text="Telegram", url=tme)],
            [Ikb(text="Nekogram", url="https://t.me/ill_lore")],
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
        if await lc(id_) else
        "How much is all this worth?\n\n"
        "Unfortunately, just answering this question via text is extremely limiting..\n"
        "Why not ask me privately? @Ill_Magnus.\n"
        "Or you can check out the socials of my more seasoned collaborators (in order of importance):",
        reply_markup=Ikm([
            [Ikb(text="GIORGIO TRABALDO",
                 url="https://www.instagram.com/giorgiotrabaldo?utm_source=ig_web_button_share_sheet"
                     "&igsh=OGQ5ZDc2ODk2ZA==")],
            [Ikb(text="MATTEO BIANCO",
                 url="https://www.instagram.com/matteobianco_papi?utm_source=ig_web_button_share_sheet"
                     "&igsh=OGQ5ZDc2ODk2ZA==")],
            [Ikb(text="MAURO BOCCOMINO",
                 url="https://www.instagram.com/mauro_boccomino?utm_source=ig_web_button_share_sheet"
                     "&igsh=OGQ5ZDc2ODk2ZA==")],
            [Ikb(text="ANDREA TRAINA",
                 url="https://www.instagram.com/andreatraina_?utm_source=ig_web_button_share_sheet&"
                     "igsh=OGQ5ZDc2ODk2ZA==")],
            [Ikb(text="MATTEO DEPRETIS",
                 url="https://www.instagram.com/matteo.depetris?utm_source=ig_web_button_share_sheet&"
                     "igsh=OGQ5ZDc2ODk2ZA==")],
            [Ikb(text="DYLAN DAGANI",
                 url="https://www.instagram.com/dylandagani?utm_source=ig_web_button_share_sheet"
                     "&igsh=OGQ5ZDc2ODk2ZA==")],
            [Ikb(text="MARCO MANENTI",
                 url="https://www.instagram.com/marcomanentii?utm_source=ig_web_button_share_sheet"
                     "&igsh=OGQ5ZDc2ODk2ZA==")],
            [Ikb(text="MANUEL MAZZOLA",
                 url="https://www.instagram.com/manuel_mazzola_?utm_source=ig_web_button_share_sheet&"
                     "igsh=OGQ5ZDc2ODk2ZA==")],
            [Ikb(text=f"LORENZO D'AMORA {'(io)' if await lc(id_) else '(me)'}",
                 url="google.com/search?q=wip")],
        ]),
        disable_web_page_preview=True,
    )


@Client.on_message()
async def event_handler(client: Client, msg: Msg):
    from .lang import lc
    from .myParameters import CHANNEL_ID, MY_ID

    if msg.text:
        import chardet
        result = chardet.detect(msg.text.encode())
        if str(result['encoding']) == 'None':
            return

    cmd = msg.text.lower()
    c_id = msg.chat.id
    ltype = "\\"

    # region noreply
    if c_id == CHANNEL_ID:
        # se il canale manda un messaggio ignoralo
        ltype = "noreply channel"

    elif c_id == MY_ID and not check_cmd(cmd, {f'/{MY_ID}': 2}):
        # se io mando un messaggio ignoralo
        _ = ct(clog(MY_ID, "noreply self", f"id:{msg.id}\n\ttext:{msg.text}"))
    # endregion

    # region step 1
    elif check_cmd(cmd, {'/start': 2}):
        from .steps.startCommands import start_command
        from asyncio import sleep
        from .steps.step2_lang import imposta_lingua
        await start_command(client, msg, MY_ID)
        await sleep(1)
        await imposta_lingua(msg)
        ltype = "comando"

    elif check_cmd(cmd, {'/h': 2, '/?': 2, '/help': 2}):
        from .steps.startCommands import help_command
        await help_command(msg)
        ltype = "comando"
    # endregion

    elif check_cmd(cmd, {
        '/instagram': 2, '/valore': 2,
        'ig': 1, 'instagram': 1, 'valore': 1
    }):
        await valore(msg)
        ltype = "comando" if 2 == cmd[0] else "testo"

    # region step 2
    elif check_cmd(cmd, {
        '/lingua': 2, '/language': 2, '/lang': 2,
        'Set Language 🌐': 1, 'Imposta Lingua 🌐': 1
    }):
        from .steps.step2_lang import imposta_lingua
        await imposta_lingua(msg)
        ltype = "comando" if 2 == cmd[0] else "testo"

    elif check_cmd(cmd, {'Other': 1}):
        from .steps.step2_lang import msg_other
        await msg_other(msg)
        ltype = "testo"

    elif check_cmd(cmd, {'Italiano': 1, 'English': 1}):
        from .steps.step2_lang import set_lang
        await set_lang(msg)
        ltype = "testo"
    # endregion

    # region contatto
    elif check_cmd(cmd, {'/contatto': 2, '/contact': 2}):
        await mycontact(msg)
        ltype = "comando"

    elif check_cmd(cmd, {'Contatto 👤': 1, 'Contact 👤': 1}):
        await mycontact(msg)
        ltype = "testo"
    # endregion

    # region step 3-4
    elif check_cmd(cmd, {'Carichi per cosa?': 1, 'Excited for what?': 1,
                         'StartUp': 3, 'Step 3': 1, '3': 1}):
        from .steps.step3_startUp import step3
        await step3(msg)
        ltype = "testo"

    elif check_cmd(cmd, {'Step 4': 1, '4': 1}):
        from .steps.step4_workshop import step4
        await step4(msg)
        ltype = "testo"

    elif check_cmd(cmd, {'workshop': 3, 'ASSOLUTAMENTE SI!': 1, 'ABSOLUTELY YES!': 1}):
        from .steps.step4_workshop import workshop
        await workshop(msg)
        ltype = "testo"
    # endregion

    # region step 5
    elif check_cmd(cmd, {'genitor': 3, 'parent': 3, 'Step 5': 1, '5': 1}):
        from .steps.step5_genitori import step5
        await step5(msg)
        ltype = "testo"

    elif check_cmd(cmd, {'Mi interessa': 1, 'I\'m interested': 1, 'gio&gia': 1}):
        from .steps.step5_genitori import workshop_gio_gia
        await workshop_gio_gia(msg)
        ltype = "testo"
    # endregion

    # region step 6-7
    elif check_cmd(cmd, {'Step 6': 1, '6': 1, 'Non mi interessa': 1, 'I\'m not interested': 1}):
        from .steps.step6_form import step6
        await step6(msg)
        ltype = "testo"

    elif check_cmd(cmd, {'/form': 2}):
        from .steps.step6_form import datisensibili
        await datisensibili(msg)
        ltype = "comando"

    elif check_cmd(cmd, {'webinar': 3, 'Step 7': 1, '7': 1}):
        from .steps.step7_webinar import step7
        await step7(msg)
        ltype = "testo"
    # endregion

    # region end
    elif check_cmd(cmd, {'/end': 2}):
        from pyrogram.types import ReplyKeyboardMarkup as Rkm
        await msg.reply(
            text="Complimenti, hai usato il comando /end !" if await lc(c_id) else
            "Congratulations, you used the /end command!",
            reply_markup=Rkm(
                keyboard=[
                    [
                        "🎉"
                    ],
                ],
                one_time_keyboard=False,
                resize_keyboard=True
            )
        )
        ltype = "comando"

    elif check_cmd(cmd, {'🎉': 3}):
        await msg.reply_text("🎉")
    # endregion

    # region extra
    elif check_cmd(cmd, {f'/{c_id}': 2}):
        if check_cmd(cmd, {f'/{c_id}': 1}):
            from .steps.step_infoExtra import step_
            await step_(msg)
            ltype = "sezione segreta"

        elif check_cmd(cmd, {f'/{c_id}bzNotion': 2}):
            from .steps.step_infoExtra import bznotion
            await bznotion(msg)
            ltype = "sezione segreta"

        elif check_cmd(cmd, {f'/{c_id}presentazioni': 2, f'/{c_id}presentations': 2}):
            from .steps.step_infoExtra import presentazioni
            await presentazioni(msg)
            ltype = "sezione segreta"

        else:
            await msg.reply_text(f"Comando non valido\nprova /{c_id}" if await lc(c_id) else
                                 f"Invalid command\ntry /{c_id}")
            ltype = "sezione segreta non valida"
    # endregion

    else:
        await msg.reply_text("Comando non valido\nprova /start" if await lc(c_id) else
                             "Invalid command\ntry /start")
        ltype = "messaggio non valido"

    # logga ogni on_message
    _ = ct(clog(c_id, ltype, f"id:{msg.id}\n\ttext:{msg.text}"))


@Client.on_edited_message()
async def on_edited_message(_, msg):
    _ = ct(clog(msg.chat.id, "messaggio modificato", f"id:{msg.id}\n\ttext:{msg.text}"))
