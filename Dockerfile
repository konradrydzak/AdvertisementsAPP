FROM python:3.9-slim-buster

RUN apt-get update && apt-get -y install libpq-dev gcc && pip install psycopg2

COPY ./src /src
COPY ./database.ini ./
COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8001
WORKDIR "src"
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001", "--insecure"]
