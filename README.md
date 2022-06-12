# Django Skeleton

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) based Django quick start.

Includes several niceties which I think any project eventually requires.
Likely too opinonated for anyone else's use, but I became tired of re-implementing the basics.

## Usage

By default, cookiecutter will deploy into the current working directory.
To specify new destination, use the `--output-dir <directory>` argument.

From git repository

```bash
cookiecutter https://github.com/dbready/django_skeleton.git
```

From local directory
```bash
cookiecutter ~/templates/django_skeleton
```
Will then produce a project outlined as below:

```
├── django_skeleton
│   ├── core
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── static
│   │   │   └── core
│   │   │       ├── css
│   │   │       │   ├── style.css
│   │   │       │   └── water.css
│   │   │       ├── icon
│   │   │       │   ├── android-icon-192x192.png
│   │   │       │   ├── android-icon-512x512.png
│   │   │       │   ├── apple-touch-icon.png
│   │   │       │   ├── favicon.ico
│   │   │       │   └── favicon.svg
│   │   │       └── img
│   │   │           └── logo.svg
│   │   ├── templates
│   │   │   └── core
│   │   │       ├── error
│   │   │       │   ├── 400.html
│   │   │       │   ├── 403.html
│   │   │       │   ├── 404.html
│   │   │       │   └── 500.html
│   │   │       ├── base.html
│   │   │       └── index.html
│   │   ├── tests
│   │   │   ├── __init__.py
│   │   │   └── test_pages.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── django_skeleton
│   │   ├── tests
│   │   │   ├── __init__.py
│   │   │   └── test_site.py
│   │   ├── asgi.py
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── wsgi.py
│   └── manage.py
├── CHANGELOG.md
├── Dockerfile
├── dockerignore
├── example.env
├── LICENSE-APACHE
├── LICENSE-MIT
├── Makefile
├── pyproject.toml
└── README.md
```


## License

This project is available under any of the following with which the user feels most comfortable.

    - Apache 2
    - CC0
    - MIT
