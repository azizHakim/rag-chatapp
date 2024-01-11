# RAG chatapp for financial analysis

### Installation and Runnning
1. get the repo: `git clone git@github.com:azizHakim/rag-chatapp.git`
2. cd into the repo folder: `cd rag-chatapp`
3. rename `env.sample` to `.env`:  `mv env.sample .env`
4. assign your openai api key to `OPENAI_API_KEY` variable inside `.env`
5. (Optional) you can change the openai model by updating the `OPENAI_MODEL`, given that you have access to the model.
6. (Optional) Also you can change the number of articles to be retrived by changing the value of `MAX_ARTICLE_NUMBER`, default is set to 3.
3. build the docker image: `docker build . -t chatapp`
4. run the docker image: `docker run --shm-size="2g" -p 8501:8501 chatapp`
5. finally go to `http://localhost:8501` to enjoy the app

### Tech stack used
1. Streamlit, for GUI.
2. OpenAI API, chat operation.
2. llama_index, for indexing related news articles.
3. Selenium, for scrapping news articles.

### How it works
1. During startup, llama_index reads and stores PDF documents from the `data/` folder into a vector store.
2. Upon a user's question, up to three relevant articles are fetched from financial times and added to the existing vector store.
3. With each subsequent question, the index nodes based on user inputs are updated according to the current question. If no article data is found, the corresponding nodes are set to "blank." This approach ensures that the chatbot maintains context to provide answers, and when no relevant articles can be retrieved, the default context in the `data/` folder is utilized for responding.
4. The `get_article_data` function runs on separate threads for each article to reduce scraping time, enhancing the user experience.
5. We have implemented "context" as the `chat_mode`, and future exploration of other [chat modes](https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/usage_pattern.html#configuring-a-chat-engine) can be considered based on specific requirements.