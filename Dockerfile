FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /KZTwitterBot

COPY config.py /KZTwitterBot/
COPY app.py /KZTwitterBot/
COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

CMD ["python3", "app.py"]