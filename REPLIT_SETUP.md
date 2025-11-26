# 🚀 Guida Setup Replit

## Passo 1: Importa il Repository

1. Vai su [Replit](https://replit.com) e accedi al tuo account
2. Clicca su **"Create Repl"** (o **"+"** in alto a destra)
3. Scegli **"Import from GitHub"**
4. Inserisci il repository: `propleaderOFFICIAL/prop-leader-telegram-api`
5. Scegli **"Python"** come template
6. Clicca **"Import"**

## Passo 2: Carica il File di Sessione

⚠️ **IMPORTANTE**: Il file di sessione NON è nel repository per sicurezza.

1. Nella sidebar di Replit, clicca su **"Files"**
2. Clicca sui **"..."** (tre punti) accanto alla cartella principale
3. Scegli **"Upload file"**
4. Carica il file: `prop_leader_user_session.session`
   - Questo file si trova nella cartella locale del progetto
   - Se non ce l'hai, esegui `python3 authenticate.py` localmente

## Passo 3: Installa le Dipendenze

1. Apri il terminale in Replit (icona terminale in basso)
2. Esegui:
   ```bash
   pip install -r requirements.txt
   ```

## Passo 4: Avvia il Server

1. Nel terminale, esegui:
   ```bash
   python3 main.py
   ```

2. Replit dovrebbe avviare automaticamente il server e mostrarti l'URL pubblico

## Passo 5: Ottieni l'URL Pubblico

1. Una volta avviato, Replit ti mostrerà un URL tipo:
   ```
   https://prop-leader-telegram-api.your-username.repl.co
   ```

2. L'endpoint completo per n8n sarà:
   ```
   https://prop-leader-telegram-api.your-username.repl.co/prop_leader/send_message
   ```

## Passo 6: Configura n8n

Nel workflow n8n, configura il nodo **HTTP Request**:

- **Method**: `POST`
- **URL**: `https://tuo-repl.repl.co/prop_leader/send_message`
- **Body Content Type**: `JSON`
- **Body Parameters**:
  ```json
  {
    "user_id": "{{ $json.message.left_chat_member.id }}",
    "first_name": "{{ $json.message.left_chat_member.first_name }}",
    "message": "Non perdere il profitto! Ho notato la tua uscita dalla community. Contattami ora per accedere di nuovo ai conti REALI."
  }
  ```

## 🔧 Troubleshooting

### Il server non si avvia
- Verifica che il file `prop_leader_user_session.session` sia nella root del progetto
- Controlla che tutte le dipendenze siano installate: `pip list | grep -E "pyrogram|flask"`

### Errore "Session file not found"
- Assicurati di aver caricato il file `.session` su Replit
- Verifica che il file sia nella stessa directory di `main.py`

### Il server si ferma dopo qualche minuto
- Replit può mettere in pausa i Repl inattivi
- Considera di usare un servizio di keep-alive o upgrade a Replit Hacker plan

### Test dell'endpoint
Puoi testare l'endpoint direttamente da Replit:
```bash
curl -X POST http://localhost:8080/prop_leader/send_message \
  -H "Content-Type: application/json" \
  -d '{"user_id": "167571343", "first_name": "Test", "message": "Test"}'
```

## ✅ Verifica Funzionamento

1. Avvia il server
2. Controlla che l'endpoint `/` risponda:
   ```bash
   curl https://tuo-repl.repl.co/
   ```
   Dovresti vedere: `{"status": "online", ...}`

3. Testa l'invio di un messaggio tramite n8n o direttamente con curl

---

**🎉 Una volta configurato, il sistema sarà completamente operativo!**

