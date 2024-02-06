# RAG chatapp for financial analysis

### Installation and Runnning
1. Get the repo: `git clone git@github.com:azizHakim/rag-chatapp.git` or if you have the zipped repo unzip it.
2. cd into the root directory: `cd rag-chatapp`
3. Rename `env.sample` to `.env`:  `mv env.sample .env`
4. Assign your openai api key to `OPENAI_API_KEY` variable inside `.env`
5. (Optional) You can change the openai model by updating the `OPENAI_MODEL`, given that you have access to the model.
6. (Optional) Also you can change the number of articles to be retrived by changing the value of `MAX_ARTICLE_NUMBER`, default is set to 3.
3. Build the docker image: `docker build . -t chatapp`
4. Run the docker image: `docker run --shm-size="2g" -p 8501:8501 chatapp`
5. Finally go to `http://localhost:8501` to enjoy the app

### Tech stack used
1. Streamlit, for GUI.
2. OpenAI API, chat operation.
2. llama_index, for indexing related news articles.
3. Selenium, for scrapping news articles.

### Future work
1. We have implemented "context" as the `chat_mode`, and future exploration of other [chat modes](https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/usage_pattern.html#configuring-a-chat-engine) can be considered based on specific requirements.
2. Evaluate and optimize RAG for better retrival.