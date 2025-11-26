# 🔐 Istruzioni per Aggiungere Variabili su Railway

## 📋 Passo 1: Apri Railway Dashboard

1. Vai su [Railway Dashboard](https://railway.app)
2. Seleziona il progetto: **prop-leader-telegram-api**
3. Clicca sulla tab **"Variables"**

## 📋 Passo 2: Apri Raw Editor

1. Clicca sul pulsante **"Raw Editor"** (icona `{}`)
2. Si aprirà un editor JSON

## 📋 Passo 3: Copia e Incolla il JSON

Apri il file **`railway_variables.json`** nella cartella del progetto e copia TUTTO il contenuto.

Incolla nel Raw Editor di Railway e clicca **"Update Variables"**.

## ✅ Verifica

Dopo aver aggiunto le variabili:
1. Railway farà automaticamente un nuovo deploy
2. Verifica nei log che non ci siano errori
3. Testa l'endpoint per confermare che funziona

## 🔒 Sicurezza

Le variabili d'ambiente su Railway sono:
- ✅ Private e sicure
- ✅ Non visibili nel codice
- ✅ Non committate su GitHub
- ✅ Accessibili solo al servizio Railway

---

**💡 Il file `railway_variables.json` contiene le due parti del file di sessione in base64, divise per rispettare il limite di 32KB di Railway.**

