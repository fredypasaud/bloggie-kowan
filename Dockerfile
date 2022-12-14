FROM python:3.8-slim-buster

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    DJANGO_SETTINGS_MODULE=bloggie.settings \
    PORT=8000 \
    WEB_CONCURRENCY=3

RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential curl \
    libpq-dev \
    libmariadbclient-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
 && rm -rf /var/lib/apt/lists/*

RUN addgroup --system django \
    && adduser --system --ingroup django django

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput --clear

RUN chown -R django:django /app
USER django

CMD gunicorn bloggie.wsgi:application