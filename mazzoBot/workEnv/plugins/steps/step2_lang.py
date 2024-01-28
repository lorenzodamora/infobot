"""
questo file contiene lo step del settaggio lingua

step 2
"""
from pyrogram.types import Message as Msg, ReplyKeyboardMarkup as Rkm

rm = Rkm(
    keyboard=[
        [
            "Italiano",  # A1
        ],
        [
            "English",  # B1
        ],
        [
            "Other",  # C1
        ]
    ],
    one_time_keyboard=False,
    resize_keyboard=True
)
"""tab delle lingue"""


async def imposta_lingua(msg: Msg):
    """manda la tab delle lingue"""
    await msg.reply(
        # text="Questi bottoni ti aiuteranno a navigare tra le funzionalità del bot",
        text="Imposta la tua lingua\nSet Your Language",
        reply_markup=rm
    )


async def msg_other(msg: Msg):
    """avvisa sulle lingue, e manda la tab delle linugue"""
    await msg.reply(
        text="Unfortunately, only these two languages are currently available..\n"
             "help me set up new languages! @Ill_Magnus",
        reply_markup=rm
    )


async def set_lang(msg: Msg):
    """evento per settare la lingua e inviare lo start della ReplyKeyboard"""
    from ..lang import set_ulang
    name = msg.from_user.first_name
    u_id = msg.from_user.id
    if msg.text == "Italiano":
        await msg.reply_text(f"Grazie per avermi insegnato l'italiano, {name} !!")
        await set_ulang(user_id=u_id, lang="I")

    else:
        await msg.reply_text(f"Thank you for teaching me English, {name}!")
        await set_ulang(user_id=u_id, lang="E")

    await lang_start(msg)


async def lang_start(msg: Msg):
    """tab step 3"""
    from ..lang import lc
    c_id = msg.chat.id
    await msg.reply(
        text="Iniziamo?! Siamo carichi? Io si!" if await lc(c_id) else "Shall we start?! Are we excited? I am!",
        reply_markup=Rkm(
            keyboard=[
                [
                    "Carichi per cosa?" if await lc(c_id) else "Excited for what?",  # A1
                ],
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
