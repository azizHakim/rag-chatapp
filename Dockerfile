FROM python:3.11-slim
#FROM ubuntu:22.04

WORKDIR /app
ADD ./requirements.txt /app/requirements.txt
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

ADD . /app
RUN pip install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "chatapp.py", "--server.port=8501", "--server.address=0.0.0.0"]