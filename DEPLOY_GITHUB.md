# 🚀 Istruzioni per caricare su GitHub

## Opzione 1: Tramite GitHub Web Interface (Consigliato)

### Passo 1: Crea il repository su GitHub
1. Vai su [GitHub.com](https://github.com) e accedi al tuo account
2. Clicca sul pulsante **"+"** in alto a destra → **"New repository"**
3. Compila i campi:
   - **Repository name**: `prop-leader-telegram-api` (o un nome a tua scelta)
   - **Description**: `Integrazione n8n Cloud + Telegram User API per contattare utenti che lasciano il gruppo`
   - **Visibility**: Scegli **Private** (consigliato per progetti con credenziali)
   - **NON** spuntare "Add a README file" (abbiamo già il nostro)
4. Clicca **"Create repository"**

### Passo 2: Collega il repository locale a GitHub
Esegui questi comandi nel terminale (sostituisci `TUO_USERNAME` con il tuo username GitHub):

```bash
cd "/Users/matte1/Documents/Progetti Antigravity/Replit scrivere TG"

# Aggiungi il remote (sostituisci TUO_USERNAME e NOME_REPO)
git remote add origin https://github.com/TUO_USERNAME/NOME_REPO.git

# Rinomina il branch in main (se necessario)
git branch -M main

# Fai il push
git push -u origin main
```

Ti verrà chiesto di inserire le tue credenziali GitHub.

---

## Opzione 2: Tramite GitHub CLI (se installato)

Se hai GitHub CLI installato, puoi creare il repository direttamente dal terminale:

```bash
cd "/Users/matte1/Documents/Progetti Antigravity/Replit scrivere TG"

# Crea il repository su GitHub (sostituisci NOME_REPO)
gh repo create NOME_REPO --private --source=. --remote=origin --push
```

---

## Opzione 3: Usa SSH (se hai configurato le chiavi SSH)

Se preferisci usare SSH invece di HTTPS:

```bash
cd "/Users/matte1/Documents/Progetti Antigravity/Replit scrivere TG"

# Aggiungi il remote SSH (sostituisci TUO_USERNAME e NOME_REPO)
git remote add origin git@github.com:TUO_USERNAME/NOME_REPO.git

# Fai il push
git push -u origin main
```

---

## ✅ Verifica

Dopo il push, verifica che tutto sia stato caricato correttamente:
- Vai sul repository su GitHub
- Dovresti vedere tutti i file: `main.py`, `telegram_sender.py`, `authenticate.py`, `requirements.txt`, `README.md`, `.gitignore`
- **IMPORTANTE**: Verifica che il file `.session` NON sia presente (dovrebbe essere escluso dal `.gitignore`)

---

## 🔒 Sicurezza

Ricorda che:
- ✅ Le credenziali API (API_ID, API_HASH) sono nel codice - considera di usarle come variabili d'ambiente
- ✅ Il file `.session` è escluso dal repository (grazie al `.gitignore`)
- ⚠️ Se il repository è pubblico, le credenziali API saranno visibili a tutti

**Consiglio**: Se vuoi rendere il repository pubblico in futuro, sposta le credenziali in variabili d'ambiente o in un file di configurazione escluso dal git.

