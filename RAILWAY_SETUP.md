# 🚂 Guida Setup Railway

Railway è perfetto per questo progetto perché supporta processi long-running e Flask senza modifiche.

## Passo 1: Crea Account e Progetto

1. Vai su [Railway](https://railway.app) e accedi (puoi usare GitHub)
2. Clicca su **"New Project"**
3. Scegli **"Deploy from GitHub repo"**
4. Seleziona il repository: `propleaderOFFICIAL/prop-leader-telegram-api`
5. Railway rileverà automaticamente che è un progetto Python

## Passo 2: Configura le Variabili d'Ambiente

1. Nel dashboard del progetto, vai su **"Variables"**
2. Aggiungi la variabile:
   - **Key**: `PORT`
   - **Value**: `8080` (o lascia vuoto, Railway la imposterà automaticamente)

## Passo 3: Carica il File di Sessione

⚠️ **IMPORTANTE**: Il file `.session` deve essere caricato come file nel progetto.

### Opzione A: Tramite Railway CLI (Consigliato)

1. Installa Railway CLI:
   ```bash
   npm i -g @railway/cli
   ```

2. Accedi:
   ```bash
   railway login
   ```

3. Collega il progetto:
   ```bash
   railway link
   ```

4. Carica il file:
   ```bash
   railway up prop_leader_user_session.session
   ```

### Opzione B: Tramite GitHub (Temporaneo)

1. **ATTENZIONE**: Questo espone il file pubblicamente!
2. Aggiungi temporaneamente il file al repository (solo per il deploy)
3. Dopo il deploy, rimuovilo immediatamente

### Opzione C: Tramite Railway Dashboard

1. Vai su **"Settings"** → **"Source"**
2. Usa il file system per aggiungere il file direttamente

## Passo 4: Configura il Build

Railway dovrebbe rilevare automaticamente Python, ma puoi verificare:

1. Vai su **"Settings"** → **"Build"**
2. Assicurati che il **Build Command** sia:
   ```bash
   pip install -r requirements.txt
   ```
3. Il **Start Command** dovrebbe essere:
   ```bash
   python3 main.py
   ```

## Passo 5: Deploy

1. Railway farà il deploy automaticamente quando rileva cambiamenti su GitHub
2. Oppure clicca su **"Deploy"** manualmente
3. Attendi che il deploy completi

## Passo 6: Ottieni l'URL Pubblico

1. Vai su **"Settings"** → **"Networking"**
2. Clicca su **"Generate Domain"**
3. Railway ti darà un URL tipo:
   ```
   https://prop-leader-telegram-api-production.up.railway.app
   ```

4. L'endpoint completo per n8n sarà:
   ```
   https://prop-leader-telegram-api-production.up.railway.app/prop_leader/send_message
   ```

## Passo 7: Configura n8n

Nel workflow n8n, configura il nodo **HTTP Request**:

- **Method**: `POST`
- **URL**: `https://tuo-progetto.up.railway.app/prop_leader/send_message`
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

### Il deploy fallisce
- Verifica che tutte le dipendenze siano in `requirements.txt`
- Controlla i log in Railway Dashboard → **"Deployments"** → **"View Logs"**

### Errore "Session file not found"
- Assicurati di aver caricato il file `.session` nella root del progetto
- Verifica che il file sia presente: Railway Dashboard → **"Files"**

### Il servizio si ferma
- Railway mantiene i servizi attivi, ma controlla i log per eventuali errori
- Verifica che il servizio sia in stato "Active" nel dashboard

### Test dell'endpoint
```bash
curl -X POST https://tuo-progetto.up.railway.app/prop_leader/send_message \
  -H "Content-Type: application/json" \
  -d '{"user_id": "167571343", "first_name": "Test", "message": "Test"}'
```

## 💰 Pricing

Railway offre:
- **Free Tier**: $5 di crediti gratuiti al mese
- **Hobby Plan**: $5/mese per servizi sempre attivi
- **Pro Plan**: $20/mese per più risorse

## ✅ Vantaggi di Railway

- ✅ Processi long-running supportati
- ✅ Deploy automatico da GitHub
- ✅ SSL automatico
- ✅ Logs in tempo reale
- ✅ Facile gestione file
- ✅ Nessuna modifica al codice necessaria

---

**🎉 Railway è perfetto per questo progetto!**

