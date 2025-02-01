from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

# Inicializar o Flask primeiro
app = Flask(__name__)

from flask_cors import CORS
CORS(app, resources={r"/chat": {"origins": "https://diogobit.vercel.app"}}) # Permitir chamadas do frontend

# Configuração da API Key
openai.api_key = os.getenv("OPENAI_API_KEY")


# ID do Assistente configurado na OpenAI
ASSISTANT_ID = os.getenv("OPENAI_ASSISTANT_ID")  # ⚠️ Substitua pelo ID real do assistente


@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '').strip()
        if not user_message:
            return jsonify({'response': '🤔 Por favor, envie uma mensagem válida!'}), 400
        
        # Criar uma nova thread no assistente da OpenAI
        thread = openai.beta.threads.create(messages=[{"role": "user", "content": user_message}])
        run = openai.beta.threads.runs.create(thread_id=thread.id, assistant_id=ASSISTANT_ID)

        # Esperar a resposta da API
        while True:
            run_status = openai.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
            if run_status.status == "completed":
                break

        # Pegar a resposta
        messages = openai.beta.threads.messages.list(thread_id=thread.id)
        response_text = messages.data[0].content[0].text.value

        return jsonify({'response': response_text})

    except Exception as e:
        return jsonify({'response': f'😔 Ocorreu um erro: {e}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
