# 🔐 Aggiungere SESSION_BASE64 su Railway

## Metodo 1: Dashboard Railway (CONSIGLIATO)

1. Vai sul dashboard Railway del tuo progetto
2. Clicca sulla tab **"Variables"**
3. Clicca su **"Raw Editor"** (icona `{}`)
4. Incolla questo JSON (sostituisci con il contenuto completo di `session_base64.txt`):

```json
{
  "SESSION_BASE64": "U1FMaXRlIGZvcm1hdCAzABAAAQEAQCAgAAAAJQAAAAcAAAAAAAAAAAAAAA4AAAAEAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAA..."
}
```

**IMPORTANTE**: Il valore deve essere il contenuto COMPLETO del file `session_base64.txt` (38KB circa).

5. Clicca su **"Update Variables"**
6. Railway farà automaticamente un nuovo deploy

## Metodo 2: Usa il file session_base64.txt

Il file `session_base64.txt` contiene già il contenuto completo in base64.

1. Apri `session_base64.txt` nella cartella del progetto
2. Copia TUTTO il contenuto (è una singola riga lunga)
3. Nel dashboard Railway → Variables → Raw Editor
4. Incolla come:
   ```json
   {
     "SESSION_BASE64": "INCOLLA_QUI_IL_CONTENUTO_COMPLETO"
   }
   ```

## Verifica

Dopo aver aggiunto la variabile, Railway farà un nuovo deploy automaticamente. Verifica nei log che non ci siano errori.

## Test

Una volta deployato, testa l'endpoint:
```bash
curl -X POST https://tuo-progetto.up.railway.app/prop_leader/send_message \
  -H "Content-Type: application/json" \
  -d '{"user_id": "167571343", "first_name": "Test", "message": "Test"}'
```

