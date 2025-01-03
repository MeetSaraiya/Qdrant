import requests
from ingest import upload_to_qdrant , search_in_qdrant

def chuck_text(text,chunk_size=2000):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]


def upload_embeddings(text):
    chunks = chuck_text(text)
    for i,chunk in enumerate(chunks):
        print(f"Uploading chunk {i}")
        upload_to_qdrant(chunk)
    print("Upload complete")
    
trialText = "tell me something about tiger" 


# upload_embeddings(trialText)
search_in_qdrant(trialText)

