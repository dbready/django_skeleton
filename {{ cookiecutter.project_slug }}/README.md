# {{ cookiecutter.project_name }}

## Development Quickstart

- `poetry install` to construct the Python virtual environment with [Poetry](https://github.com/python-poetry/poetry). If not using poetry, can install dependencies into a virtual environment using pip (`pip install .`)
- `cp example.env .env` for local configuration settings not appropriate for source control
- load .env environment variables, suggest using [direnv](https://github.com/direnv/direnv) to auto load the configuration (`direnv allow .`)
- `poetry run python {{ cookiecutter.project_slug }}/manage.py migrate` to construct the local development database (alternatively, run inside Poetry shell `poetry shell` and then run `python {{ cookiecutter.project_slug }}/manage.py migrate`)
- `poetry run python {{ cookiecutter.project_slug }}/manage.py runserver` to launch the development web server

## License

Code is dual licensed under [Apache 2](https://www.apache.org/licenses/LICENSE-2.0.html) and [MIT](https://opensource.org/licenses/MIT).
All contributions to this project will be licensed under the same.
