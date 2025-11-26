#!/usr/bin/env python3
"""
Script separato per inviare messaggi Telegram tramite Pyrogram.
Viene chiamato come subprocess per isolare completamente Pyrogram da Flask.
"""
import sys
import json
import asyncio
import os
import base64
import binascii
from pyrogram import Client

# Credenziali
API_ID = 31738726
API_HASH = "3c64e7c0d6c4c47524ae1b49102715ea"
SESSION_NAME = "prop_leader_user_session"

# Determina il path assoluto del file di sessione (nella directory dello script)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SESSION_FILE_PATH = os.path.join(SCRIPT_DIR, f"{SESSION_NAME}.session")

def create_session_file():
    """Crea il file di sessione dalle variabili d'ambiente se non esiste"""
    # Se il file esiste già, non fare nulla
    if os.path.exists(SESSION_FILE_PATH):
        return True
    
    try:
        session_data = None
        
        # Metodo 1: Variabile singola SESSION_BASE64 (se presente)
        if os.environ.get('SESSION_BASE64'):
            session_b64 = os.environ.get('SESSION_BASE64', '').strip()
            if session_b64:
                session_data = base64.b64decode(session_b64)
        
        # Metodo 2: Variabili divise SESSION_BASE64_PART1 e PART2 (per limiti Railway)
        elif os.environ.get('SESSION_BASE64_PART1') and os.environ.get('SESSION_BASE64_PART2'):
            part1 = os.environ.get('SESSION_BASE64_PART1', '').strip()
            part2 = os.environ.get('SESSION_BASE64_PART2', '').strip()
            if part1 and part2:
                combined = part1 + part2
                session_data = base64.b64decode(combined)
        
        if session_data:
            # Crea il file nella directory dello script
            with open(SESSION_FILE_PATH, 'wb') as f:
                f.write(session_data)
            
            # Verifica che il file sia stato creato correttamente
            if os.path.exists(SESSION_FILE_PATH):
                file_size = os.path.getsize(SESSION_FILE_PATH)
                if file_size > 0:
                    return True
                else:
                    print(json.dumps({"success": False, "error": "File di sessione creato ma vuoto"}), file=sys.stderr)
                    return False
            else:
                print(json.dumps({"success": False, "error": "Impossibile creare il file di sessione"}), file=sys.stderr)
                return False
        else:
            print(json.dumps({"success": False, "error": "Nessuna variabile d'ambiente SESSION_BASE64 trovata"}), file=sys.stderr)
            return False
            
    except binascii.Error as e:
        print(json.dumps({"success": False, "error": f"Errore decodifica base64: {str(e)}"}), file=sys.stderr)
        return False
    except Exception as e:
        print(json.dumps({"success": False, "error": f"Errore creazione file sessione: {str(e)}"}), file=sys.stderr)
        return False

# Crea il file di sessione se necessario
if not create_session_file():
    sys.exit(1)

async def send_message(user_id: int, message: str):
    """
    Invia un messaggio Telegram.
    
    NOTA IMPORTANTE: Telegram ha limitazioni anti-spam:
    - Non puoi inviare messaggi a utenti che non ti hanno mai scritto
    - Eccezioni: se l'utente è in un gruppo/canale comune, potrebbe funzionare
    - Se l'utente ti ha aggiunto come contatto, funziona
    
    Questo script tenta comunque l'invio e gestisce gli errori appropriatamente.
    """
    app_client = Client(SESSION_NAME, API_ID, API_HASH, workdir=SCRIPT_DIR)
    try:
        await app_client.start()
        
        # Prova a risolvere il peer prima (aiuta in alcuni casi)
        try:
            peer = await app_client.resolve_peer(user_id)
        except Exception:
            # Se non riesce a risolvere, continua comunque
            pass
        
        # Tenta l'invio del messaggio
        await app_client.send_message(chat_id=user_id, text=message)
        await app_client.stop()
        return {"success": True}
        
    except Exception as e:
        error_str = str(e).lower()
        
        # Gestione errori specifici
        if "peer_id_invalid" in error_str or "peer id invalid" in error_str or "invalid or not known yet" in error_str:
            return {
                "success": False,
                "error": "PEER_ID_INVALID: Non puoi iniziare una conversazione con questo utente perché non ti ha mai scritto. Telegram richiede che l'utente ti abbia scritto almeno una volta prima di poterlo contattare. Soluzione: l'utente deve scriverti prima, oppure devi aggiungerlo come contatto."
            }
        elif "user privacy" in error_str or "privacy" in error_str:
            return {
                "success": False, 
                "error": "L'utente ha impostazioni di privacy che impediscono i messaggi da sconosciuti. L'utente deve averti scritto almeno una volta o essere in un gruppo comune."
            }
        elif "user not found" in error_str or "not found" in error_str:
            return {
                "success": False,
                "error": "Utente non trovato. Verifica che l'user_id sia corretto."
            }
        elif "blocked" in error_str:
            return {
                "success": False,
                "error": "L'utente ti ha bloccato."
            }
        elif "spam" in error_str or "too many" in error_str:
            return {
                "success": False,
                "error": "Limite anti-spam raggiunto. Telegram impedisce di inviare troppi messaggi a utenti che non ti hanno scritto."
            }
        else:
            return {"success": False, "error": str(e)}

if __name__ == "__main__":
    # Leggi i parametri da stdin (JSON)
    try:
        data = json.loads(sys.stdin.read())
        user_id = int(data["user_id"])
        message = data["message"]
        
        # Esegui l'invio
        result = asyncio.run(send_message(user_id, message))
        
        # Output il risultato come JSON
        print(json.dumps(result))
        
    except Exception as e:
        print(json.dumps({"success": False, "error": str(e)}))
        sys.exit(1)

