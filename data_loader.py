# data_loader.py

from langchain_community.document_loaders import WebBaseLoader

def extract_data(url):
    # Load data from the website using LangChain's WebBaseLoader
    loader = WebBaseLoader(url)
    documents = loader.load()
    return documents
