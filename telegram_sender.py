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
from pyrogram import Client

# Credenziali
API_ID = 31738726
API_HASH = "3c64e7c0d6c4c47524ae1b49102715ea"
SESSION_NAME = "prop_leader_user_session"

# Crea il file di sessione dalla variabile d'ambiente se non esiste
if not os.path.exists(f"{SESSION_NAME}.session") and os.environ.get('SESSION_BASE64'):
    try:
        session_data = base64.b64decode(os.environ.get('SESSION_BASE64'))
        with open(f"{SESSION_NAME}.session", 'wb') as f:
            f.write(session_data)
    except Exception as e:
        print(json.dumps({"success": False, "error": f"Errore creazione file sessione: {str(e)}"}), file=sys.stderr)

async def send_message(user_id: int, message: str):
    """Invia un messaggio Telegram"""
    app_client = Client(SESSION_NAME, API_ID, API_HASH)
    try:
        await app_client.start()
        await app_client.send_message(chat_id=user_id, text=message)
        await app_client.stop()
        return {"success": True}
    except Exception as e:
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

