from flask import Flask, request, jsonify
from retriever import retrieve_answer
from config import COHERE_API_KEY
import cohere
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to connect

# Initialize Cohere
co = cohere.Client(COHERE_API_KEY)

@app.route('/chat', methods=['POST'])
def chat():
    user_query = request.json.get('query')
    if not user_query:
        return jsonify({'error': 'Query missing'}), 400
    
    # Retrieve answer using retriever
    response = retrieve_answer(user_query, co)
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
  
