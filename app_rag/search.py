import sys

import chromadb
import ollama

from utilities import getconfig

COLLECTION_NAME = "python_rag_example"

embedmodel = getconfig()["embedmodel"]
mainmodel = getconfig()["mainmodel"]
chroma = chromadb.HttpClient(host="localhost", port=8010)
collection = chroma.get_or_create_collection(COLLECTION_NAME)

query = " ".join(sys.argv[1:])
print(f"\nquery: \n{query}")
queryembed = ollama.embeddings(model=embedmodel, prompt=query)["embedding"]

### n_results=5; 10 - default
relevantdocs = collection.query(query_embeddings=[queryembed], n_results=3)[
    "documents"
][0]
docs = "\n\n".join(relevantdocs)
print(f"\ndocs: \n{docs}")

# <think>...</think> block
modelquery = (
    f"Question: {query} \n\n"
    f"Answer that question shortly "
    f"using the following text as a resource: \n\n{docs}"
)
print(f"\nmodelquery: \n{modelquery}\n\n")

stream = ollama.generate(model=mainmodel, prompt=modelquery, stream=True)

print(f"\nAnswering...\n")
for chunk in stream:
    if chunk["response"]:
        print(chunk["response"], end="", flush=True)

print("\n\n")
