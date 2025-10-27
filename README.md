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

# Part 2: Static VS Dynamic Analysis

**Main Points:**
*1. Define static analysis. What is it? Why is it important in software security? Give one example of a tool used for static analysis.
2. Define dynamic analysis. What is it? How does it differ from static analysis? Give one example scenario where dynamic analysis is preferred.*

Static analysis and dynamic analysis can be compared to passive
reconnaissance and active reconnaissance. Static analysis is not as in depth as dynamic, but it
involves poking around a given file and gauging how to move forward while getting a basic
understanding of how it works. Usually, it is hard to detect when passive reconnaissance and static
analysis is occurring, as it is much less involved than its counterpart. Static analysis is essential for 
software security because it finds vulnerabilities and errors in code usually before having to run it or deploy it. 
It also requires less resources than dynamic analysis and can save money later on. **Ghidra** can be used as a 
static analysis tool as it can decompile and organize malicious code that someone may not want to run, and makes
it easier to reverse engineer code you have downloaded remotely. No one outside really knows when you're using static 
analysis due to it being hard to detect. Dynamic analysis is more like active reconnaissance, where it is more aggressive and more clear that 
something is being analyzed. In many cases, static analysis can be performed without running the file, 
while dynamic analysis does require the executable to be ran. Despite this, static analysis can be done on a file or system that is consistently running.
Dynamic analysis is usually preferred when the source code isn't avaliable or something is already running, or when something needs to be solved quickly. 
It could also be when something outside/foreign is occuring. 

# Part 3: Partner Reflection 

**1. What strategies did you use to analyze your partners executable?**
I started off by using strings, which turns executables into a readable format with 
each part of the assembly code's headers to get an idea of what each func was named 
and might do, I picked this up from NCL. After, I used ghidra and located the main func
and looked through the estimated C code to see the overall structure of the code and where
each other func was called. From there I looked at the other funcs and figured out what the code did. 

**2. What insights did you gain from analyzing the shared executable?**
I learned that the function was using two different shifting functions that took in different parameters
to perform a caeser cipher encryption/decryption process. 

**3. Describe one major challenge you encountered during this process.**
One major challenge I faced was making sense of the encryption and decryption functions, but after
taking a break and looking at it from a different angle later on, I figured out what the function
was meant to do by using context clues and other parts of the code. 

**4. How did your understanding of compiled binaries and disassembly evolve?**
My understanding of compiled binaries and disassembly evolved because I realized that decompiled functions in C code dont give
the full story of what is happening and doesn't always show the parameters of the function. I have to see what variables are 
used in it and assume from there to make educated guesses on what is happening. 

**5. If you could redo one part of your Ghidra work, what would you change and why?**
I probably wouldn't change much, I would still do everything how I did it, but I would probably
try to make use of Ghidra's other features like the flow chart and such to get a better understanding
of the code I examined. 

