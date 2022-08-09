# Denver Python Website

This is the repository for the Denver Python website at [insituexsilico.info](https://insituexsilico.info).

<!-- [![Circle CI](https://circleci.com/gh/In-Situ-ex-Silico/groupsite-django/tree/main.svg?style=shield)](https://circleci.com/gh/In-Situ-ex-Silico/groupsite-django/tree/main) -->
[![AppVeyor](https://ci.appveyor.com/api/projects/status/184l9lc8y7av2fah?svg=true)](https://ci.appveyor.com/project/davidfischer/groupsite-django)
<!-- [![Requirements Status](https://requires.io/github/In-Situ-ex-Silico/groupsite-django/requirements.svg?branch=main)](https://requires.io/github/In-Situ-ex-Silico/groupsite-django/requirements/?branch=main) -->


## Developing

### Prerequisites

* Python 3.7+

### Getting started (local development)

```shell
pip install -r requirements/local.txt  # Install local Python requirements
pre-commit install                     # Setup code standard pre-commit hook
./manage.py migrate                    # Create a local development database
./manage.py createsuperuser            # Create a local development administrator user
./manage.py runserver                  # Starts a local development server at http://localhost:8000
# or
gunicorn -c config/gunicorn/dev.py
```

### Production Deployment

```shell
./build.sh                             # Install production Python requirements and run manage.py ops
gunicorn -c config/gunicorn/prod.py    # Run the server
```
