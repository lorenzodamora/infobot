"""
questo file è l'event handler,
evito di usare i filter per evitare certi strani bug
"""
from asyncio import create_task as ct
from os import getenv

from chardet import detect
from pyrogram import Client
from pyrogram.types import Message as Msg
from pyrogram.raw.base import Update

from lang import lc
from log import complete_log as clog
from myParameters import CHANNEL_ID, MY_ID
from functions import *


@Client.on_message(group=0)
async def event_handler(client: Client, msg: Msg):
    def mylogger(c_id_, ltype_):
        # logga ogni on_message
        _ = ct(clog(c_id_, ltype_, f"id:{msg.id}\n\ttext:{msg.text}"))

    if msg.text:
        if str(detect(msg.text.encode())['encoding']) == 'None':
            return

    # Leggi la variabile d'ambiente e convertila in booleano (numerico)
    is_dev = getenv('dev', '0') == '1'
    cmd = msg.text.lower()
    c_id = msg.chat.id
    ltype = "\\"

    # region noreply
    if is_dev and c_id != MY_ID:
        ltype = "noreply dev"
        mylogger(c_id, ltype)
        return

    elif c_id == CHANNEL_ID:
        # se il canale manda un messaggio ignoralo
        ltype = "noreply channel"
        mylogger(c_id, ltype)
        return

    elif ((not is_dev) and c_id == MY_ID) and not check_cmd1(cmd, {f'/{MY_ID}': 2}):
        # se io mando un messaggio ignoralo
        ltype = "noreply self"
        mylogger(c_id, ltype)
        return
    # endregion

    cmdf = finder_cmd(cmd)
    ltype = cmdf[1]

    match cmdf[0]:
        case "start":  # step 1
            from .steps.startCommands import start_command
            from asyncio import sleep
            from .steps.step2_lang import imposta_lingua

            await start_command(client, msg, MY_ID)
            await sleep(1)
            await imposta_lingua(msg)

        case "help":
            from .steps.startCommands import help_command
            await help_command(msg)

        case "instagram":
            await valore(msg)

        case "lang":
            from .steps.step2_lang import imposta_lingua
            await imposta_lingua(msg)

        case "other":
            from .steps.step2_lang import msg_other
            await msg_other(msg)

        case "available langs":
            from .steps.step2_lang import set_lang
            await set_lang(msg)

        case "contact":
            await mycontact(msg)

        case "step3":
            from .steps.step3_startUp import step3
            await step3(msg)

        case "step4":
            from .steps.step4_workshop import step4
            await step4(msg)

        case "workshop":
            from .steps.step4_workshop import workshop
            await workshop(msg)

        case "step5.3" | "step5.1":
            from .steps.step5_genitori import step5
            await step5(msg)

        case 'gio&gia':
            from .steps.step5_genitori import workshop_gio_gia
            await workshop_gio_gia(msg)

        case 'step6':
            from .steps.step6_form import step6
            await step6(msg)

        case 'form':
            from .steps.step6_form import datisensibili
            await datisensibili(msg)

        case 'step7':
            from .steps.step7_webinar import step7
            await step7(msg)

        case 'end':
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

        case 'party':
            await msg.reply_text("🎉")
            ltype = "emoji"

        case _:
            # region extra
            if check_cmd1(cmd, {f'/{c_id}': 2}):
                if check_cmd1(cmd, {f'/{c_id}': 1}):
                    from .steps.step_infoExtra import step_
                    await step_(msg)
                    ltype = "sezione segreta"

                elif check_cmd1(cmd, {f'/{c_id}bzNotion': 2}):
                    from .steps.step_infoExtra import bznotion
                    await bznotion(msg)
                    ltype = "sezione segreta"

                elif check_cmd1(cmd, {f'/{c_id}presentazioni': 2, f'/{c_id}presentations': 2}):
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

    mylogger(c_id, ltype)


@Client.on_edited_message(group=1)
async def on_edited_message(_, msg):
    _ = ct(clog(msg.chat.id, "messaggio modificato", f"id:{msg.id}\n\ttext:{msg.text}"))


"""
@Client.on_raw_update(group=2)
async def on_raw_up(client: Client, update: Update, _, __):
    pass
"""
