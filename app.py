from flask import Flask, render_template, request, jsonify
import ollama
import json


class AIAgent:
    """Handles model configuration and interactions with Ollama."""

    def __init__(self, json_file='static/data/model.json'):
        self.model = self.load_model(json_file)

    def load_model(self, json_file):
        """Load the model configuration from a JSON file."""
        with open(json_file, 'r') as file:
            return json.load(file)

    def get_response(self, user_prompt="Introduce yourself."):
        """Generate a chat response."""
        messages = [
            {"role": "system", "content": self.model['model']['system_prompt']},
            {"role": "user", "content": user_prompt}
        ]
        try:
            response = ollama.chat(
                model=self.model['model']['ollama_model'],
                messages=messages,
                options={"temperature": 0.3},
                stream=False,
            )
            return response.get('message', {}).get('content', '').strip()
        except Exception as e:
            print(f"Error getting response from {self.model['model']['name']}: {e}")
            return None


app = Flask(__name__)
ai_agent = AIAgent() 


@app.route('/')
def index():
    general_info = ai_agent.get_response()
    return render_template('index.html', general_info=general_info)


@app.route('/get_region_info', methods=['POST'])
def get_region_info():
    region_name = request.json.get('region')
    regional_info = ai_agent.get_response(region_name)
    return jsonify({"info": regional_info})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")