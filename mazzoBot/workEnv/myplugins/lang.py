"""
questo file contiene il get e il set della lingua del singolo utente
"""
import os
import pickle
from asyncio import Lock
from .myParameters import PREFERENCES_FILE
# Creare un lock globale per evitare concorrenza durante la scrittura del file
lock_pkl = Lock()


# Funzione per ottenere la lingua preferita di un utente
async def get_ulang(user_id) -> str:
    """
    ottiene la lingua scelta dall'utente

    intanto ci sono solo "I" & "E" (italiano e inglese)

    :param user_id: id dell'utente, che verrà convertito in stringa
    :return: la stringa della lingua, per ora default: Italiano
    :rtype: str
    """
    # Acquisire il lock prima di accedere al file
    async with lock_pkl:
        if os.path.exists(PREFERENCES_FILE):
            with open(PREFERENCES_FILE, 'rb') as file:
                preferences = pickle.load(file)
                return preferences.get(str(user_id))
        return "I"  # mai runnato


# Funzione per impostare la lingua preferita di un utente
async def set_ulang(user_id, lang: str):
    """
    imposta la lingua scelta dall'utente

    intanto ci sono solo "I" & "E" (italiano e inglese)

    :param user_id: id dell'utente, che verrà convertito in stringa
    :param lang: lingua da impostare
    :type lang: str
    :return: la stringa della lingua, per ora default: Italiano
    :rtype: str
    """
    preferences = {}
    # Acquisire il lock prima di accedere al file
    async with lock_pkl:
        if os.path.exists(PREFERENCES_FILE):
            with open(PREFERENCES_FILE, 'rb') as file:
                preferences = pickle.load(file)
        preferences[str(user_id)] = lang
        with open(PREFERENCES_FILE, 'wb') as file:
            pickle.dump(preferences, file)


async def lang_check(u_id) -> bool:
    """
    controlla la lingua dell'utente

    :param u_id: id utente
    :return: true se italiano, false inglese
    :rtype: bool
    """
    lang = await get_ulang(u_id)
    if lang == "E":
        return False
    if lang == "I":
        return True
    return False
    # raise f"errore nel get della lingua: {lang}\nu_id:{u_id}"


lc = lang_check
