# RAG chatapp for financial analysis

A financial assistant chatbot powered by Retrieval Augmented Generation (RAG) with Streamlit and ChatGPT, Selenium to answer queries regarding finance by scraping through the latest financial news articles. 

Checkout the live version [here](https://rag-chatapp-sbeilyjgrq-uc.a.run.app/) (deployed on GCP with cloud build and cloud run).
![rag-chatapp demo](https://github.com/azizHakim/rag-chatapp/blob/master/images/rag-chatapp-demo.png?raw=true)


### ✔️ Installation and Runnning
1. Get the repo: 
   - `git clone git@github.com:azizHakim/rag-chatapp.git`
2. cd into the root directory: 
   - `cd rag-chatapp`
3. Rename `env.sample` to `.env`:  
    - `mv env.sample .env`
4. Assign your openai api key to `OPENAI_API_KEY` variable inside `.env`
5. (Optional) You can change the openai model by updating the `OPENAI_MODEL`, given that you have access to the model.
6. (Optional) Also you can change the number of articles to be retrived by changing the value of `MAX_ARTICLE_NUMBER`, default is set to 3.
3. Build the docker image: 
    - `docker build . -t chatapp`
4. Run the docker image: 
     - `docker run -p 8501:8501 chatapp`
5. Finally go to `http://localhost:8501` to enjoy the app


### ⚙️ Tech stack
- Streamlit==1.29.0
- OpenAI API==1.6.1
- LlamaIndex==0.9.26
- Selenium==4.16.0
- Docker

### 🔲 Future work
1. Chunking documents before vectorizing for better better retrieval.
2. Evaluate the retrieval performance.


### ©️ License

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=for-the-badge&logoColor=white)](https://opensource.org/licenses/Apache-2.0)


## 📫 How to reach me 

Feel free to reach out to me on [Twitter](https://twitter.com/aziz_raihan19) or [LinkedIn](https://www.linkedin.com/in/aziz-hakim) for collaboration. Know more about me at [azizhakim.github.io](https://azizhakim.github.io)

[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/aziz_raihan19)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:hakim.smazizul@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aziz-hakim)