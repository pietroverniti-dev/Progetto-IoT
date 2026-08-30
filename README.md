# ESP32‑MQTT‑Radar‑System  
Sistema radar IoT basato su **ESP32**, sensore **HC‑SR04**, **OLED**, **buzzer**, backend **MQTT + MongoDB**, server **Flask**, dashboard **web HTML** e **tester MQTT con scenari simulati**.

---

## 🎯 Panoramica del Sistema
Questo progetto implementa un **radar IoT completo**, composto da:

- **ESP32** che misura la distanza tramite ultrasuoni e pubblica via MQTT  
- **server MQTT** che riceve i dati e calcola la fascia di sicurezza  
- **MongoDB** per salvare i cambi fascia  
- **server web Flask** che espone API e dashboard  
- **dashboard HTML** per visualizzare distanza e fascia  
- **tester MQTT** che simula scenari realistici di movimento  

Il sistema è pensato per demo IoT, automazione, sicurezza, robotica e applicazioni scolastiche avanzate.

---

## 🧱 Componenti del Sistema

### 1. ESP32 Radar Unit (`esp32/`)
- Sensore ultrasuoni HC‑SR04  
- Display OLED SSD1306  
- Buzzer con logica intelligente  
- Pubblicazione MQTT del valore di distanza  
- Barra grafica su OLED  
- Riconnessione automatica WiFi + MQTT  

---

### 2. Backend MQTT + MongoDB (`server/server_mqtt.py`)
- Riceve i messaggi dal topic `radar/distanza`  
- Calcola la fascia di sicurezza:
  - <20 cm → **ROSSA**  
  - <40 cm → **GIALLA**  
  - ≥40 cm → **VERDE**  
- Salva in MongoDB **solo i cambi fascia**  
- Registra distanza + fascia + timestamp  

---

### 3. Server Web Flask (`server/server_web.py`)
Espone:

#### 🔹 Dashboard HTML  
Route:
```
/
```

#### 🔹 API REST – storico dati  
```
/api/dati
```
Restituisce gli ultimi 200 documenti salvati.

#### 🔹 API REST – dato live  
```
/api/live
```
Restituisce:
```json
{
  "distanza": <ultimo_valore>,
  "fascia": "ROSSA|GIALLA|VERDE"
}
```

---

### 4. Dashboard HTML (`server/templates/index.html`)
- Visualizza distanza e fascia  
- Aggiornamento dinamico tramite API  
- Pensata per monitoraggio realtime  

---

### 5. Tester MQTT con scenari (`tester.py`)
Simula movimenti realistici senza ESP32.

#### Scenari disponibili:
| ID | Nome |
|----|------------------------------|
| 1  | Avvicinamento graduale       |
| 2  | Oscillazione zona gialla     |
| 3  | Allarme rapido               |
| 4  | Sinusoide continua           |
| 5  | Valore manuale               |

Esempio output terminale:
```
ROSSA   12 cm  [████████████░░░░░░░░░░░░░░░░]
GIALLA  55 cm  [██████████████████░░░░░░░░░░]
VERDE  120 cm  [████████████████████████░░░░]
```

Avvio:
```
python tester.py
```

---

## 📡 MQTT Topics

Il radar pubblica la distanza su:

```
radar/distanza
```

Formato messaggio:
```
<distanza_cm>
```

---

## 🔌 Collegamenti Hardware ESP32

### HC‑SR04
- TRIG → GPIO 13  
- ECHO → GPIO 12  

### OLED SSD1306 (I2C)
- SDA → GPIO 21  
- SCL → GPIO 22  

### Buzzer
- BUZZER → GPIO 14  

---

## 🖥️ Interfaccia OLED
Il display mostra:

- stato radar  
- distanza rilevata  
- barra grafica proporzionale  

La barra si accorcia man mano che l’oggetto si avvicina.

---

## 🗄️ Database MongoDB

### Database
```
radarDB
```

### Collezione
```
fasce
```

### Documento salvato
```json
{
  "fascia": "GIALLA",
  "distanza": 32,
  "timestamp": "2026-08-30T22:38:00"
}
```

---

## 📁 Struttura della Repository

```
ESP32-MQTT-Radar-System/
│
├── esp32/
│   └── main.cpp / main.ino
│
├── server/
│   ├── server_mqtt.py
│   ├── server_web.py
│   └── templates/
│       └── index.html
│
├── tester.py
├── Images/
├── README.md
└── docs/
```

---

## 🚀 Come Avviare il Sistema

### 1. Avvia il broker MQTT  
```
mosquitto -v
```

### 2. Avvia il modulo fasce (MongoDB)  
```
python server/server_mqtt.py
```

### 3. Avvia il server web Flask  
```
python server/server_web.py
```

### 4. Carica il firmware sull’ESP32  
Inserisci SSID, password e IP del broker nel codice.

### 5. Apri la dashboard  
```
http://localhost:5000
```

### 6. (Opzionale) Avvia il tester MQTT  
```
python tester.py
```

---

## 📌 Possibili Estensioni
- Grafici storici  
- Notifiche Telegram  
- Dashboard avanzata  
- Integrazione con Home Assistant  
- LED RGB per feedback visivo  
- Logging avanzato  

---

## 📜 Licenza
Progetto sviluppato a scopo didattico e sperimentale.
