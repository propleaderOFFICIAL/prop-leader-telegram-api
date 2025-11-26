#!/bin/bash

# Script per caricare il file di sessione su Railway usando pipe diretto
# Metodo più affidabile

echo "🚂 Upload File di Sessione su Railway"
echo "======================================"
echo ""

# Verifica che Railway CLI sia installato
if ! command -v railway &> /dev/null; then
    echo "❌ Railway CLI non trovato!"
    exit 1
fi

# Verifica che il file esista
if [ ! -f "prop_leader_user_session.session" ]; then
    echo "❌ File prop_leader_user_session.session non trovato!"
    exit 1
fi

echo "✅ File trovato: prop_leader_user_session.session"
FILE_SIZE=$(ls -lh prop_leader_user_session.session | awk '{print $5}')
echo "   Dimensione: $FILE_SIZE"
echo ""

# Verifica autenticazione
if ! railway whoami &> /dev/null; then
    echo "❌ Non autenticato! Esegui: railway login"
    exit 1
fi

echo "✅ Autenticato"
echo ""

# Carica il file usando cat e pipe
echo "📤 Caricamento file su Railway..."
cat prop_leader_user_session.session | railway run bash -c "cat > prop_leader_user_session.session && ls -lh prop_leader_user_session.session && echo '' && echo '✅ File caricato correttamente!' && wc -c prop_leader_user_session.session"

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Processo completato!"
    echo ""
    echo "💡 Verifica che il file sia presente:"
    echo "   railway run ls -la prop_leader_user_session.session"
else
    echo ""
    echo "❌ Errore durante il caricamento"
    exit 1
fi

