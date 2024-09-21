FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /workspace/back

RUN apt-get update \
    && apt-get install -y default-mysql-client \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip

COPY . .
RUN pip3 install -r ./requirements.txt
