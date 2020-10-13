#!/bin/bash

docker run \
    --env-file=.env \
    --mount type=bind,source=.,target=/app \
    --publish 8000:8000 \
    --rm \
    localhost/skeleton /app_venv/bin/python /app/skeleton/manage.py runserver
