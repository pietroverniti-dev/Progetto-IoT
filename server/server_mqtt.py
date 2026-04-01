from datetime import datetime
from pymongo import MongoClient
import paho.mqtt.client as mqtt

# ------------------------------
# CONFIG
# ------------------------------
MQTT_BROKER = "127.0.0.1"
MQTT_PORT = 1883
MQTT_TOPIC = "radar/distanza"

MONGO_URL = "mongodb://127.0.0.1:27017"
DB_NAME = "radarDB"
COLLECTION_NAME = "fasce"

# ------------------------------
# MONGO
# ------------------------------
mongo = MongoClient(MONGO_URL)
db = mongo[DB_NAME]
collection = db[COLLECTION_NAME]

# ------------------------------
# LOGICA FASCE
# ------------------------------
fascia_corrente = None

def calcola_fascia(distanza):
    if distanza < 20:
        return "ROSSA"
    elif distanza < 40:
        return "GIALLA"
    else:
        return "VERDE"

# ------------------------------
# MQTT CALLBACKS
# ------------------------------
def on_connect(client, userdata, flags, rc):
    print("MQTT connesso con codice:", rc)
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    global fascia_corrente

    try:
        distanza = int(msg.payload.decode())
    except ValueError:
        print("Valore non valido:", msg.payload)
        return

    nuova_fascia = calcola_fascia(distanza)

    # Salva SOLO se cambia fascia
    if nuova_fascia != fascia_corrente:
        fascia_corrente = nuova_fascia
        doc = {
            "fascia": nuova_fascia,
            "distanza": distanza,
            "timestamp": datetime.now()
        }
        collection.insert_one(doc)
        print("CAMBIO FASCIA:", doc)

# ------------------------------
# MAIN
# ------------------------------
if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    print("Server MQTT in ascolto su", MQTT_TOPIC)
    client.loop_forever()
