# Relazione Progetto IoT - TPSIT 5F (a.s. 2025/26)

## Dati studente
- Nome e cognome: Pietro Verniti
- Classe: 5F
- Materia: TPSIT
- Titolo progetto: Stazione Meteo Smart IoT con ESP32, MQTT e Dashboard

## 1) Contesto e obiettivo del progetto
Il progetto nasce dall'esigenza di monitorare in modo semplice e continuo i parametri ambientali (temperatura, umidita e pressione) di un ambiente interno, ad esempio aula, laboratorio o stanza domestica.

L'obiettivo e realizzare un sistema IoT completo che:
- acquisisce i dati da sensore con ESP32;
- visualizza i valori in tempo reale su display OLED;
- trasmette i dati tramite protocollo MQTT;
- salva i dati su database;
- pubblica i dati in forma fruibile tramite dashboard/pagina web.

## 2) Specifiche funzionali
Il sistema deve rispettare le seguenti specifiche:
- Lettura periodica dei valori ambientali (intervallo configurabile, default 5 secondi).
- Visualizzazione locale su OLED di temperatura, umidita e pressione.
- Invio dei dati via Wi-Fi a un broker MQTT.
- Formato dei messaggi in JSON con timestamp.
- Ricezione lato server dei messaggi e salvataggio su database.
- Visualizzazione dello storico tramite grafico e valore corrente.
- Gestione base errori (assenza Wi-Fi, broker non raggiungibile, sensore non disponibile).

## 3) Risorse hardware e software utilizzate
### Hardware
- ESP32
- Sensore BMP-AHT20 (I2C)
- Display OLED (I2C)
- Cavi jumper, breadboard, alimentazione USB

### Software
- IDE: Arduino IDE (oppure PlatformIO)
- Protocollo di comunicazione: MQTT
- Broker MQTT: Mosquitto (in locale o su macchina remota)
- Test rete: netcat
- Backend di acquisizione: script Python subscriber MQTT
- Database: SQLite (oppure MySQL/PostgreSQL)
- Pubblicazione dati: dashboard web (Flask + Chart.js)

## 4) Architettura del sistema
Il sistema e organizzato in quattro livelli:
- **Acquisizione:** ESP32 legge i sensori.
- **Trasporto:** MQTT pubblica i dati su topic dedicato.
- **Persistenza:** un subscriber salva i dati nel database.
- **Presentazione:** la dashboard mostra dati correnti e storici.

Topic MQTT proposto:
- `5f/meteo/[cognome]/telemetria`

Payload JSON proposto:
```json
{
  "device_id": "esp32_meteo_01",
  "timestamp": "2026-04-01T10:15:00Z",
  "temperatura_c": 23.4,
  "umidita_pct": 48.2,
  "pressione_hpa": 1009.6
}
```

## 5) Descrizione del funzionamento
1. All'avvio l'ESP32 inizializza sensore e display.
2. Il dispositivo si connette alla rete Wi-Fi.
3. Si connette al broker MQTT.
4. Ogni ciclo:
   - legge i dati ambientali;
   - li mostra su OLED;
   - genera un messaggio JSON con timestamp;
   - pubblica sul topic MQTT.
5. Lo script server in ascolto sul topic riceve i messaggi.
6. Ogni messaggio viene validato e inserito nel database.
7. La dashboard interroga il database e aggiorna grafico e valori correnti.

## 6) Test eseguiti
Sono stati eseguiti i seguenti test:
- Test lettura sensore (coerenza valori a temperatura ambiente).
- Test display OLED (aggiornamento periodico senza blocchi).
- Test connessione Wi-Fi (riconnessione dopo disconnessione).
- Test pubblicazione MQTT (controllo topic e payload).
- Test subscriber + database (verifica inserimento record).
- Test dashboard (visualizzazione ultimi valori e storico).

Esito generale: sistema funzionante con acquisizione, trasmissione, salvataggio e visualizzazione dei dati.

## 7) Criticita incontrate e soluzioni adottate
- **Disconnessione Wi-Fi:** implementata logica di riconnessione automatica.
- **Dati null o instabili all'avvio:** introdotto ritardo iniziale e validazione letture.
- **Integrazione database/dashboard:** definito schema tabella semplice e endpoint dedicato ai grafici.

## 8) Sicurezza e affidabilita (livello base)
- Separazione tra rete locale e accesso esterno.
- Validazione del payload ricevuto prima del salvataggio.
- Possibilita di estendere con autenticazione MQTT utente/password e TLS.

## 9) Conclusioni
Il progetto ha permesso di realizzare un sistema IoT completo, applicando competenze hardware e software in modo integrato: acquisizione dati da sensori, comunicazione MQTT, persistenza su database e pubblicazione web.

Gli obiettivi iniziali sono stati raggiunti e il sistema risulta estendibile con nuove funzionalita.

## 10) Sviluppi futuri
- Notifiche automatiche su superamento soglie (Telegram/email).
- Uso Bluetooth per configurazione locale iniziale.
- Aggiunta di altri sensori ambientali.
- Dashboard avanzata con filtri temporali e statistiche.

