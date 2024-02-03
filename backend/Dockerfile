FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false --local

COPY ./manage.py /app/

COPY ./pyproject.toml ./poetry.lock* /app/

RUN poetry install --without dev

COPY ./appname /app/appname

EXPOSE $PORT

CMD uvicorn appname.config.wsgi:applications --host 0.0.0.0 --port $PORT
