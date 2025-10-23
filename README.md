# CSCI 408 Project 

This is my first attempt at a minimal Django app. It is a fake bank website that allows you to
send in a contact form into a DB and look up different locations on the search bar. Kind of a
more informal readme mostly to help with my own learning.

# Project Structure
```
MIDTERM/
├── .venv/                    # Virtual environment (ignored in .gitignore)
├── .gitignore                # Git ignore file
├── db.sqlite3                # SQLite database
├── manage.py                 # Django project management script
│
├── project/                  # Main Django project package
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py           # Global Django settings
│   ├── urls.py               # Root URL configurations
│   └── wsgi.py
│
└── app/                      # Application package
    ├── __init__.py
    ├── admin.py              # Model admin registrations
    ├── apps.py               # App configuration
    ├── forms.py              # Django forms
    ├── models.py             # Database models
    ├── tests.py              # Unit tests
    ├── urls.py               # App URL routes
    ├── views.py              # View functions / page controllers
    │
    ├── migrations/           # Auto-generated DB migrations
    │   └── __init__.py
    │
    ├── static/               # Static assets (CSS, images, JS)
    │   └── bank.jpg
    │
    └── templates/            # HTML templates
        ├── base.html
        ├── home.html
        ├── about.html
        ├── contact-us.html
        ├── form-submitted.html
        └── search.html
```

# Important Files 
Many of these files are standard for Django packages, but I will cover the files that
are most relevant to the project/different from the standard Django configs. 

* **project/settings** - Basic settings for the Django project. I had to add 'app' under "INSTALLED
APPS" for everything in apps to show up, but that was the only thing changed. 

* **project/urls.py** - This python script handles the routing of the entire Django project 
between different apps. In this case, since there is only one app, then there is only one
line for routing all the urls featured in app/urls.py, and then routing everything contained in
the admin dashboard. 

* **app/admin.py** - Contains models from *models.py* that appear on the admin dashboard. If you go
to the link (usually localhost:8000) and go to /admin, then you'll see a gui for the admin portal
where you can add more of different models from there. This is how I made the locations table and
added data to it.

* **app/forms.py** - This was used to assist with the creation of the contact form. It takes the
model "ContactMessage" and turns it into a format where it can be generated and used in an HTML file.
It also handles security and database integration, and makes the code cleaner in the long run. 

* **app/models.py** - This file creates different ways to store data in the local db through different models. For example,
I created a model named "Locations" which has a city, state, and location; and you can create and store values using this
model to correspond and send to a table in the db.

* **app/urls.py** - This file is where I defined all the routes from home that come from this specific app. Every route except for
the admin one is in here. So after "" (home), the routes from here would be defined.

* **templates/** - This folder contains all of the HTML templates for the frontend of the website. **base.html** is the jinga template that
every other HTML file is built off of.

* **templates/search.html** - There is a XSS vulnerability in here.

```
{% extends "base.html" %} {% block title %} Home {% endblock %}
{% load static %}

{% block content %}
{% if searched %}
    <!-- VULNERABILITY: The use of {{ searched|safe }} is unsafe and can lead to XSS attacks. -->
    <h1 style="text-align: center;">Your Search Results for {{ searched|safe }}</h1>

    {% if locations %}
        <ul style="text-align: center;">
        {% for item in locations %}
            <li>{{ item }}</li>
        {% endfor %}
        </ul>

    {% else %}
        <h1>No results found.</p>
    {% endif %}

{% else %}
    <p style="text-align: center;">Please enter a search term.</p>
{% endif %}

{% endblock %}
```

The line where the query from the navbar is taken in and searched: ``` <h1 style="text-align: center;">Your Search Results for {{ searched|safe }}</h1> ```
does not sanitize any inputs from the user because of the "| safe" tag, which considers every input as benign without double checking. This is very
dangerous to have in your code because it leaves it vulnerable to not only XSS, but also SQL injections! 

A better example of how to handle these situations is seen in the contact form page, **templates/contact-us.html**, where all inputs are sanitized 
by not including the | safe tag when placing data in the variables that insert stuff into the db (its implemented in a form differently, uses the form
structure to make the HTML code easier and not have to worry about sanitizing inputs and such). 

# Static VS Dynamic Analysis


