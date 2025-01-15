from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    api_key = os.getenv("API_KEY")
    genai.configure(api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    user_input = request.json.get('message')
    response = model.generate_content(user_input)
    return jsonify({"response": response.text})

if __name__ == '__main__':
    app.run(debug=True)