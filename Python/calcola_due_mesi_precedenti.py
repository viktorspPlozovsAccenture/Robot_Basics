from datetime import datetime
from dateutil.relativedelta import relativedelta

def secondo_mese_precedente():
    # Ottieni la data di oggi
    oggi = datetime.today()

    # Sottrai due mesi
    due_mesi_fa = oggi - relativedelta(months=2)

    # Restituisci la data nel formato desiderato (YYYY-MM)
    return due_mesi_fa.strftime('%Y-%m')

# Esempio di utilizzo
secondo_mese = secondo_mese_precedente()
print(f"Il secondo mese precedente è: {secondo_mese}")