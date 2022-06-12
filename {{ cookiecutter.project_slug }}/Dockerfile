FROM python:3.10.4-bullseye
# Optional method to bake the commit id into the image `docker build --build-arg COMMIT_ID=abcdef12 .`
ARG COMMIT_ID
ENV COMMIT_ID=$COMMIT_ID

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8000
WORKDIR /app

#RUN apt-get update && apt-get install --yes \
#    libpq \
#    && rm -rf /var/lib/apt/lists/*

# install Poetry
ENV POETRY_VERSION=1.1.13
RUN python3 -m pip install --no-cache-dir poetry==$POETRY_VERSION
# place virtual environment inside the project directory (/app/.venv/)
RUN poetry config virtualenvs.in-project true --local

COPY poetry.lock pyproject.toml ./
RUN poetry install --no-dev

COPY . /app

RUN {{ cookiecutter.project_slug.upper() }}_IS_DEBUG=True poetry run python /app/{{ cookiecutter.project_slug }}/manage.py collectstatic --noinput

CMD ["/app/.venv/bin/gunicorn", \
    "--chdir", "/app/{{ cookiecutter.project_slug }}", \
    "--bind", "0.0.0.0:8000", \
    "{{ cookiecutter.project_slug }}.wsgi:application"]
