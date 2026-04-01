# Scaletta Presentazione (10 minuti max)

## Slide 1 - Titolo (0:30)
Buongiorno, presento il mio progetto di TPSIT: **Stazione Meteo Smart IoT con ESP32**.
L'obiettivo e monitorare temperatura, umidita e pressione in tempo reale, salvare i dati e renderli consultabili tramite dashboard.

## Slide 2 - Problema e obiettivi (1:00)
In molti contesti (aula, laboratorio, casa) e utile controllare le condizioni ambientali.
Per questo ho progettato un sistema che:
- misura i dati con sensori;
- li visualizza localmente;
- li invia in rete;
- li salva e li pubblica.

## Slide 3 - Componenti usati (1:00)
Hardware:
- ESP32
- Sensore BMP-AHT20
- Display OLED

Software:
- MQTT (broker Mosquitto)
- Script subscriber
- Database
- Dashboard web

## Slide 4 - Schema a blocchi hardware (1:00)
Spiego il collegamento:
- sensore e OLED su bus I2C;
- ESP32 come nodo centrale;
- alimentazione via USB.

Messaggio chiave: l'ESP32 acquisisce, elabora e comunica.

## Slide 5 - Flusso dei dati (1:30)
1. Lettura sensore su ESP32.
2. Visualizzazione su OLED.
3. Pubblicazione su topic MQTT in JSON.
4. Subscriber riceve e salva su database.
5. Dashboard mostra valore attuale e storico.

Messaggio chiave: architettura completa end-to-end.

## Slide 6 - Implementazione software (1:00)
Firmware ESP32:
- connessione Wi-Fi;
- riconnessione automatica;
- ciclo periodico di lettura e publish.

Backend:
- ascolto topic MQTT;
- validazione messaggi;
- inserimento nel DB.

## Slide 7 - Demo funzionamento (2:00)
Durante la demo mostro:
- OLED con dati live;
- terminale subscriber con messaggi ricevuti;
- database che si aggiorna;
- dashboard con grafico.

Prova pratica: vario la temperatura (es. avvicino la mano al sensore) e faccio vedere la variazione in tempo reale.

## Slide 8 - Criticita e soluzioni (1:00)
- Perdita Wi-Fi: risolta con riconnessione automatica.
- Letture instabili all'avvio: risolte con validazione e gestione errori.
- Integrazione tra moduli: standardizzato formato JSON.

## Slide 9 - Conclusioni e sviluppi futuri (1:00)
Conclusione:
ho realizzato un sistema IoT completo che integra hardware, rete e software.

Sviluppi futuri:
- notifiche su soglie;
- estensione Bluetooth;
- nuovi sensori e statistiche avanzate.

## Suggerimenti per esposizione orale
- Parla per obiettivi, non per codice.
- Mostra prima lo schema, poi la demo.
- Tieni pronti screenshot di backup nel caso la rete non funzioni.
- Chiudi con una frase netta: "Obiettivo raggiunto: monitoraggio, storicizzazione e pubblicazione dati in tempo reale."

