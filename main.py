from flask import Flask, request, jsonify
import os
import subprocess
import json

app = Flask(__name__)

# Endpoint di test per verificare che il server funzioni
@app.route('/', methods=['GET'])
def health_check():
    return jsonify({
        "status": "online",
        "service": "Prop Leader Telegram User API",
        "endpoint": "/prop_leader/send_message"
    }), 200

# L'endpoint Webhook che n8n colpirà.
@app.route('/prop_leader/send_message', methods=['POST'])
def send_telegram_message():
    data = request.json
    
    # 1. ESTREZIONE DATI CONCRETI (Dall'n8n)
    user_id = data.get('user_id')
    first_name = data.get('first_name', 'Membro')
    message_text = data.get('message', "Messaggio di default: contatta Prop Leader.")

    if not user_id:
        return jsonify({"status": "error", "message": "user_id mancante"}), 400

    # 2. STRUTTURA DEL MESSAGGIO PERSONALIZZATO (ZERO FILTRI!)
    final_message = f"🚨 Ehi {first_name}! {message_text}"

    # 3. AZIONE: INVIARE TRAMITE IL TUO ACCOUNT PERSONALE
    try:
        # Prepara i dati per lo script esterno
        script_path = os.path.join(os.path.dirname(__file__), "telegram_sender.py")
        
        # Verifica che lo script esista
        if not os.path.exists(script_path):
            return jsonify({"status": "failure", "error": f"Script non trovato: {script_path}", "user": user_id}), 500
        
        input_data = json.dumps({
            "user_id": int(user_id),
            "message": final_message
        })
        
        # Esegui lo script come subprocess (isolato completamente da Flask)
        import sys
        process = subprocess.Popen(
            [sys.executable, script_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=os.path.dirname(__file__)
        )
        
        stdout, stderr = process.communicate(input=input_data, timeout=30)
        
        if process.returncode != 0:
            error_msg = stderr.strip() if stderr else "Errore sconosciuto durante l'esecuzione"
            # Se è un errore di autenticazione (file sessione mancante), è normale
            if "session" in error_msg.lower() or "phone number" in error_msg.lower():
                error_msg = "File di sessione mancante. Esegui authenticate.py per generarlo."
            return jsonify({"status": "failure", "error": error_msg, "user": user_id, "returncode": process.returncode}), 500
        
        # Parse del risultato
        try:
            result = json.loads(stdout.strip())
        except json.JSONDecodeError:
            return jsonify({"status": "failure", "error": f"Risposta non valida: {stdout[:200]}", "user": user_id}), 500
        
        if result.get("success"):
            return jsonify({"status": "success", "message": f"Messaggio inviato a {user_id}"}), 200
        else:
            return jsonify({"status": "failure", "error": result.get("error", "Errore sconosciuto"), "user": user_id}), 500
        
    except subprocess.TimeoutExpired:
        if 'process' in locals():
            process.kill()
        return jsonify({"status": "failure", "error": "Timeout durante l'invio del messaggio", "user": user_id}), 500
    except Exception as e:
        # Gestione degli errori (es. utente ha bloccato il tuo account)
        import traceback
        error_trace = traceback.format_exc()
        return jsonify({"status": "failure", "error": str(e), "traceback": error_trace[:500], "user": user_id}), 500

if __name__ == '__main__':
    # Esegui il server sulla porta fornita dall'ambiente di hosting (es. Replit)
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 8080))

