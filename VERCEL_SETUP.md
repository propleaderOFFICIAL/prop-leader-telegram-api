# ▲ Guida Setup Vercel (Serverless)

⚠️ **NOTA**: Vercel è ottimizzato per funzioni serverless. Richiede una piccola modifica al codice per funzionare correttamente.

## Considerazioni

Vercel funziona meglio con funzioni serverless, ma il nostro codice usa subprocess che può avere limitazioni. Tuttavia, possiamo adattarlo.

## Passo 1: Crea Account e Progetto

1. Vai su [Vercel](https://vercel.com) e accedi (puoi usare GitHub)
2. Clicca su **"Add New..."** → **"Project"**
3. Importa il repository: `propleaderOFFICIAL/prop-leader-telegram-api`
4. Vercel rileverà automaticamente Python

## Passo 2: Crea File di Configurazione Vercel

Crea un file `vercel.json` nella root del progetto:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "main.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "main.py"
    }
  ]
}
```

## Passo 3: Adatta il Codice per Vercel

Vercel richiede che l'app Flask sia esposta come `app` (già fatto) e che gestisca le richieste in modo serverless.

Il codice attuale dovrebbe funzionare, ma creiamo una versione ottimizzata:

### Crea `vercel_handler.py`:

```python
from main import app

# Vercel richiede questo export
handler = app
```

## Passo 4: Carica il File di Sessione

⚠️ **IMPORTANTE**: Vercel ha limitazioni sui file system. Dobbiamo usare variabili d'ambiente o storage esterno.

### Opzione A: Base64 Encoding (Consigliato)

1. Converti il file `.session` in base64:
   ```bash
   base64 prop_leader_user_session.session > session_base64.txt
   ```

2. Aggiungi come variabile d'ambiente in Vercel:
   - Vai su **Settings** → **Environment Variables**
   - **Key**: `SESSION_BASE64`
   - **Value**: (incolla il contenuto di session_base64.txt)

3. Modifica `telegram_sender.py` per decodificare:
   ```python
   import base64
   import os
   
   # All'inizio dello script
   if os.environ.get('SESSION_BASE64'):
       session_data = base64.b64decode(os.environ.get('SESSION_BASE64'))
       with open('prop_leader_user_session.session', 'wb') as f:
           f.write(session_data)
   ```

### Opzione B: Usa Storage Esterno (S3, etc.)

Per produzione, considera di usare AWS S3 o simile per il file di sessione.

## Passo 5: Configura le Variabili d'Ambiente

Nel dashboard Vercel, vai su **Settings** → **Environment Variables**:

- `API_ID`: `31738726`
- `API_HASH`: `3c64e7c0d6c4c47524ae1b49102715ea`
- `SESSION_BASE64`: (contenuto base64 del file .session)

## Passo 6: Deploy

1. Vercel farà il deploy automaticamente quando rileva cambiamenti su GitHub
2. Oppure clicca su **"Deploy"** manualmente
3. Attendi che il deploy completi

## Passo 7: Ottieni l'URL Pubblico

1. Vercel ti darà automaticamente un URL tipo:
   ```
   https://prop-leader-telegram-api.vercel.app
   ```

2. L'endpoint completo per n8n sarà:
   ```
   https://prop-leader-telegram-api.vercel.app/prop_leader/send_message
   ```

## ⚠️ Limitazioni di Vercel

- **Cold Start**: La prima richiesta può essere lenta (2-5 secondi)
- **Timeout**: Funzioni serverless hanno timeout (10s su free, 60s su pro)
- **File System**: Limitato, meglio usare variabili d'ambiente
- **Subprocess**: Può avere limitazioni

## 🔧 Troubleshooting

### Timeout Error
- Vercel free tier ha timeout di 10 secondi
- Considera di usare Railway o upgrade a Vercel Pro (60s timeout)

### File Session Not Found
- Verifica che `SESSION_BASE64` sia configurato correttamente
- Controlla i log in Vercel Dashboard → **Functions** → **Logs**

### Cold Start Lento
- È normale per funzioni serverless
- Considera di usare Railway per performance migliori

## 💰 Pricing

Vercel offre:
- **Free Tier**: 100GB bandwidth, 100 invocations/giorno
- **Pro Plan**: $20/mese per più risorse e timeout più lunghi

## ✅ Quando Usare Vercel

- ✅ Hai bisogno di scalabilità automatica
- ✅ Il traffico è sporadico
- ✅ Vuoi integrazione facile con Next.js/React

## ❌ Quando NON Usare Vercel

- ❌ Hai bisogno di processi long-running
- ❌ Il timeout di 10s non è sufficiente
- ❌ Hai bisogno di file system completo

---

**💡 Raccomandazione**: Per questo progetto, **Railway è più adatto** perché:
- Supporta processi long-running
- Nessuna modifica al codice necessaria
- File system completo
- Più semplice da configurare

---

**🎉 Se preferisci Vercel, segui i passi sopra!**

