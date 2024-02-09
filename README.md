# RAG chatapp for financial analysis

### Installation and Runnning
1. Get the repo: `git clone git@github.com:azizHakim/rag-chatapp.git`
2. cd into the root directory: `cd rag-chatapp`
3. Rename `env.sample` to `.env`:  `mv env.sample .env`
4. Assign your openai api key to `OPENAI_API_KEY` variable inside `.env`
5. (Optional) You can change the openai model by updating the `OPENAI_MODEL`, given that you have access to the model.
6. (Optional) Also you can change the number of articles to be retrived by changing the value of `MAX_ARTICLE_NUMBER`, default is set to 3.
3. Build the docker image: `docker build . -t chatapp`
4. Run the docker image: `docker run --shm-size="2g" -p 8501:8501 chatapp`
5. Finally go to `http://localhost:8501` to enjoy the app

### Tech stack used
1. Streamlit==1.29.0
2. OpenAI API==1.6.1
2. LlamaIndex==0.9.26
3. Selenium==4.16.0
4. Docker

### Future work
1. Chunking documents before vectorizing for better better retrieval.
2. Evaluate the retrieval performance.