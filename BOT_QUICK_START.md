# 🚀 Quick Start: Bot Telegram

## ⚡ Setup Rapido (5 minuti)

### 1. Crea il Bot (2 minuti)

1. Apri Telegram → Cerca **@BotFather**
2. Invia: `/newbot`
3. Nome: `Prop Leader Bot`
4. Username: `propleader_bot` (o qualsiasi nome disponibile)
5. **Copia il TOKEN** che ti dà (tipo: `1234567890:ABCdef...`)

### 2. Configura il Token (1 minuto)

**Su Railway:**
- Variables → Aggiungi `BOT_TOKEN` = `il_tuo_token`

**Su Replit:**
- Secrets → Aggiungi `BOT_TOKEN` = `il_tuo_token`

### 3. Aggiungi il Bot al Gruppo (1 minuto)

1. Apri il gruppo
2. Aggiungi membri → Cerca `@propleader_bot`
3. Aggiungi il bot

### 4. Usa l'Endpoint Bot (1 minuto)

In n8n, cambia l'URL da:
```
/prop_leader/send_message
```

a:
```
/prop_leader/send_message_bot
```

## ✅ Fatto!

Ora puoi inviare messaggi anche a utenti che non ti hanno scritto (se hanno interagito con il bot).

## ⚠️ Importante

L'utente deve aver interagito con il bot prima:
- Ha inviato `/start` al bot
- Ha scritto un messaggio al bot
- Ha cliccato su un pulsante del bot

Se l'utente non ha mai interagito, riceverai un errore "chat not found".

## 🔄 Strategia Ibrida

Usa entrambi gli endpoint per massimizzare le possibilità:

1. Prova prima con **Bot API** (`/send_message_bot`)
2. Se fallisce, prova con **User API** (`/send_message`)

Vedi [BOT_SETUP.md](./BOT_SETUP.md) per la guida completa.

