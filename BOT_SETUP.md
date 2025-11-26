# 🤖 Setup Bot Telegram

Questa guida ti aiuta a creare e configurare un Bot Telegram per superare le limitazioni dell'API User.

## 🎯 Perché Usare un Bot?

- ✅ **Supera PEER_ID_INVALID**: Puoi contattare utenti che non ti hanno scritto
- ✅ **Più affidabile**: Nessuna limitazione di privacy
- ✅ **Automazione migliore**: Ideale per messaggi automatici
- ⚠️ **Limitazione**: L'utente deve aver interagito con il bot prima (inviato /start o un messaggio)

## 📋 Passo 1: Crea il Bot

1. **Apri Telegram** e cerca **@BotFather**
2. **Invia il comando**: `/newbot`
3. **Scegli un nome** per il bot (es. "Prop Leader Assistant")
4. **Scegli un username** per il bot (deve finire con `bot`, es. `propleader_bot`)
5. **BotFather ti darà un TOKEN** tipo: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`

⚠️ **SALVA IL TOKEN!** Ti servirà per configurare il sistema.

## 📋 Passo 2: Configura il Bot (Opzionale)

### Imposta Descrizione
```
/setdescription
```
Scegli il bot → Inserisci una descrizione (es. "Bot ufficiale Prop Leader")

### Imposta Immagine
```
/setuserpic
```
Scegli il bot → Carica un'immagine

### Imposta Comandi
```
/setcommands
```
Scegli il bot → Aggiungi comandi come:
```
start - Inizia a usare il bot
help - Mostra aiuto
```

## 📋 Passo 3: Aggiungi il Bot al Gruppo

1. **Apri il gruppo** dove vuoi usare il bot
2. **Aggiungi membri** → Cerca il tuo bot (es. `@propleader_bot`)
3. **Dai i permessi necessari** al bot (se richiesto)

## 📋 Passo 4: Configura il Token

### Opzione A: Variabile d'Ambiente (Consigliato)

**Su Railway:**
1. Vai su **Variables**
2. Aggiungi: `BOT_TOKEN` = `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`

**Su Replit:**
1. Vai su **Secrets** (🔒)
2. Aggiungi: `BOT_TOKEN` = `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`

**Localmente:**
```bash
export BOT_TOKEN="1234567890:ABCdefGHIjklMNOpqrsTUVwxyz"
```

### Opzione B: File di Configurazione (Non Raccomandato)

Puoi modificare `telegram_bot_sender.py` e inserire il token direttamente, ma **NON è sicuro** per produzione.

## 📋 Passo 5: Testa il Bot

### Test Locale

1. **Imposta la variabile d'ambiente:**
   ```bash
   export BOT_TOKEN="il_tuo_token"
   ```

2. **Testa l'invio:**
   ```bash
   echo '{"user_id": 123456789, "message": "Test"}' | python3 telegram_bot_sender.py
   ```

### Test via API

```bash
curl -X POST http://localhost:8080/prop_leader/send_message_bot \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 123456789,
    "message": "Test messaggio dal bot"
  }'
```

## 📋 Passo 6: Configura n8n

Nel workflow n8n, usa l'endpoint **Bot API** invece di User API:

**HTTP Request Node:**
- **Method**: `POST`
- **URL**: `https://tuo-servizio.railway.app/prop_leader/send_message_bot`
- **Body**:
  ```json
  {
    "user_id": "{{ $json.message.left_chat_member.id }}",
    "message": "Messaggio personalizzato"
  }
  ```

## ⚠️ Limitazioni Importanti

### L'Utente Deve Aver Interagito con il Bot

Il bot può inviare messaggi SOLO a utenti che:
- Hanno inviato `/start` al bot
- Hanno inviato qualsiasi messaggio al bot
- Hanno interagito con il bot in qualche modo

### Soluzione: Messaggio di Benvenuto Automatico

Quando un utente entra nel gruppo:
1. Il bot può inviare un messaggio di benvenuto nel gruppo
2. Questo NON crea una conversazione privata
3. Ma se l'utente clicca sul bot o gli scrive, allora puoi contattarlo

### Strategia Consigliata

1. **Aggiungi il bot al gruppo**
2. **Configura il bot per rispondere a /start** (opzionale, per creare conversazioni)
3. **Quando un utente esce**, prova a contattarlo:
   - Se ha interagito con il bot → Funziona ✅
   - Se non ha interagito → Errore "chat not found" ❌

## 🔄 Fallback: User API + Bot API

Puoi usare entrambi gli endpoint:

1. **Prova prima con Bot API** (`/prop_leader/send_message_bot`)
2. **Se fallisce**, usa User API (`/prop_leader/send_message`)

Questo massimizza le possibilità di contattare l'utente.

## 🐛 Troubleshooting

### Errore: "BOT_TOKEN non configurato"
- Verifica che la variabile d'ambiente `BOT_TOKEN` sia impostata
- Riavvia il servizio dopo aver aggiunto la variabile

### Errore: "chat not found" o "peer_id_invalid"
- L'utente non ha mai interagito con il bot
- L'utente deve inviare `/start` o un messaggio al bot prima

### Errore: "bot was blocked"
- L'utente ha bloccato il bot
- Non puoi contattarlo finché non sblocca il bot

### Il bot non risponde
- Verifica che il token sia corretto
- Verifica che il bot sia attivo (non disabilitato da BotFather)

## 📚 Risorse

- [Documentazione Pyrogram Bot API](https://docs.pyrogram.org/api/methods/send_message)
- [BotFather su Telegram](https://t.me/BotFather)
- [Telegram Bot API](https://core.telegram.org/bots/api)

