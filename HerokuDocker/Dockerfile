FROM python:3

WORKDIR /app

COPY requirements.txt ./

RUN pip install  -r requirements.txt

EXPOSE 8000
EXPOSE $PORT
COPY . .

CMD uvicorn server:app --host 0.0.0.0 --port $PORT