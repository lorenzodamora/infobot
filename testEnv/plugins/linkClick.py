from asyncio import Lock
# Creare un lock globale per evitare concorrenza durante la scrittura del file
lock_linkClick = Lock()


async def add_click(field):
    # Acquisire il lock prima di accedere al file
    async with lock_linkClick:
        # Leggi il contenuto attuale del file
        with open("../database/linkClick.txt", "r") as file:
            lines = file.readlines()
    trovato = False
    # Cerca il campo nel file
    for i, line in enumerate(lines):
        if field in line:
            # Se il campo è presente, aggiorna il conteggio
            trovato = True
            parts = line.split(":")
            count = int(parts[1].strip())
            count += 1
            lines[i] = f"{field}: {count}\n"
            break
    # Se il campo non è presente, aggiungilo al file con il conteggio iniziale di 1
    if not trovato:
        lines.append(f"{field}: 1\n")
    # Acquisire il lock prima di accedere al file
    async with lock_linkClick:
        # Scrivi il nuovo contenuto nel file
        with open("../database/linkClick.txt", "w") as file:
            file.writelines(lines)
