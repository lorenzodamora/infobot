import csv
from asyncio import Lock
# Creare un lock globale per evitare concorrenza durante la scrittura del file
lock_allUser = Lock()


async def update_all_user(user_id, first_name, tag, datetime_value):
    # Converti il valore datetime in una stringa formattata
    datetime_str = datetime_value.strftime('%d-%m-%Y %H:%M:%S')

    # Acquisire il lock prima di accedere al file
    async with lock_allUser:
        # Apri il file CSV in modalità lettura
        with open("../database/allUser.csv", mode='r', newline='', encoding='utf-8') as file:
            # Leggi il file CSV
            reader = csv.DictReader(file, delimiter=';')
            # Inizializza una lista per contenere tutte le righe del CSV
            rows = list(reader)

    # Indica se l'utente è già presente nel file
    utente_presente = False

    # Itera attraverso le righe del CSV
    for row in rows:
        # Se l'ID utente è presente
        r = str(row['user_id'])
        us = str(user_id)
        if r == us:
            utente_presente = True

            # Se il nome utente è cambiato, aggiorna il nome
            if row['first_name'] != first_name:
                row['first_name'] = first_name
            # Se il tag è cambiato, aggiorna il tag
            if row['tag'] != tag:
                row['tag'] = tag

    # Se l'utente non è presente, aggiungi una nuova riga
    if not utente_presente:
        nuova_riga = {'user_id': user_id, 'first_name': first_name, 'tag': tag, 'datetime': datetime_str}
        rows.append(nuova_riga)
        # crea file di log
        open(f"../database/userLogs/{user_id}.log", "w").close()
        ret = [True, nuova_riga]
    else:
        ret = [False]

    # Acquisire il lock prima di accedere al file
    async with lock_allUser:
        # Scrivi nel file CSV aggiornato
        with open("../database/allUser.csv", mode='w', newline='', encoding='utf-8') as file:
            # Scrivi le righe aggiornate nel file
            writer = csv.DictWriter(file, fieldnames=['user_id', 'first_name', 'tag', 'datetime'], delimiter=';')
            writer.writeheader()
            writer.writerows(rows)

    return ret
