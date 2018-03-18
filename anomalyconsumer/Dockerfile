FROM python:3.6

RUN apt-get update

COPY ./requirements.txt /requirements.txt
COPY ./app.py /app.py

RUN pip install --no-cache-dir -r /requirements.txt

ENV BIND_PORT 5000

EXPOSE $BIND_PORT
CMD ["python3", "/app.py" ]
