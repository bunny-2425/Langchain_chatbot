from pinecone import Pinecone

pinecone_client = Pinecone(api_key="a3b80409-5985-4b30-b718-112e60831a20")
regions = pinecone_client.list_regions()
print(regions)