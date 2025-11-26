# 📤 Come Caricare File su Railway

Railway non ha un'interfaccia web per caricare file direttamente. Ecco i metodi disponibili:

## 🎯 Metodo 1: Railway CLI (CONSIGLIATO)

Questo è il metodo più sicuro e diretto.

### Passo 1: Installa Railway CLI

**Su macOS (con Homebrew):**
```bash
brew install railway
```

**Su macOS/Linux (con npm):**
```bash
npm i -g @railway/cli
```

**Su Windows:**
```bash
npm i -g @railway/cli
```

### Passo 2: Accedi a Railway

```bash
railway login
```

Ti aprirà il browser per autenticarti con GitHub o email.

### Passo 3: Collega il Progetto

```bash
# Vai nella cartella del progetto locale
cd "/Users/matte1/Documents/Progetti Antigravity/Replit scrivere TG"

# Collega al progetto Railway
railway link
```

Ti chiederà di selezionare il progetto Railway. Scegli quello che hai creato.

### Passo 4: Carica il File di Sessione

```bash
# Assicurati che il file esista nella cartella corrente
ls -la prop_leader_user_session.session

# Carica il file su Railway
railway up prop_leader_user_session.session
```

Il file verrà caricato nella root del progetto su Railway.

### Verifica il Caricamento

```bash
# Lista i file nel progetto Railway
railway run ls -la
```

Dovresti vedere `prop_leader_user_session.session` nella lista.

---

## 🔄 Metodo 2: Tramite GitHub (Temporaneo)

⚠️ **ATTENZIONE**: Questo metodo espone temporaneamente il file pubblicamente su GitHub!

### Passo 1: Aggiungi Temporaneamente al Repository

```bash
cd "/Users/matte1/Documents/Progetti Antigravity/Replit scrivere TG"

# Rimuovi temporaneamente dal .gitignore
# (modifica .gitignore e commenta la riga *.session)

# Aggiungi il file
git add prop_leader_user_session.session
git commit -m "Temporaneo: aggiunto file sessione per deploy Railway"
git push origin main
```

### Passo 2: Railway Farà il Deploy Automatico

Railway rileverà il cambiamento e farà il deploy automaticamente.

### Passo 3: RIMUOVI IMMEDIATAMENTE il File da GitHub

```bash
# Rimuovi il file dal repository
git rm --cached prop_leader_user_session.session
git commit -m "Rimosso file sessione da GitHub (sicurezza)"
git push origin main

# Ripristina .gitignore
# (decommenta la riga *.session)
```

**IMPORTANTE**: Anche se rimuovi il file, rimane nella cronologia Git. Per sicurezza completa, considera di:
1. Usare un repository privato
2. O meglio ancora, usare il Metodo 1 (CLI)

---

## 🔐 Metodo 3: Variabili d'Ambiente (Per File Piccoli)

Se il file `.session` è piccolo (< 1MB), puoi convertirlo in base64 e salvarlo come variabile d'ambiente.

### Passo 1: Converti il File in Base64

```bash
cd "/Users/matte1/Documents/Progetti Antigravity/Replit scrivere TG"

# Converti in base64
base64 prop_leader_user_session.session > session_base64.txt

# Copia il contenuto
cat session_base64.txt
```

### Passo 2: Aggiungi come Variabile d'Ambiente su Railway

1. Vai sul dashboard Railway
2. Seleziona il tuo progetto
3. Vai su **"Variables"**
4. Aggiungi:
   - **Key**: `SESSION_BASE64`
   - **Value**: (incolla il contenuto di session_base64.txt)

### Passo 3: Modifica il Codice (Opzionale)

Se vuoi usare la variabile d'ambiente invece del file, modifica `telegram_sender.py`:

```python
import os
import base64

# All'inizio dello script, prima di usare Client
if os.environ.get('SESSION_BASE64'):
    session_data = base64.b64decode(os.environ.get('SESSION_BASE64'))
    with open('prop_leader_user_session.session', 'wb') as f:
        f.write(session_data)
```

**Nota**: Questo metodo funziona, ma il Metodo 1 (CLI) è più semplice e diretto.

---

## ✅ Verifica che il File Sia Presente

Dopo aver caricato il file, verifica che sia presente:

### Tramite CLI:
```bash
railway run ls -la prop_leader_user_session.session
```

### Tramite Logs:
1. Vai sul dashboard Railway
2. Seleziona il progetto
3. Vai su **"Deployments"** → **"View Logs"**
4. Cerca errori tipo "Session file not found"

### Test dell'Endpoint:
```bash
curl -X POST https://tuo-progetto.up.railway.app/prop_leader/send_message \
  -H "Content-Type: application/json" \
  -d '{"user_id": "167571343", "first_name": "Test", "message": "Test"}'
```

---

## 🔧 Troubleshooting

### "railway: command not found"
- Installa Railway CLI: `npm i -g @railway/cli` o `brew install railway`

### "No project linked"
- Esegui `railway link` nella cartella del progetto

### "Session file not found" dopo il deploy
- Verifica che il file sia stato caricato: `railway run ls -la`
- Assicurati che il file sia nella root del progetto (stessa directory di `main.py`)

### Il file non viene caricato
- Verifica di essere nella directory corretta
- Controlla che il file esista: `ls -la prop_leader_user_session.session`
- Prova a ricollegare: `railway unlink` poi `railway link`

---

## 💡 Raccomandazione Finale

**Usa il Metodo 1 (Railway CLI)** perché:
- ✅ Sicuro (non espone il file pubblicamente)
- ✅ Semplice e diretto
- ✅ Funziona immediatamente
- ✅ Non richiede modifiche al codice

---

**🎉 Una volta caricato il file, Railway farà il deploy automaticamente e il sistema sarà operativo!**

