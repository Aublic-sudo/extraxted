FROM python:3.9.7-slim-buster

WORKDIR /app
COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD ["python", "./main.py"]


