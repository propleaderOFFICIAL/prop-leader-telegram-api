#!/bin/bash

# Script per aggiornare le variabili Railway dopo aver rigenerato il file di sessione

echo "🔄 Aggiornamento Variabili Railway"
echo "===================================="
echo ""

# Verifica che il file esista
if [ ! -f "prop_leader_user_session.session" ]; then
    echo "❌ File prop_leader_user_session.session non trovato!"
    echo ""
    echo "💡 Prima rigenera il file eseguendo:"
    echo "   python3 authenticate.py"
    exit 1
fi

echo "✅ File di sessione trovato"
FILE_SIZE=$(ls -lh prop_leader_user_session.session | awk '{print $5}')
echo "   Dimensione: $FILE_SIZE"
echo ""

# Converti in base64 (sintassi macOS)
echo "🔄 Conversione in base64..."
base64 -i prop_leader_user_session.session > session_base64_temp.txt

# Verifica dimensione
BASE64_SIZE=$(wc -c < session_base64_temp.txt)
echo "   Dimensione base64: $BASE64_SIZE byte"
echo ""

# Divide in due parti (limite 32KB = 32768 byte)
PART1_SIZE=32000
echo "📦 Divisione in due parti..."
head -c $PART1_SIZE session_base64_temp.txt > session_part1_temp.txt
tail -c +$((PART1_SIZE + 1)) session_base64_temp.txt > session_part2_temp.txt

PART1_LEN=$(wc -c < session_part1_temp.txt)
PART2_LEN=$(wc -c < session_part2_temp.txt)

echo "   Parte 1: $PART1_LEN byte"
echo "   Parte 2: $PART2_LEN byte"
echo ""

# Crea il JSON
echo "📝 Creazione railway_variables.json..."
python3 << 'PYEOF'
import json

# Leggi le due parti
with open('session_part1_temp.txt', 'r') as f:
    part1 = f.read().strip()

with open('session_part2_temp.txt', 'r') as f:
    part2 = f.read().strip()

# Crea il JSON per Railway
railway_vars = {
    "SESSION_BASE64_PART1": part1,
    "SESSION_BASE64_PART2": part2
}

# Salva il JSON
with open('railway_variables.json', 'w') as f:
    json.dump(railway_vars, f, indent=2)

print("✅ railway_variables.json creato!")
print(f"   Parte 1: {len(part1)} caratteri")
print(f"   Parte 2: {len(part2)} caratteri")
PYEOF

# Pulisci file temporanei
rm -f session_base64_temp.txt session_part1_temp.txt session_part2_temp.txt

echo ""
echo "✅ COMPLETATO!"
echo ""
echo "📋 PROSSIMI PASSI:"
echo "   1. Apri railway_variables.json"
echo "   2. Copia TUTTO il contenuto"
echo "   3. Railway Dashboard → Variables → Raw Editor"
echo "   4. Incolla il JSON e clicca 'Update Variables'"
echo ""

