"""
questo file gestisce i files di logs
"""
# Creare un lock globale per evitare concorrenza durante la scrittura del file
# lock_userlogs = threading.Lock()
lock_userLogs = {}


async def complete_log(u_id, ltype: str, details: str):
    """
    shortcut per aggiungere un log

    guarda le funzioni :func:`create_log_line` e :func:`add_log`

    :param u_id: id utente
    :param ltype: log_type di :func:`create_log_line`
    :type ltype: str
    :param details: details di :func:`create_log_line`
    :type details: str
    """
    await add_log(u_id, create_log_line(ltype, details))


def create_log_line(log_type: str, details: str) -> str:
    """
    crea la linea standard di log

    :param log_type: tipo di log
    :type log_type: str
    :param details: dettagli del log
    :type details: str
    :return: ritorna le linee di log
    :rtype: str
    """
    from datetime import datetime
    datetime_ = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    return f"{datetime_} -- {log_type}:\n\t{details}"


async def add_log(user_id, msg: str):
    """
    aggiunge il log al file 'user_id'.log

    :param user_id: id utente che sarà il nome del file .log
    :param msg: testo del log
    :type msg: str
    """
    from asyncio import Lock
    global lock_userLogs
    u_id = str(user_id)
    # crea il lock se non esiste
    if u_id not in lock_userLogs:
        lock_userLogs[u_id] = Lock()
    # Acquisire il lock prima di accedere al file
    async with lock_userLogs[u_id]:
        # file creato in ./newuser.py
        open(f"../database/userLogs/{u_id}.log", mode="a", encoding="utf-8").write(f"{msg}\n\n")
