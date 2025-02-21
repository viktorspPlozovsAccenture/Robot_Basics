import os

def cancella_file(cartella):
    try:
        # Elenco di tutti i file nella cartella
        for file in os.listdir(cartella):
            percorso_file = os.path.join(cartella, file)
            # Verifica che sia un file e non una directory, e che non abbia estensione .md
            if os.path.isfile(percorso_file) and not file.endswith('.md'):
                print(f"Cancello: {file}")
                os.remove(percorso_file)
    except Exception as e:
        print(f"Errore: {e}")