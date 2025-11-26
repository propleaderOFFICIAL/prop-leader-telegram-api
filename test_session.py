#!/usr/bin/env python3
"""Test rapido per verificare se la sessione è valida"""
import asyncio
from pyrogram import Client

API_ID = 31738726
API_HASH = "3c64e7c0d6c4c47524ae1b49102715ea"
SESSION_NAME = "prop_leader_user_session"

async def test_session():
    app_client = Client(SESSION_NAME, API_ID, API_HASH)
    try:
        await app_client.start()
        me = await app_client.get_me()
        print(f"✅ Sessione valida! Utente: {me.first_name} (@{me.username})")
        await app_client.stop()
        return True
    except Exception as e:
        print(f"❌ Sessione non valida: {e}")
        return False

if __name__ == "__main__":
    result = asyncio.run(test_session())

