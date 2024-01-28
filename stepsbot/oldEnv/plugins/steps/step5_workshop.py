"""
questo file contiene il secondo step informativo: i workshop

step 5
"""
from pyrogram.types import Message as Msg
from ..lang import lc


async def step5(msg: Msg):
    """
    :param msg: Messaggio che ha lanciato l'evento
    :type msg: Message
    """
    from pyrogram.types import ReplyKeyboardMarkup as Rkm
    c_id = msg.chat.id
    await msg.reply(
        text="Sei carico per il prossimo video?"
        if await lc(c_id) else "eng text : 5.1",
        reply_markup=Rkm(
            keyboard=[
                [
                    "ASSOLUTAMENTE SI!",  # A1
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


async def workshop(msg: Msg):
    """Manda la tab dei WorkShop"""
    from pyrogram.types import ReplyKeyboardMarkup as Rkm
    id_ = msg.from_user.id
    await msg.reply(
        text="Ad oggi, come avrai già ben capito, l'azienda BE offre due macroaree di metodi per guadagnare.\n"
             "Sia che tu voglia sapere di più su uno, sull'altro, o su entrambi, ti consiglio di guardare bene "
             "entrambi i seguenti video, per non perdere le informazioni o le risposte alle domande che magari ti "
             "frullano nella testa da giorni oppure anche da pochi secondi" if await lc(id_) else "eng text : 5.-",
        reply_markup=Rkm(
            keyboard=[
                [
                    "by Manenti" if await lc(id_) else "eng text : 5.-",  # A1
                ],
                [
                    "by Trabaldo" if await lc(id_) else "eng text : 5.-",  # B1
                ],
                [
                    "Vai allo step 6" if await lc(id_) else "eng text : 5.-",  # C1
                ],
            ],
            one_time_keyboard=False,
            resize_keyboard=True)
    )


async def workshop_manenti(msg: Msg):
    """ // """
    from pyrogram.types import InlineKeyboardMarkup as Ikm, InlineKeyboardButton as Ikb
    await msg.reply(
        text=f"invia il workshop di Mane, è vecchio, magari aspetto che lo rifà, o che qualcuno faccia un workshop "
             f"come quelli del giovedì"
        if await lc(msg.from_user.id) else f"eng text : 5.-",
        disable_web_page_preview=True
    )
    '''
        reply_markup=Ikm([
            [Ikb(text="WORKSHOP",
                 # url = https://youtube.com/playlist?list=
                 callback_data="workshop manenti")],
            [Ikb(text="INSTAGRAM MARCO MANENTI",
                 # url = https://www.instagram.com/ ?
                 #       utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA==,
                 callback_data="ig manenti from workshop")],
        ]),
    '''


async def workshop_giorgio(msg: Msg):
    """invia il workshop di giorgio fatto al post evento di Vienna"""
    from pyrogram.types import InlineKeyboardMarkup as Ikm, InlineKeyboardButton as Ikb
    await msg.reply(
        text=f"Questo workshop è stato registrato da parte del nostro leader di riferimento, e vi andrà a dare tutte "
             f"le informazioni necessarie per capire tutto al meglio.\n"
             f"è tutto quello che non volete assolutamente perdere:" if await lc(msg.from_user.id)
        else f"eng text : 5.-",
        reply_markup=Ikm([
            [Ikb(text="WORKSHOP",
                 # url = https://youtube.com/playlist?list=PLcm45GY4vpKBL4quIBcQPcYcQChPQ_aqA&si=ybee2BRhV70PduIT
                 callback_data="workshop giorgio")],
            [Ikb(text="INSTAGRAM GIORGIO TRABALDO",
                 # url="https://www.instagram.com/giorgiotrabaldo?"
                 # "utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA==",
                 callback_data="ig giorgio from workshop")],
            [Ikb(text="TIK-TOK GIORGIO TRABALDO",
                 # url="https://www.tiktok.com/@giorgiotrabaldo?_t=8ifrWVfS3yz&_r=1",
                 callback_data="tt giorgio from workshop")],
        ]),
        disable_web_page_preview=True,
    )
