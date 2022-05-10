<p align="center">
  <img alt="Chromatic Logo" src="img/chromatic_logo.png" width="400">
</p>

# chromatic

## Overview

![](https://img.shields.io/badge/Tests-Passing-greenyellow)
![](https://img.shields.io/badge/Coverage-82%25-aquamarine)

*chromatic* is a public image repository website. It allows users to authenticate themselves and upload images. *chromatic* also performs facial detection on uploaded images. This was a part of the **Shopify Fall 2022 Data Engineering Intern Challenge.**

This challenge was completed by building a stand-alone **Django** application called **Chromatic**. Try out the demo [here](https://devpostman404.pythonanywhere.com/).

![Homepage](img/homepage_unauthenticated.png)

In order to upload images of your own, click *Register* on the top left to register for an account, then login to your created account. Once you're logged in, you should see the *Upload Image +* option on the top left, which will lead you to the image uploading page.

![Upload Image](img/upload.png)

Clicking on an individual image will launch a modal that displays the picture, which includes a facial recognition feature built using **OpenCV** and Haar Cascade Classifiers.

![Movie Theatre](img/movie_theatre.png)

## Try it out locally

The instructions below are for using the Chromatic app on a local machine.

### Clone the repository

```bash
git clone https://github.com/alvii147/chromatic.git
```

### Install dependencies

```bash
pip3 install -r requirements.txt
```

### Set up environment variables

```bash
export DJANGO_ENV_MODE="DEV"
export SECRET_KEY="qwertyuiopasdfghjklzxcvbnm1234567890"
```

### Run migrations

```bash
cd chromatic
python3 manage.py migrate
```

### Run the server

```bash
python3 manage.py runserver
```

The server should then be up at `http://localhost:8000`.

## Testing

Currently Chromatic is run through rigorous testing, including unit tests for Django URLs, views, as well as OpenCV functions, under Python 3.7, 3.8, and 3.9 environments. [This Github Actions CI script](.github/workflows/django.yml) is used for automated testing on Github. Currently **100% of tests are passing**, while **test coverage is 82%** (coverage is not perfect due to a few default Django files that are not covered in tests).

### Running tests and coverage

```bash
coverage run --source='.' manage.py test -v 2
coverage report
```

### Coverage Report

```
Name                                       Stmts   Miss  Cover
--------------------------------------------------------------
chromatic/__init__.py                          0      0   100%
chromatic/asgi.py                              4      4     0%
chromatic/settings/__init__.py                 7      3    57%
chromatic/settings/base.py                    24      0   100%
chromatic/settings/dev.py                      3      0   100%
chromatic/settings/prod.py                     3      3     0%
chromatic/urls.py                              6      0   100%
chromatic/wsgi.py                              4      4     0%
chromatic_app/__init__.py                      0      0   100%
chromatic_app/admin.py                         8      0   100%
chromatic_app/apps.py                          4      0   100%
chromatic_app/forms.py                         8      0   100%
chromatic_app/migrations/0001_initial.py       7      0   100%
chromatic_app/migrations/__init__.py           0      0   100%
chromatic_app/models.py                       19      2    89%
chromatic_app/tests/__init__.py                0      0   100%
chromatic_app/tests/test_urls.py              19      0   100%
chromatic_app/tests/test_utils.py             16      1    94%
chromatic_app/tests/test_views.py             20      0   100%
chromatic_app/urls.py                          4      0   100%
chromatic_app/utils.py                        18      3    83%
chromatic_app/views.py                        36     18    50%
manage.py                                     12      2    83%
--------------------------------------------------------------
TOTAL                                        222     40    82%
```

