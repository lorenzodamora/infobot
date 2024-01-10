# Creare un lock globale per evitare concorrenza durante la scrittura del file
# lock_userlogs = threading.Lock()
lock_userLogs = {}


async def complete_log(u_id, ltype: str, details: str):
    await add_log(u_id, create_log_line(ltype, details))


def create_log_line(log_type, details) -> str:
    from datetime import datetime
    datetime_ = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    return f"{datetime_} -- {log_type}:\n\t{details}"


'''
async def add_log1(user_id, messaggio):
    import csv
    # import threading
    from asyncio import Lock
    from .newuser import lock_allUser
    # Acquisire il lock prima di accedere al file
    async with lock_allUser:
        # Apri il file CSV in modalità lettura
        with open("../database/allUser.csv", mode='r', newline='', encoding='utf-8') as file:
            # Leggi il file CSV
            reader = csv.DictReader(file, delimiter=';')
            # Inizializza una lista per contenere tutte le righe del CSV
            rows = list(reader)
    global lock_userlogs
    id_channel = str(-1002054102325)
    if not lock_userlogs[id_channel]:
        lock_userlogs[id_channel] = Lock()
    for row in rows:
        u_id = str(row['user_id'])
        if not lock_userlogs[u_id]:
            lock_userlogs[u_id] = Lock()
    # Acquisire il lock prima di accedere al file
    async with lock_userlogs[str(user_id)]:
        open(f"../database/userLogs/{user_id}.log", mode="a", encoding="utf-8").write(f"{messaggio}\n\n")
'''


async def add_log(user_id, messaggio):
    from asyncio import Lock
    global lock_userLogs
    u_id = str(user_id)
    # crea il lock se non esiste
    if u_id not in lock_userLogs:
        lock_userLogs[u_id] = Lock()
    # Acquisire il lock prima di accedere al file
    async with lock_userLogs[u_id]:
        open(f"../database/userLogs/{u_id}.log", mode="a", encoding="utf-8").write(f"{messaggio}\n\n")
