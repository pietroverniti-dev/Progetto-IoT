import time
import random
import math
import paho.mqtt.client as mqtt

# ------------------------------
# CONFIG (uguale ad app.py)
# ------------------------------
MQTT_BROKER = "127.0.0.1"
MQTT_PORT   = 1883
MQTT_TOPIC  = "radar/distanza"

# ------------------------------
# SCENARI DI TEST
# ------------------------------
# Ogni scenario è una lista di (distanza_cm, durata_secondi)
SCENARI = {
    "1": {
        "nome": "Avvicinamento graduale",
        "steps": [
            (150, 3), (120, 3), (90, 3), (70, 3),
            (50, 3),  (30, 3),  (15, 3),
            (30, 2),  (60, 2),  (100, 2), (150, 2),
        ]
    },
    "2": {
        "nome": "Oscillazione zona gialla",
        "steps": [
            (85, 2), (75, 2), (65, 2), (75, 2),
            (55, 2), (45, 2), (55, 2), (85, 2),
        ]
    },
    "3": {
        "nome": "Allarme rapido",
        "steps": [
            (200, 2), (100, 1), (60, 1), (30, 1),
            (10,  2), (30, 1),  (60, 1), (200, 2),
        ]
    },
    "4": {
        "nome": "Simulazione sinusoidale continua (infinita)",
        "steps": None  # gestita separatamente
    },
    "5": {
        "nome": "Valore manuale",
        "steps": None  # input utente
    },
}

# ------------------------------
# MQTT
# ------------------------------
def crea_client():
    client = mqtt.Client()
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()
    return client

def pubblica(client, distanza):
    distanza = max(0, int(distanza))
    result = client.publish(MQTT_TOPIC, str(distanza))
    fascia = "ROSSA" if distanza < 40 else "GIALLA" if distanza < 80 else "VERDE"
    colori = {"VERDE": "\033[32m", "GIALLA": "\033[33m", "ROSSA": "\033[31m"}
    reset  = "\033[0m"
    barra  = "█" * (distanza // 5) + "░" * max(0, 30 - distanza // 5)
    print(f"  {colori[fascia]}{fascia:6s}{reset}  {distanza:4d} cm  [{barra[:30]}]")
    return result

# ------------------------------
# RUNNER SCENARI
# ------------------------------
def esegui_scenario(client, steps, intervallo=0.5):
    """Pubblica i valori di ogni step per la durata indicata."""
    for distanza, durata in steps:
        n = max(1, int(durata / intervallo))
        for _ in range(n):
            pubblica(client, distanza)
            time.sleep(intervallo)

def esegui_sinusoide(client, intervallo=0.3):
    """Onda sinusoidale continua tra 5 cm e 160 cm. Ctrl+C per fermare."""
    print("  Sinusoide attiva — premi Ctrl+C per tornare al menu\n")
    t = 0
    try:
        while True:
            # onda lenta (periodo ~30s) + piccolo rumore
            distanza = 82 + 77 * math.sin(t) + random.randint(-3, 3)
            pubblica(client, distanza)
            t += intervallo * (2 * math.pi / 30)
            time.sleep(intervallo)
    except KeyboardInterrupt:
        print("\n  Sinusoide interrotta.")

def esegui_manuale(client):
    """Input da tastiera finché l'utente non scrive 'q'."""
    print("  Digita una distanza in cm (0–250) oppure 'q' per uscire:\n")
    while True:
        raw = input("  > ").strip()
        if raw.lower() == 'q':
            break
        try:
            distanza = int(raw)
            pubblica(client, distanza)
        except ValueError:
            print("  Valore non valido. Inserisci un numero intero.")

# ------------------------------
# MENU
# ------------------------------
def stampa_menu():
    print("\n" + "═" * 48)
    print("  MQTT TEST PUBLISHER — radar/distanza")
    print("═" * 48)
    for k, v in SCENARI.items():
        print(f"  [{k}]  {v['nome']}")
    print("  [0]  Esci")
    print("═" * 48)

def main():
    print("\nConnessione al broker MQTT...")
    try:
        client = crea_client()
        print(f"  Connesso a {MQTT_BROKER}:{MQTT_PORT}  →  topic: {MQTT_TOPIC}\n")
    except Exception as e:
        print(f"  ERRORE connessione: {e}")
        return

    while True:
        stampa_menu()
        scelta = input("  Scegli uno scenario: ").strip()

        if scelta == "0":
            print("  Uscita.\n")
            break
        elif scelta in ("1", "2", "3"):
            s = SCENARI[scelta]
            print(f"\n  ▶ {s['nome']}\n")
            esegui_scenario(client, s["steps"])
            print("\n  Scenario completato.")
        elif scelta == "4":
            print(f"\n  ▶ {SCENARI['4']['nome']}\n")
            esegui_sinusoide(client)
        elif scelta == "5":
            print(f"\n  ▶ {SCENARI['5']['nome']}\n")
            esegui_manuale(client)
        else:
            print("  Scelta non valida.")

    client.loop_stop()
    client.disconnect()

if __name__ == "__main__":
    main()