from pyrogram import Client, filters as f
from pyrogram.types import ReplyKeyboardMarkup as Rkm


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


@Client.on_message(f.command("start"), group=1)
@Client.on_message(f.regex("Set Language 🌐") | f.regex("Imposta Lingua 🌐"), group=0)
async def start_rkm(_, msg):
    await msg.reply(
        # text="Questi bottoni ti aiuteranno a navigare tra le funzionalità del bot",
        text="Imposta la tua lingua\nSet Your Language",
        reply_markup=rm
    )


@Client.on_message(f.regex("Other"), group=0)
async def msg_other(_, msg):
    await msg.reply(
        text="Unfortunately, only these two languages are currently available..\n"
             "help me set up new languages! @Ill_Magnus",
        reply_markup=rm
    )
