FROM --platform=linux/amd64 python:3.11-slim

WORKDIR /app

ADD ./requirements.txt /app/requirements.txt

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    wget \
    xvfb \
    unzip \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

ADD . /app

RUN pip install -r requirements.txt

ENV DISPLAY=:99

EXPOSE 8501

#RUN mkdir -p ~/.streamlit/
#RUN echo "[general]"  > ~/.streamlit/credentials.toml
#RUN echo "email = \"\""  >> ~/.streamlit/credentials.toml

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "chatapp.py", "--server.port=8501", "--server.address=0.0.0.0"]