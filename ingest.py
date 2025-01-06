import os
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from ollama import embeddings
from qdrant_client.models import PointStruct, VectorParams, Distance
import requests
import shortuuid
import json
import time
import random


qdrant_client = QdrantClient(
    url= os.getenv("QDRANT_URL"), 
    api_key="A97ywzviKu5LylwwpAuFg3v-seSzqJIQHNI59_xa2B7MFCjqKOL4hw",
)

collection_name = "web_scrapper"

fetchURL = os.getenv("FETCH_URL"), 
headers = { "Content-Type": "application/json" }

# qdrant_client.create_collection(collection_name="web_scrapper",
#                                 vectors_config=VectorParams(size=768, distance=Distance.DOT))
# print(qdrant_client.get_collections())


# Define your text
# text = "The sky is blue because of Rayleigh scattering"

# # Generate embeddings
def get_embeddings(text):
    return embeddings(model='nomic-embed-text', prompt=text)

def generate_unique_id(): 
    return random.randint(1, 10**10)

def upload_to_qdrant(text):
    embeddings = get_embeddings(text)
    print(embeddings)
    operation_info = qdrant_client.upsert(
        collection_name="web_scrapper",
        wait=True,
        points=[
            PointStruct(id=generate_unique_id(), vector=embeddings.embedding, payload={"data": text}),
        ],
    )
    print(operation_info)
    return operation_info

def search_in_qdrant(text):
    embeddings = get_embeddings(text)
    search_results = qdrant_client.query_points(
        collection_name="web_scrapper",
        query=embeddings.embedding,
        with_payload=True,
        limit=2
    )
    print(search_results)
    return search_results



