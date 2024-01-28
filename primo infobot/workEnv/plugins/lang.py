"""
questo file contiene il get e il set della lingua del singolo utente
"""
import os
import pickle
from asyncio import Lock
# Creare un lock globale per evitare concorrenza durante la scrittura del file
lock_pkl = Lock()
PREFERENCES_FILE = '../database/user_preferences.pkl'


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
        return "I"


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
