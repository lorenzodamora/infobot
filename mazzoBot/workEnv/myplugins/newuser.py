"""
questo file gestisce il file 'allUser.csv'
"""
from asyncio import Lock
from csv import DictWriter, DictReader
from myParameters import ALLUSER_PATH, USERLOGS_FOLD

# Creare un lock globale per evitare concorrenza durante la scrittura del file
lock_allUser = Lock()


async def update_all_user(user_id, first_name: str, tag: str) -> list[bool | dict[str, str]] | list[bool]:
    """
    aggiorna il file all user, e crea il file 'user_id'.log

    :param user_id: id utente
    :param first_name: nome utente
    :type first_name: str
    :param tag: username utente
    :type tag: str
    :return: ritorna una lista,
        dove il primo valore è true se l'utente è nuovo,
        e se è true il secondo elemento è un dict che descrive l'utente aggiunto
    :rtype: list[bool | dict[str, str]] | list[bool]
    """
    # Converti il valore datetime in una stringa formattata
    # datetime_str = datetime_value.strftime('%d-%m-%Y %H:%M:%S')

    # Acquisire il lock prima di accedere al file
    async with lock_allUser:
        # Apri il file CSV in modalità lettura
        with open(ALLUSER_PATH, 'r', newline='', encoding='utf-8') as file:
            # Leggi il file CSV
            reader = DictReader(file, delimiter=';')
            # Inizializza una lista per contenere tutte le righe del CSV
            rows = list(reader)

    # Indica se l'utente è già presente nel file
    utente_presente = False

    # Itera attraverso le righe del CSV
    usr = str(user_id)
    for row in rows:
        # Se l'ID utente è presente
        r = str(row['user_id'])
        if r == usr:
            utente_presente = True

            # Se il nome utente è cambiato, aggiorna il nome
            if row['first_name'] != first_name:
                row['first_name'] = first_name
            # Se il tag è cambiato, aggiorna il tag
            if row['tag'] != tag:
                row['tag'] = tag

    # Se l'utente non è presente, aggiungi una nuova riga
    if not utente_presente:
        from datetime import datetime
        dt_str = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        nuova_riga = {'user_id': usr, 'first_name': first_name, 'tag': tag, 'datetime': dt_str}
        rows.append(nuova_riga)
        # crea file di log
        open(f"{USERLOGS_FOLD}/{usr}.log", "w").close()
        ret = [True, nuova_riga]
    else:
        ret = [False]

    # Acquisire il lock prima di accedere al file
    async with lock_allUser:
        # Scrivi nel file CSV aggiornato
        with open(ALLUSER_PATH, 'w', newline='', encoding='utf-8') as file:
            # Scrivi le righe aggiornate nel file
            writer = DictWriter(file, fieldnames=['user_id', 'first_name', 'tag', 'datetime'], delimiter=';')
            writer.writeheader()
            writer.writerows(rows)

    return ret
