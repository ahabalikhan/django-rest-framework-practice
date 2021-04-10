# django-rest-framework-practice

A practice of building REST Api using Django Rest Framework

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/ahabalikhan/django-rest-framework-practice.git
$ cd django-rest-framework-practice
```

Create a virtual environment to install dependencies in and activate it:
If you have virtualenvwrapper installed then you can simply make a virtual env and install all the required modules as stated in requirements.txt.
Make a virtual env by using following commands in the terminal
```sh
$ pip install virtualenvwrapper
$ mkvirtualenv venv
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenvwrapper`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd <project>
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/product/0`.

## Walkthrough

Send GET request to `http://127.0.0.1:8000/product/0`
Response will be all the products with their details delivered in json format

Send GET request to `http://127.0.0.1:8000/product/1`
Response will contain a product having id = 1, with its details.

Send POST request to `http://127.0.0.1:8000/product/create`
With json containing all the required fields to register a product, and it will return Http 200.

## Webhook

This project is also hosted at `https://myproject-justforpractice.herokuapp.com/`

You can send GET request to it, for example:
`https://myproject-justforpractice.herokuapp.com/product/1`
Copy the above url into your browser and Hit Enter


