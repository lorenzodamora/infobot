"""
questo file contiene il primo step informativo: il webinar

step 3
"""
from pyrogram.types import Message as Msg, InlineKeyboardMarkup as Ikm, InlineKeyboardButton as Ikb
from asyncio import sleep
from ..handler import mycontact


async def step3(msg: Msg, lc: bool):
    """Manda il link video della startUp"""
    await msg.reply(
        text="Ovviamente per iniziare a vivere la vita da film che sogni!\n"
             "Ora, vorrei stare io personalmente a spiegarti cosa intendo e tutti i dettagli, "
             "e passarti così tutta la mia energia, ma ahimè ad oggi mi viene praticamente impossibile farlo per tutti."
             "\nPerciò per fare in modo di rispettare sia il mio che il tuo tempo ho preparato questo video "
             "apposta per te!\n"
             "Il video è pieno di informazioni, perciò prendi assolutamente carta e penna!!\n"
             "    /contatto" if lc else
        "Of course, to start living the movie-like life you dream of!\n"
        "Now, I would love to personally explain to you what I mean and all the details, and pass on all my energy "
        "to you, but unfortunately, today it's practically impossible for me to do that for everyone.\n"
        "So, to ensure that I respect both my time and yours, I've prepared this video specifically for you!\n"
        "The video is packed with information, so be sure to grab pen and paper!!\n"
        "    /contact",
        reply_markup=Ikm([[
                Ikb(
                    text="VIDEO",
                    url="https://youtube.com/playlist?list=PLcm45GY4vpKDxuBf0nSZJ5j3EmLcabQyj&si=26d5TtvaQ-z3mGmb"
                )
            ]]),
        disable_web_page_preview=True,  # Disabilita l'anteprima del sito web se presente
    )
    await sleep(20)
    try:
        await mycontact(msg, lc)
    except Exception as e:
        fu = msg.from_user
        last = str(fu.last_name)
        tag = str(fu.username)
        last = "" if last == "None" else last
        tag = f" {tag}" if tag == "None" else tag
        print(f"msg:\n  id:{msg.id}\n  user id:`{fu.id}`\n  name:{fu.first_name}; {last}\n  "
              f"tag:@{tag}\n  lang:{fu.language_code}\n"
              f"Exception:{e.__class__.__name__}: {e}")
