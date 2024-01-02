# Creare un lock globale per evitare concorrenza durante la scrittura del file
# lock_userlogs = threading.Lock()
def async_log(u_id, ltype: str, details: str):
    from asyncio import create_task as ct
    _ = ct(add_log(u_id, create_log_line(ltype, details)))


def create_log_line(log_type, details) -> str:
    from datetime import datetime
    datetime_ = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    return f"{datetime_} -- {log_type}:\n\t{details}"


async def add_log(user_id, messaggio):
    import csv
    import threading
    from .newuser import lock_allUser
    # Acquisire il lock prima di accedere al file
    with lock_allUser:
        # Apri il file CSV in modalità lettura
        with open("../database/allUser.csv", mode='r', newline='', encoding='utf-8') as file:
            # Leggi il file CSV
            reader = csv.DictReader(file, delimiter=';')
            # Inizializza una lista per contenere tutte le righe del CSV
            rows = list(reader)
    lock_userlogs = {}
    for row in rows:
        u_id = str(row['user_id'])
        lock_userlogs[u_id] = threading.Lock()
    # Acquisire il lock prima di accedere al file
    with lock_userlogs[str(user_id)]:
        open(f"../database/userLogs/{user_id}.log", mode="a", encoding="utf-8").write(f"{messaggio}\n\n")
