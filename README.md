# RAG chatapp for financial analysis

### Installation
1. get the repo git clone
2. cd rag-chatapp
3. rename `.env_sample` to `.env`. run this command `mv .env_sample .env`
4. assign your openai api key to `OPENAI_API_KEY` variable inside `.env`
5. (Optional) you can change the openai model by updating the `OPENAI_MODEL`, given that you have access to the model.
3. build the docker image `docker build . -t chatapp`
4. run the docker image `docker run --shm-size="2g" -p 8501:8501 chatapp`
5. finally go to `http://localhost:8501` to enjoy the app

### Tech stack used
1. Streamlit, for GUI.
2. OpenAI API, chat operation.
2. llama_index, for indexing related news articles.
3. Selenium, for scrapping news articles.