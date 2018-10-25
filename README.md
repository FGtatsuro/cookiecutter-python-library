cookiecutter-python-library
==================================================

Cookiecutter template for Python Library project.

[![Build Status](https://travis-ci.org/FGtatsuro/cookiecutter-python-library.svg?branch=master)](https://travis-ci.org/FGtatsuro/cookiecutter-python-library)

Requirements
------------

Cookiecutter (>=1.6) (<https://github.com/audreyr/cookiecutter>)

How to
------

You can create new project of Cookiecutter template as follows.

```bash
$ cookiecutter gh:FGtatsuro/cookiecutter-python-library
...
project_name [Name of generated project]: test-project
project_description [Description of generated project]: Test Project
year [2018]:
author [FGtatsuro]:
email [Your Email address]
...
$ cd test-project
$ ls -1a
.
..
LICENSE
README.rst
```

You can overwrite default value of the field prompt asks with
~/.cookiecutterrc. It's better to overwrite 'author' field with your
Github username.

```bash
$ cat ~/.cookiecutterrc
default_context:
    author: "FGtatsuro"

$ cookiecutter gh:FGtatsuro/cookiecutter-python-library
...
author [FGtatsuro]:
...
```
