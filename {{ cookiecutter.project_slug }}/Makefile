.PHONY : collectstatic
collectstatic :
	export {{ cookiecutter.project_slug.upper() }}_IS_DEBUG=True; poetry run python {{ cookiecutter.project_slug }}/manage.py collectstatic --no-input

.PHONY : docker
docker :
	podman build --build-arg GIT_COMMIT=$(git rev-parse HEAD) --tag {{ cookiecutter.project_slug }}:latest .

.PHONY : docker_image
docker_image : # not requiring rebuild of image - not necessarily fresh
	mkdir --parents dist/
	timestamp=$(shell date --utc "+%Y%m%dT%H%M%SZ"); \
	podman save --output "dist/{{ cookiecutter.project_slug }}_$${timestamp}.tar" {{ cookiecutter.project_slug }}:latest

.PHONY : test
test : collectstatic # whitenoise static handling requires collectstatic be run first. potentially slow
	poetry run pytest
