# RAG (Retrieval Augmented Generation)

1. Create .venv and install the requirements: `pip install -r requirements.txt`
3. Make sure you have the models listed in config.ini.
4. Make sure you have running ChromaDB.
5. Edit the list of docs in `sourcedocs.txt`
6. Load the source docs: `python3 load.py`
7. Start searching: `python3 search.py <your_search_request>`

*A query example: `python3 search.py What is ollama?`*

*An answer example:*
> Ollama is a local and secure platform for deploying Large Language Models (LLMs), allowing users to maintain control over sensitive data and prioritize privacy in industries such as healthcare, finance, and government.