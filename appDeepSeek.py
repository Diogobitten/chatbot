from flask import Flask, request, jsonify, render_template
import requests  # Use requests to call the DeepSeek API
import logging
from flask_cors import CORS  # Enable CORS for frontend-backend communication

app = Flask(__name__, template_folder='templates')
CORS(app)  # Allow cross-origin requests

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Set your DeepSeek API key and endpoint
DEEPSEEK_API_KEY = "sk-3c76b395dbc14e1bb302bbde292ef364"
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"  # Example endpoint, adjust as needed

# Predefined answers dictionary with friendly tone and emojis
predefined_answers = {
    "what are your hours of operation?": "⏰ We are open from 9 AM to 9 PM, Monday to Friday. Come visit us anytime during these hours! 😊",
    "where are you located?": "📍 We are located at 123 Main Street, Cityville. We'd love to see you here! 🗺️",
    "do you offer delivery?": "🚚 Yes, we deliver within a 5-mile radius. Enjoy our goodies from the comfort of your home! 🏠",
    "what is on the menu?": "🍴 We offer coffee, sandwiches, and desserts. Perfect for any time of the day! ☕🍰🥪"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get the user's message from the request
        user_message = request.json.get('message', '').strip().lower()  # Convert to lowercase for case-insensitive matching
        if not user_message:
            logging.error("No message provided in the request.")
            return jsonify({'response': '🤔 Please provide a message to chat. I’m here to help!'}), 400

        logging.debug(f"User message: {user_message}")

        # Check for an exact match in predefined answers
        if user_message in predefined_answers:
            response = predefined_answers[user_message]
            logging.debug(f"Predefined answer found: {response}")
            return jsonify({'response': response})

        # If no predefined match is found, use DeepSeek API as a fallback
        logging.info("No predefined match found. Falling back to DeepSeek API.")
        headers = {
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "deepseek-chat",  # Adjust the model name as per DeepSeek's documentation
            "messages": [
                {"role": "system", "content": "You are a friendly and helpful restaurant chatbot."},
                {"role": "user", "content": user_message}
            ]
        }
        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data)
        response_data = response.json()
        bot_reply = response_data['choices'][0]['message']['content']
        logging.debug(f"DeepSeek API response: {bot_reply}")
        return jsonify({'response': bot_reply})

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({'response': '😔 Oops! Something went wrong. Please try again later.'}), 500

if __name__ == '__main__':
    app.run(debug=True)