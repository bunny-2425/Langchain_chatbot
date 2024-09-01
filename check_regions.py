from pinecone import Pinecone

PINECONE_API_KEY = "your_pinecone_api_key"  # Replace with your actual API key
region = "us-west1-gcp"  # Replace with your intended region

pinecone_client = Pinecone(api_key=PINECONE_API_KEY)

try:
    # Attempt to connect to the specified region
    pinecone_client.create_index(
        name="test_index",
        dimension=1536,
        metric="euclidean",
        spec={"cloud": "gcp", "region": region}
    )
    print(f"Successfully connected to region: {region}")
except Exception as e:
    print(f"Failed to connect to region: {region}. Error: {str(e)}")
