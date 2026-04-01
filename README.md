# Progetto IoT - TPSIT 5F

Stazione meteo smart con `ESP32`, sensore `BMP-AHT20`, `OLED`, protocollo `MQTT`, salvataggio su database e pubblicazione dati su dashboard.

## Interfaccia grafica HTML
<img src="Images\Interfaccia.png" alt="Descrizione" style="float: right; width: 300px; height: auto; margin-left: 10px;">

_Schermata della dashboard HTML per la visualizzazione dei dati in tempo reale._

## Panoramica
Questo repository contiene il materiale del progetto personale IoT per TPSIT (a.s. 2025/26).

Obiettivi principali:
- acquisire dati ambientali (temperatura, umidita, pressione);
- mostrare i dati in locale su display OLED;
- inviare i dati via MQTT;
- salvare lo storico su database;
- rendere i dati consultabili via dashboard.

## Materiale consegna
- `docs/RELAZIONE.md` - relazione completa pronta da consegnare.
- `docs/PRESENTAZIONE_10_MIN.md` - scaletta parlata per esposizione (max 10 min).
- `docs/SCHEMI.md` - schema hardware e flusso logico dei dati per le slide.

## Stack del progetto
- **Hardware:** ESP32, BMP-AHT20, OLED
- **Comunicazione:** MQTT
- **Backend:** subscriber MQTT + database
- **Frontend:** dashboard web per visualizzazione real-time e storico

## Struttura repository
- `README.md` - introduzione al progetto
- `docs/` - documentazione del progetto
- `docs/RELAZIONE.md` - documentazione tecnica/funzionale
- `docs/PRESENTAZIONE_10_MIN.md` - traccia presentazione
- `docs/SCHEMI.md` - schemi da inserire nelle slide
- `Images/` - immagini del progetto

## Note
Il progetto e pensato per essere mostrato in demo dal vivo: acquisizione sensori, pubblicazione MQTT, salvataggio su DB e visualizzazione su dashboard.
