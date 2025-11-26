#!/usr/bin/env python3
"""
Test diretto dell'invio messaggio Telegram (bypassa Flask per test rapido).
Invia un messaggio a "me" (te stesso) per testare.
"""
import asyncio
from pyrogram import Client

API_ID = 31738726
API_HASH = "3c64e7c0d6c4c47524ae1b49102715ea"
SESSION_NAME = "prop_leader_user_session"

async def send_test_message():
    """Invia un messaggio di test a se stesso"""
    app_client = Client(SESSION_NAME, API_ID, API_HASH)
    
    try:
        print("🔄 Connessione a Telegram...")
        await app_client.start()
        
        print("📤 Invio messaggio di test a te stesso...")
        message = "🧪 TEST PROP LEADER - Se ricevi questo messaggio, il sistema funziona! ✅\n\nQuesto è un messaggio di test dal sistema di automazione."
        
        # Invia a "me" (se stesso)
        sent = await app_client.send_message("me", message)
        
        print("✅ Messaggio inviato con successo!")
        print(f"📱 ID Messaggio: {sent.id}")
        print(f"📅 Data: {sent.date}")
        print("\n💡 Controlla Telegram per verificare la ricezione!")
        
        await app_client.stop()
        return True
        
    except Exception as e:
        print(f"❌ Errore: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("🧪 TEST DIRETTO INVIO MESSAGGIO TELEGRAM")
    print("=" * 60)
    print()
    
    result = asyncio.run(send_test_message())
    
    if result:
        print("\n✅ Test completato con successo!")
    else:
        print("\n❌ Test fallito. Controlla gli errori sopra.")

