#!/usr/bin/env python3
"""
Script per inviare messaggi Telegram tramite Bot API (Pyrogram).
I bot possono inviare messaggi a utenti che hanno interagito con il bot,
superando le limitazioni dell'API User.
"""
import sys
import json
import asyncio
import os
from pyrogram import Client

# Token del bot (ottenuto da @BotFather)
# Può essere passato come variabile d'ambiente o hardcoded
BOT_TOKEN = os.environ.get('BOT_TOKEN', '')

if not BOT_TOKEN:
    print(json.dumps({"success": False, "error": "BOT_TOKEN non configurato. Imposta la variabile d'ambiente BOT_TOKEN."}), file=sys.stderr)
    sys.exit(1)

async def send_message(user_id: int, message: str):
    """
    Invia un messaggio Telegram tramite Bot API.
    
    Vantaggi rispetto all'API User:
    - Può inviare messaggi a utenti che hanno interagito con il bot
    - Non ha limitazioni PEER_ID_INVALID
    - Più affidabile per automazioni
    
    Limitazioni:
    - L'utente deve aver interagito con il bot prima (avviato una conversazione)
    - I messaggi arrivano dal bot, non dal tuo account personale
    """
    app_client = Client("bot", bot_token=BOT_TOKEN)
    try:
        await app_client.start()
        
        # Tenta l'invio del messaggio
        await app_client.send_message(chat_id=user_id, text=message)
        await app_client.stop()
        return {"success": True}
        
    except Exception as e:
        error_str = str(e).lower()
        
        # Gestione errori specifici
        if "user is deactivated" in error_str:
            return {
                "success": False,
                "error": "L'utente ha disattivato il suo account Telegram."
            }
        elif "user not found" in error_str or "not found" in error_str:
            return {
                "success": False,
                "error": "Utente non trovato. Verifica che l'user_id sia corretto."
            }
        elif "blocked" in error_str:
            return {
                "success": False,
                "error": "L'utente ha bloccato il bot."
            }
        elif "bot was blocked" in error_str:
            return {
                "success": False,
                "error": "Il bot è stato bloccato dall'utente."
            }
        elif "chat not found" in error_str or "peer_id_invalid" in error_str:
            return {
                "success": False,
                "error": "L'utente non ha mai interagito con il bot. L'utente deve avviare una conversazione con il bot prima (inviare /start o qualsiasi messaggio)."
            }
        elif "forbidden" in error_str:
            return {
                "success": False,
                "error": "Il bot non può inviare messaggi a questo utente. L'utente deve aver interagito con il bot prima."
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

