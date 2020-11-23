FROM python:3.7.9

ENV PYTHONUNBUFFERED 1

RUN ls .

WORKDIR /code
# Install packages
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/