#!/usr/bin/env python3
"""
Script di test per verificare l'invio di messaggi Telegram.
Invia un messaggio a se stesso ("me") per testare il sistema.
"""
import requests
import json
import sys

# URL del server locale
BASE_URL = "http://localhost:8080"
ENDPOINT = f"{BASE_URL}/prop_leader/send_message"

def get_my_user_id():
    """Ottiene il proprio user_id Telegram"""
    from pyrogram import Client
    
    API_ID = 31738726
    API_HASH = "3c64e7c0d6c4c47524ae1b49102715ea"
    SESSION_NAME = "prop_leader_user_session"
    
    try:
        with Client(SESSION_NAME, API_ID, API_HASH) as app:
            me = app.get_me()
            return me.id
    except Exception as e:
        print(f"❌ Errore nel recupero user_id: {e}")
        return None

def test_send_message(user_id=None, custom_message=None):
    """Testa l'invio di un messaggio"""
    
    # Se non specificato, ottieni il tuo user_id
    if user_id is None:
        print("🔍 Recupero del tuo user_id Telegram...")
        user_id = get_my_user_id()
        if user_id is None:
            print("❌ Impossibile recuperare user_id. Specifica manualmente.")
            return False
        print(f"✅ User ID trovato: {user_id}")
    
    # Prepara i dati
    message = custom_message or "🧪 Test di invio messaggio dal sistema Prop Leader! Se ricevi questo messaggio, il sistema funziona correttamente! ✅"
    
    data = {
        "user_id": str(user_id),
        "first_name": "Test",
        "message": message
    }
    
    print(f"\n📤 Invio messaggio a user_id: {user_id}")
    print(f"💬 Messaggio: {message[:50]}...")
    print(f"🌐 Endpoint: {ENDPOINT}\n")
    
    try:
        response = requests.post(
            ENDPOINT,
            json=data,
            headers={"Content-Type": "application/json"},
            timeout=35
        )
        
        result = response.json()
        
        print("=" * 60)
        print("📥 RISPOSTA DEL SERVER:")
        print("=" * 60)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        print("=" * 60)
        
        if result.get("status") == "success":
            print("\n✅ SUCCESSO! Messaggio inviato correttamente!")
            print(f"📱 Controlla Telegram per verificare la ricezione del messaggio.")
            return True
        else:
            print(f"\n❌ ERRORE: {result.get('error', 'Errore sconosciuto')}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ ERRORE: Impossibile connettersi al server Flask.")
        print("   Assicurati che il server sia avviato (python3 main.py)")
        return False
    except Exception as e:
        print(f"❌ ERRORE: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("🧪 TEST INVIO MESSAGGIO TELEGRAM")
    print("=" * 60)
    print()
    
    # Permetti di specificare user_id e messaggio da riga di comando
    user_id = None
    message = None
    
    if len(sys.argv) > 1:
        user_id = sys.argv[1]
        print(f"📋 User ID specificato: {user_id}")
    
    if len(sys.argv) > 2:
        message = " ".join(sys.argv[2:])
        print(f"📋 Messaggio personalizzato: {message}")
    
    success = test_send_message(user_id, message)
    
    sys.exit(0 if success else 1)

