import os
import time

import chromadb
import nltk
import ollama

from tools import chunk_text_by_sentences
from utilities import getconfig, readtext

COLLECTION_NAME = "python_rag_example"

app_path = os.path.dirname(os.path.abspath(__file__))
print(app_path)

directory_nltk_data_path = f"{app_path}/.venv/nltk_data"
directory_punkt_tab_path = f"{directory_nltk_data_path}/tokenizers/punkt_tab"
if not os.path.isdir(directory_punkt_tab_path):
    print(directory_punkt_tab_path)
    nltk.download(
        info_or_id="punkt_tab", download_dir=directory_nltk_data_path
    )

chroma = chromadb.HttpClient(host="localhost", port=8010)
print(chroma.list_collections())
if any(
    collection == COLLECTION_NAME for collection in chroma.list_collections()
):
    print(f"deleting collection '{COLLECTION_NAME}'")
    chroma.delete_collection(COLLECTION_NAME)
collection = chroma.get_or_create_collection(
    name="python_rag_example", metadata={"hnsw:space": "cosine"}
)

embedmodel = getconfig()["embedmodel"]
starttime = time.time()
with open("sourcedocs.txt") as f:
    lines = f.readlines()
    print(lines)
    for filename in lines:
        print(f"\n\nfilename: {filename}")
        text = readtext(filename)

        chunks = chunk_text_by_sentences(
            source_text=text, sentences_per_chunk=7, overlap=0
        )
        print(f"with {len(chunks)} chunks")
        for index, chunk in enumerate(chunks):
            embed = ollama.embeddings(model=embedmodel, prompt=chunk)[
                "embedding"
            ]
            print(".", end="", flush=True)
            collection.add(
                [filename + str(index)],
                [embed],
                documents=[chunk],
                metadatas={"source": filename},
            )

print("\n--- %s seconds ---" % (time.time() - starttime))
