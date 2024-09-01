# from flask import Flask, request, jsonify
# from embedding_store import setup_vector_store
# from data_loader import extract_data
# from config import OPENAI_API_KEY, PINECONE_API_KEY
# import os
# from dotenv import load_dotenv
# import os

# # Load environment variables from .env file
# load_dotenv()

# # Access environment variables
# OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
# PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')


# app = Flask(__name__)

# # Initialize vector store
# url = "https://brainlox.com/courses/category/technical"
# documents = extract_data(url)
# vector_store = setup_vector_store(documents)

# @app.route('/query', methods=['POST'])
# def query_vector_store():
#     user_query = request.json.get("query")
#     if not user_query:
#         return jsonify({"error": "Query is required"}), 400

#     response = vector_store.similarity_search(user_query, k=5)
#     return jsonify({"response": response})

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)

'''---------------------------------------------------------------------------------------'''
# app.py

from flask import Flask, request, jsonify
from embedding_store import setup_vector_store
from data_loader import extract_data

app = Flask(__name__)

# Load and set up the vector store on server start
url = "https://brainlox.com/courses/category/technical"
documents = extract_data(url)
vector_store = setup_vector_store(documents)

@app.route('/query', methods=['POST'])
def query_vector_store():
    user_query = request.json.get("query")
    response = vector_store.similarity_search(user_query, k=5)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)