import os
import pickle
from asyncio import Lock
# Creare un lock globale per evitare concorrenza durante la scrittura del file
lock_pkl = Lock()
PREFERENCES_FILE = '../database/user_preferences.pkl'


# Funzione per ottenere la lingua preferita di un utente
async def get_ulang(user_id):
    # Acquisire il lock prima di accedere al file
    async with lock_pkl:
        if os.path.exists(PREFERENCES_FILE):
            with open(PREFERENCES_FILE, 'rb') as file:
                preferences = pickle.load(file)
                return preferences.get(user_id)
        return "I"


# Funzione per impostare la lingua preferita di un utente
async def set_ulang(user_id, lang):
    preferences = {}
    # Acquisire il lock prima di accedere al file
    async with lock_pkl:
        if os.path.exists(PREFERENCES_FILE):
            with open(PREFERENCES_FILE, 'rb') as file:
                preferences = pickle.load(file)
        preferences[user_id] = lang
        with open(PREFERENCES_FILE, 'wb') as file:
            pickle.dump(preferences, file)
