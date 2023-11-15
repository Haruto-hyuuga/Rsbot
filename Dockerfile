FROM python:3.11-slim-buster
WORKDIR /app
RUN apt install -y git
COPY requirements.txt requirements.txt
RUN pip3 install -U -r requirements.txt

COPY . .

CMD python3 main.py
