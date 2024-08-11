from flask import Flask, render_template, request, jsonify
import requests

RASA_API_URL = "http://localhost:5005/webhooks/rest/webhook"  # Adjust this URL as needed
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    user_message = request.json.get('message')  # Use .get() to avoid KeyError if 'message' is not in JSON
    print("UserMessage:", user_message)

    # Send message to Rasa
    try:
        rasa_response = requests.post(RASA_API_URL, json={'message': user_message})
        rasa_response.raise_for_status()  # Raise an exception for 4xx and 5xx HTTP status codes
        rasa_response_json = rasa_response.json()
        bot_response = rasa_response_json[0]['text'] if rasa_response_json else 'Sorry, I don\'t get you'
    except Exception as e:
        print("Error sending message to Rasa:", e)
        bot_response = 'Sorry, something went wrong!'

    print("Rasa response:", bot_response)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True, port=7000)
