# from sentence_transformers import SentenceTransformer
# from langchain_community.vectorstores import Pinecone as LangchainPinecone
# import os
# from pinecone import Pinecone, ServerlessSpec
# from config import PINECONE_API_KEY

# def setup_vector_store(documents, index_name="brainlox-course-index"):
#     # Initialize SentenceTransformer model
#     model = SentenceTransformer('all-MiniLM-L6-v2')
    
#     # Initialize Pinecone client
#     pinecone_client = Pinecone(api_key=PINECONE_API_KEY)
    
#     # Check if the index exists, if not, create it
#     if index_name not in pinecone_client.list_indexes().names():
#         pinecone_client.create_index(
#             name=index_name,
#             dimension=384,  # Dimension of 'all-MiniLM-L6-v2' embeddings
#             metric='euclidean',
#             spec=ServerlessSpec(
#                 cloud='aws',
#                 region='us-west-2'
#             )
#         )
    
#     # Generate embeddings for each document
#     document_texts = [doc.page_content for doc in documents]
#     embeddings = model.encode(document_texts)
    
#     # Use LangChain's Pinecone wrapper to handle vector storage
#     vector_store = LangchainPinecone.from_documents(
#         documents, 
#         embeddings, 
#         index_name=index_name,
#         pinecone_client=pinecone_client
#     )
    
#     return vector_store

# if __name__ == "__main__":
#     from data_loader import extract_data
    
#     url = "https://brainlox.com/courses/category/technical"
#     documents = extract_data(url)
#     vector_store = setup_vector_store(documents)
#     print("Vector store is set up.")

'''-------------------------------------------------------------------------------'''
# embedding_store.py

from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import Pinecone as LangchainPinecone
import os
from pinecone import Pinecone, ServerlessSpec
from config import PINECONE_API_KEY

def setup_vector_store(documents, index_name="brainlox-course-index"):
    # Initialize SentenceTransformer model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Initialize Pinecone client
    pinecone_client = Pinecone(api_key=PINECONE_API_KEY)
    
    # Check if the index exists, if not, create it
    if index_name not in pinecone_client.list_indexes().names():
        pinecone_client.create_index(
            name=index_name,
            dimension=384,  # Dimension of 'all-MiniLM-L6-v2' embeddings
            metric='euclidean',
            spec=ServerlessSpec(
                cloud='gcp',
                region='us-east1'  # Use a region supported by your Pinecone plan
            )
        )
    
    # Generate embeddings for each document
    document_texts = [doc.page_content for doc in documents]
    embeddings = model.encode(document_texts)
    
    # Use LangChain's Pinecone wrapper to handle vector storage
    vector_store = LangchainPinecone.from_documents(
        documents, 
        embeddings, 
        index_name=index_name,
        pinecone_client=pinecone_client
    )
    
    return vector_store

if __name__ == "__main__":
    from data_loader import extract_data
    
    url = "https://brainlox.com/courses/category/technical"
    documents = extract_data(url)
    vector_store = setup_vector_store(documents)
    print("Vector store is set up.")