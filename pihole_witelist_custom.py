import requests
import subprocess
import time

# URL del file TXT su GitHub
url = "https://raw.githubusercontent.com/paolo-hub/pi.hole_whitelist_custom/main/Whitelist_Custom.txt"

try:
    # Scarica il contenuto del file TXT
    response = requests.get(url)
    response.raise_for_status()  # Solleva un'eccezione se la richiesta non ha successo

    # Leggi il contenuto del file linea per linea
    lines = response.text.split('\n')

    # Itera sulle righe e esegui il comando pihole -b con un ritardo di 1 secondo tra i comandi
    for line in lines:
        # Ignora le linee vuote e i commenti
        if line.strip() and not line.strip().startswith("#"):
            command = f"pihole -w {line.strip()} --comment 'My Whitelist'"
            subprocess.run(command, shell=True, check=True)
            
            # Aggiungi un ritardo di 1 secondo prima di eseguire il prossimo comando
            time.sleep(1)

    print("Completato!")

except requests.exceptions.RequestException as e:
    print(f"Errore nella richiesta HTTP: {e}")

except subprocess.CalledProcessError as e:
    print(f"Errore durante l'esecuzione del comando: {e}")