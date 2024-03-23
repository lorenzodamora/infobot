from pyrogram.types import Message as Msg
from lang import lc
from myParameters import COMMANDS

__all__ = (
    'check_cmd1',
    'check_cmd',
    'finder_cmd',
    'mycontact',
    'valore',
)


def check_cmd1(cmd: str, comandi: dict[str, int]) -> bool:
    """
    Controlla se l'input dell'utente corrisponde a uno dei comandi specificati.

    Fa una corrispondenza key insensitive.

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
        cmd = cmd.lower()
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


def check_cmd(txt: str, name: str):
    """
    Controlla se l'input dell'utente corrisponde a uno dei comandi specificati.

    Fa una corrispondenza key insensitive.

    :param txt: Testo di input.
    :type txt: str
    :param name: key del dizionario 'commands'
        - type (int): il tipo di check da effettuare sul comando.
          - 1 '^$': 'only' cerca una corrispondenza esatta.
          - 2 '/': 'command' cerca se la stringa inizia con il testo del comando.
          - 3 '': 'within' cerca se è presente
    :type name: str
    :return: True se c'è una corrispondenza, else False.
    rtype: bool
    :raises ValueError: Se il dizionario contiene un valore non valido per il tipo di check.
    """
    name = name.lower()
    txt = txt.lower()
    value = COMMANDS[name]['type']
    for alias in COMMANDS[name]['alias']:
        alias = alias.lower()
        match value:
            case 1:
                if txt == alias:
                    return True
            case 2:
                if (txt[:len(alias) + 1].strip() + " ").startswith((alias + " ")):
                    return True
            case 3:
                if alias in txt:
                    return True
            case _:
                raise ValueError(f"Il dizionario contiene un valore non valido per il tipo di check: {value}\n"
                                 f"per i valori validi leggi la documentazione")
    return False


def finder_cmd(txt: str) -> list[str]:
    """
    trova il comando associato al testo inserito

    Fa una corrispondenza key insensitive.

    :param txt: Testo di input.
    :type txt: str
    :return: ritorna una lista con due elementi,
        [0]: comando
        [1]: log type
    :rtype: list[str]
    """
    if txt.startswith('/'):
        search_txt = txt[1:]
        logtype = "comando"
    else:
        search_txt = txt
        logtype = "testo"

    for name in COMMANDS:
        if check_cmd(search_txt, name):
            return [name, logtype]
    raise Exception("not find")


async def mycontact(msg: Msg):
    """ invia il mio contatto """
    tme = "https://t.me/Ill_Magnus"
    wa_url = ("https://wa.me/393286435255?text=Ciaoo%21%0AHo%20ricevuto%20questo%20contatto%20dal%20tuo%20bot%20su%20"
              "Telegram.%0AMolto%20piacere%21%21" if await lc(msg.from_user.id) else
              "https://wa.me/393286435255?text=Hii%21%0AI%20received%20this%20contact%20from%20your%20bot%20on%20"
              "Telegram.%0ANice%20to%20meet%20you%21%21")
    from pyrogram.enums import ParseMode as Pm
    from pyrogram.types import InlineKeyboardMarkup as Ikm, InlineKeyboardButton as Ikb
    await msg.reply(
        text=f"Per qualsiasi problema o domanda:\nEcco [il mio contatto telegram]({tme})\n"
             "\nAltri contatti:" if await lc(msg.from_user.id) else
        f"For any issues or questions:\nHere's [my Telegram contact]({tme})\n"
        "\nOther contacts:",
        parse_mode=Pm.MARKDOWN,  # Usa la formattazione Markdown
        reply_markup=Ikm([
            [Ikb(text="Whatsapp", url=wa_url)],
            [Ikb(text="Telegram", url=tme)],
            [Ikb(text="Nekogram", url="https://t.me/ill_lore")],
        ]),
        disable_web_page_preview=True,  # Disabilita l'anteprima del sito web se presente
    )


async def valore(msg: Msg):
    """Invia il testo sul valore e le inline per gli ig dei grossi leader"""
    from pyrogram.types import InlineKeyboardMarkup as Ikm, InlineKeyboardButton as Ikb
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
                 url="https://www.instagram.com/d.amora_lorenzo?"
                     "utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA==")],
        ]),
        disable_web_page_preview=True,
    )
