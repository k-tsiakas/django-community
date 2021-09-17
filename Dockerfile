FROM python:3.6.5


RUN pip install --upgrade pip
WORKDIR /app
ADD requirements.txt /app

RUN pip install -r requirements.txt
# needed for logs
ENV PYTHONUNBUFFERED=1


ADD . /app



WORKDIR /app/community
