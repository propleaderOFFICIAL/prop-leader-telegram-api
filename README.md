# 🚀 Integrazione n8n Cloud + Telegram User API (Pyrogram)

## 🎯 Obiettivo: Contatto Diretto (User API)

Automatizzare il contatto dal tuo account Telegram personale (non dal Bot) verso gli utenti che abbandonano il Gruppo di Discussione collegato al Canale Prop Leader, superando i limiti di installazione di n8n Cloud.

---

## 📋 Prerequisiti

1. **API ID e API Hash di Telegram**: Ottenuti da [my.telegram.org](https://my.telegram.org)
2. **Python 3.7+** installato sul tuo PC locale
3. **Account hosting** (Replit, Railway, o Vercel - vedi [DEPLOY_OPTIONS.md](./DEPLOY_OPTIONS.md))

---

## 🔑 Passo 1: Autenticazione (CRUCIALE)

**IMPORTANTE:** Questo passaggio genera il file `prop_leader_user_session.session`, che è la chiave per far agire il codice come te. **NON** può essere gestito da remoto.

### Setup Locale:

1. **Installa Pyrogram sul tuo PC locale:**
   ```bash
   pip install pyrogram
   ```

2. **Esegui lo script di autenticazione:**
   ```bash
   python authenticate.py
   ```

3. **Segui le istruzioni:**
   - Inserisci il tuo **numero di telefono** (con prefisso internazionale, es. +39...)
   - Inserisci il **codice di accesso** inviato da Telegram
   - Se hai 2FA attivo, inserisci la **password**

4. **Risultato:** Verrà creato il file **`prop_leader_user_session.session`** nella stessa cartella.

---

## 🛠️ Passo 2: Hosting

Puoi usare uno di questi servizi:
- 🚂 **Railway** (Consigliato) - Vedi [RAILWAY_SETUP.md](./RAILWAY_SETUP.md)
- 🖥️ **Replit** - Vedi [REPLIT_SETUP.md](./REPLIT_SETUP.md)
- ▲ **Vercel** - Vedi [VERCEL_SETUP.md](./VERCEL_SETUP.md)

Confronto completo: [DEPLOY_OPTIONS.md](./DEPLOY_OPTIONS.md)

### Opzione A: Hosting su Replit

1. **Importa il progetto su Replit:**
   - Crea un nuovo Repl
   - Importa questo repository GitHub (o carica i file manualmente)

2. **Carica la Sessione:**
   - Carica **manualmente** il file `prop_leader_user_session.session` (generato nel Passo 1) nel progetto Replit
   - **IMPORTANTE:** Assicurati che il file sia nella root del progetto

3. **Installa le dipendenze:**
   - Replit dovrebbe installare automaticamente le dipendenze da `requirements.txt`
   - Oppure esegui manualmente: `pip install -r requirements.txt`

4. **Avvia il server:**
   - Clicca "Run" su Replit
   - Il server sarà online e ti verrà fornito un URL pubblico (es. `https://nome-progetto.replit.app`)

5. **Ottieni l'URL Finale:**
   ```
   URL Pubblico di Replit + /prop_leader/send_message
   ```
   Esempio: `https://prop-leader-bot.replit.app/prop_leader/send_message`

---

### Opzione B: Hosting su Railway (Consigliato)

Railway è più semplice e non richiede modifiche al codice. Vedi la guida completa in [RAILWAY_SETUP.md](./RAILWAY_SETUP.md).

### Opzione C: Hosting su Vercel

Vercel richiede alcune modifiche per funzionare con serverless. Vedi [VERCEL_SETUP.md](./VERCEL_SETUP.md).

---

## ⚙️ Passo 3: Configurazione n8n Cloud

### Workflow n8n:

1. **Nodo 1: Telegram Trigger**
   - Configurazione: Ascolta `New Chat Member` sul tuo Supergruppo collegato

2. **Nodo 2: IF**
   - **Condizione:**
     - `Value 1`: `{{ $json.message.left_chat_member }}`
     - `Operation`: `Is Not Empty`
   - Collega il ramo **"True"** al nodo successivo

3. **Nodo 3: HTTP Request**
   - **Method:** `POST`
   - **URL:** *Incolla l'URL Finale ottenuto da Replit*
     ```
     https://nome-progetto.replit.app/prop_leader/send_message
     ```
   - **Body Content Type:** `JSON`
   - **Body Parameters (JSON/RAW Expression):**
     ```json
     {
       "user_id": "{{ $json.message.left_chat_member.id }}",
       "first_name": "{{ $json.message.left_chat_member.first_name }}",
       "message": "Non perdere il profitto! Ho notato la tua uscita dalla community. Contattami ora per accedere di nuovo ai conti REALI."
     }
     ```

---

## 🔒 Sicurezza

- **NON** committare il file `prop_leader_user_session.session` su GitHub
- Aggiungi `*.session` al tuo `.gitignore`
- Mantieni le tue credenziali API private

---

## 🐛 Troubleshooting

### Errore: "Session file not found"
- Assicurati di aver caricato il file `prop_leader_user_session.session` su Replit
- Verifica che il file sia nella root del progetto

### Errore: "User blocked"
- L'utente ha bloccato il tuo account Telegram
- Il sistema gestirà l'errore e continuerà con gli altri utenti

### Errore: "Phone number invalid"
- Usa il formato internazionale con il prefisso `+` (es. `+39123456789`)

### Errore: "There is no current event loop"
- Questo errore può apparire durante i test locali senza il file di sessione
- **Non è un problema**: il sistema funzionerà correttamente su Replit con il file di sessione caricato
- Il codice usa subprocess per isolare completamente Pyrogram da Flask, risolvendo i problemi di event loop

---

## 📝 Note

- Il server Flask è configurato per ascoltare su tutte le interfacce (`0.0.0.0`)
- La porta viene letta dalla variabile d'ambiente `PORT` (default: 8080)
- Replit gestisce automaticamente la porta, quindi non è necessario modificarla

---

**ZERO FILTRI! 🚀**

