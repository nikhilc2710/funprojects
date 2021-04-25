FROM python:3

RUN apt-get update && apt-get install -y libzbar0

WORKDIR /app

COPY requirements.txt ./

RUN pip install  -r requirements.txt

EXPOSE 5000
EXPOSE $PORT

COPY . .

CMD ["python","./app.py"]

