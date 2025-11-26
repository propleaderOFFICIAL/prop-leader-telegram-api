#!/usr/bin/env python3
"""
Script completo: autenticazione + test invio messaggio
Esegue l'autenticazione e poi testa l'invio a un user_id specifico.
"""
import asyncio
from pyrogram import Client

API_ID = 31738726
API_HASH = "3c64e7c0d6c4c47524ae1b49102715ea"
SESSION_NAME = "prop_leader_user_session"

async def authenticate_and_test(user_id, message):
    """Autentica e invia un messaggio di test"""
    print("=" * 60)
    print("🔐 AUTENTICAZIONE E TEST TELEGRAM")
    print("=" * 60)
    print()
    print("📋 Passo 1: Autenticazione")
    print("   Ti verrà chiesto di inserire:")
    print("   - Numero di telefono (es. +39123456789)")
    print("   - Codice di verifica da Telegram")
    print("   - Password 2FA (se attiva)")
    print()
    print("=" * 60)
    print()
    
    app_client = Client(SESSION_NAME, API_ID, API_HASH)
    
    try:
        # Avvia il client (richiederà autenticazione se necessario)
        await app_client.start()
        
        # Verifica che l'autenticazione sia andata a buon fine
        me = await app_client.get_me()
        print("\n✅ Autenticazione completata!")
        print(f"   Utente: {me.first_name} (@{me.username or 'N/A'})")
        print()
        
        # Invia messaggio di conferma a se stesso
        await app_client.send_message("me", "Autenticazione Prop Leader completata con successo! 🚀")
        print("📱 Messaggio di conferma inviato a te stesso")
        print()
        
        # Passo 2: Test invio messaggio
        print("=" * 60)
        print("📤 Passo 2: Test invio messaggio")
        print("=" * 60)
        print()
        print(f"👤 Destinatario: {user_id}")
        print(f"💬 Messaggio: {message}")
        print()
        
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
        
        print("\n✅ Tutto completato con successo!")
        return True
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Operazione annullata")
        return False
    except Exception as e:
        print(f"\n❌ Errore: {e}")
        return False

if __name__ == "__main__":
    # User ID e messaggio di default
    user_id = 167571343
    message = "🧪 Test di invio messaggio dal sistema Prop Leader!\n\nSe ricevi questo messaggio, il sistema funziona correttamente! ✅"
    
    result = asyncio.run(authenticate_and_test(user_id, message))
    
    if not result:
        print("\n💡 Se l'autenticazione è fallita, assicurati di:")
        print("   - Usare il formato corretto del numero (es. +39123456789)")
        print("   - Inserire il codice di verifica entro il tempo limite")
        print("   - Avere una connessione internet stabile")

