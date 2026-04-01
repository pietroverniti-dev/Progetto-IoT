# Schemi da inserire nella presentazione

## 1) Schema a blocchi hardware

```text
+-------------------+        I2C        +------------------+
|  Sensore BMP-AHT20|<----------------->|      ESP32       |
| (Temp/Umid/Press) |                   | (controllo logica)|
+-------------------+                   +------------------+
                                              |
                                              | I2C
                                              v
                                       +-------------+
                                       | OLED Display|
                                       +-------------+
                                              |
                                              | Wi-Fi
                                              v
                                       +-------------+
                                       | MQTT Broker |
                                       +-------------+
```

Note da dire:
- ESP32 e il nodo centrale.
- Sensore e display condividono il bus I2C.
- La trasmissione dati esterna avviene via Wi-Fi/MQTT.

## 2) Schema flusso logico dei dati

```text
[Acquisizione]
ESP32 legge BMP-AHT20 ogni N secondi
        |
        v
[Visualizzazione locale]
Aggiorna OLED con valori correnti
        |
        v
[Pubblicazione rete]
Invio JSON su topic MQTT
        |
        v
[Ingestione server]
Subscriber riceve messaggio
        |
        v
[Persistenza]
Inserimento record nel Database
        |
        v
[Fruizione]
Dashboard mostra real-time + storico
```

## 3) Schema software (moduli)

```text
Firmware ESP32
- setup sensore/OLED
- connessione Wi-Fi
- connessione MQTT
- loop lettura + publish

Backend
- client MQTT subscriber
- parser/validazione JSON
- writer DB

Frontend
- API lettura dati
- dashboard con grafici
```

## 4) Tabella rapida I/O del sistema

| Tipo | Nome | Descrizione |
|---|---|---|
| Input | Temperatura | Misura dal sensore |
| Input | Umidita | Misura dal sensore |
| Input | Pressione | Misura dal sensore |
| Output | OLED | Valori in tempo reale |
| Output | MQTT | Telemetria in JSON |
| Output | Database | Storico misure |
| Output | Dashboard | Visualizzazione utente |

## 5) Frase pronta per spiegare l'architettura
"Il sistema segue una pipeline IoT completa: sensore -> edge device (ESP32) -> protocollo MQTT -> storage su database -> pubblicazione su dashboard."

