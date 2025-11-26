#!/usr/bin/env python3
"""
Script automatico per testare la sessione e inviare un messaggio.
Se la sessione non è valida, fornisce istruzioni chiare.
"""
import asyncio
import sys
from pyrogram import Client

API_ID = 31738726
API_HASH = "3c64e7c0d6c4c47524ae1b49102715ea"
SESSION_NAME = "prop_leader_user_session"

async def test_and_send(user_id, message):
    """Testa la sessione e invia un messaggio"""
    app_client = Client(SESSION_NAME, API_ID, API_HASH)
    
    try:
        print("🔄 Tentativo di connessione a Telegram...")
        print("   (Se viene richiesto il numero di telefono, la sessione non è valida)\n")
        
        await app_client.start()
        
        # Se arriviamo qui, la sessione è valida!
        me = await app_client.get_me()
        print(f"✅ Sessione valida!")
        print(f"   Utente: {me.first_name} {me.last_name or ''} (@{me.username or 'N/A'})")
        print(f"   ID: {me.id}\n")
        
        print(f"📤 Invio messaggio a user_id: {user_id}")
        print(f"💬 Messaggio: {message}\n")
        
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
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Operazione annullata dall'utente")
        return False
    except Exception as e:
        error_msg = str(e)
        print("\n" + "=" * 60)
        print("❌ ERRORE")
        print("=" * 60)
        
        if "phone number" in error_msg.lower() or "EOF" in error_msg:
            print("⚠️  La sessione Telegram non è valida o è scaduta.")
            print("\n📋 Per rigenerare la sessione:")
            print("   1. Esegui: python3 authenticate.py")
            print("   2. Inserisci il tuo numero di telefono")
            print("   3. Inserisci il codice di verifica da Telegram")
            print("   4. Inserisci la password 2FA (se attiva)")
        else:
            print(f"Errore: {error_msg}")
            print("\n💡 Possibili cause:")
            print("   - User ID non valido")
            print("   - Utente ha bloccato il tuo account")
            print("   - Problemi di connessione")
        
        return False

if __name__ == "__main__":
    # User ID e messaggio di default
    user_id = 167571343
    message = "🧪 Test di invio messaggio dal sistema Prop Leader!\n\nSe ricevi questo messaggio, il sistema funziona correttamente! ✅"
    
    # Permetti override da riga di comando
    if len(sys.argv) > 1:
        user_id = int(sys.argv[1])
    if len(sys.argv) > 2:
        message = " ".join(sys.argv[2:])
    
    print("=" * 60)
    print("🤖 TEST AUTOMATICO INVIO MESSAGGIO TELEGRAM")
    print("=" * 60)
    print()
    
    try:
        result = asyncio.run(test_and_send(user_id, message))
        if result:
            print("\n✅ Test completato con successo!")
            sys.exit(0)
        else:
            print("\n❌ Test fallito.")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Test interrotto dall'utente")
        sys.exit(1)

