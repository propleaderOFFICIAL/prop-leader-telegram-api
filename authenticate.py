from pyrogram import Client

API_ID = 31738726
API_HASH = "3c64e7c0d6c4c47524ae1b49102715ea"
SESSION_NAME = "prop_leader_user_session"

print("=" * 60)
print("🔐 AUTENTICAZIONE TELEGRAM - Prop Leader")
print("=" * 60)
print("\nQuesto script genererà il file di sessione necessario.")
print("Ti verrà chiesto di inserire:")
print("  1. Il tuo numero di telefono (con prefisso, es. +39123456789)")
print("  2. Il codice di verifica inviato da Telegram")
print("  3. La password 2FA (se attiva)\n")
print("=" * 60)
print()

# Il client si avvia, ti chiederà numero di telefono, codice e password 2FA.
try:
    with Client(SESSION_NAME, API_ID, API_HASH) as app:
        app.send_message("me", "Autenticazione Prop Leader completata con successo! 🚀")
        print("\n✅ Autenticazione completata con successo!")
        print(f"📁 File di sessione creato: {SESSION_NAME}.session")
        print("\nOra puoi caricare questo file su Replit!")
except Exception as e:
    print(f"\n❌ Errore durante l'autenticazione: {e}")
    print("\nAssicurati di:")
    print("  - Usare il formato corretto del numero (es. +39123456789)")
    print("  - Inserire il codice di verifica entro il tempo limite")
    print("  - Avere una connessione internet stabile")

