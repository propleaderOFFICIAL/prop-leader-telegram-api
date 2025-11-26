#!/usr/bin/env python3
"""
Test diretto per inviare un messaggio a un user_id specifico.
Uso: python3 test_send_to_user.py [user_id] [messaggio opzionale]
"""
import asyncio
import sys
from pyrogram import Client

API_ID = 31738726
API_HASH = "3c64e7c0d6c4c47524ae1b49102715ea"
SESSION_NAME = "prop_leader_user_session"

async def send_to_user(user_id, message):
    """Invia un messaggio a un user_id specifico"""
    app_client = Client(SESSION_NAME, API_ID, API_HASH)
    
    try:
        print("🔄 Connessione a Telegram...")
        await app_client.start()
        
        print(f"📤 Invio messaggio a user_id: {user_id}")
        print(f"💬 Messaggio: {message}")
        print()
        
        # Invia il messaggio
        sent = await app_client.send_message(
            chat_id=int(user_id),
            text=message
        )
        
        print("=" * 60)
        print("✅ MESSAGGIO INVIATO CON SUCCESSO!")
        print("=" * 60)
        print(f"📱 ID Messaggio: {sent.id}")
        print(f"📅 Data: {sent.date}")
        print(f"👤 Destinatario: {user_id}")
        print("\n💡 Controlla Telegram per verificare la ricezione!")
        
        await app_client.stop()
        return True
        
    except Exception as e:
        print("=" * 60)
        print("❌ ERRORE DURANTE L'INVIO")
        print("=" * 60)
        print(f"Errore: {e}")
        print()
        print("💡 Possibili cause:")
        print("  1. File di sessione non valido - esegui: python3 authenticate.py")
        print("  2. User ID non valido o utente ha bloccato il tuo account")
        print("  3. Problemi di connessione")
        return False

if __name__ == "__main__":
    # User ID di default (quello fornito dall'utente)
    default_user_id = 167571343
    default_message = "🧪 Test di invio messaggio dal sistema Prop Leader!\n\nSe ricevi questo messaggio, il sistema funziona correttamente! ✅"
    
    # Leggi parametri da riga di comando
    user_id = sys.argv[1] if len(sys.argv) > 1 else str(default_user_id)
    message = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else default_message
    
    print("=" * 60)
    print("🧪 TEST INVIO MESSAGGIO TELEGRAM")
    print("=" * 60)
    print()
    
    result = asyncio.run(send_to_user(user_id, message))
    
    if result:
        print("\n✅ Test completato con successo!")
        sys.exit(0)
    else:
        print("\n❌ Test fallito.")
        sys.exit(1)

