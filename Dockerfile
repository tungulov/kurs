FROM python:3.11

WORKDIR /app

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

RUN apt-get -y update \
 && apt-get -y upgrade 

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install poetry
RUN poetry config virtualenvs.create false

COPY . .
RUN poetry install