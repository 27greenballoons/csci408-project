from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name=""), # this is the home page 
    path("about/", views.about, name="about"), # this is the about page
    path("contact-us/", views.contact_us, name ="contact-us"), # this is the contact us page
    path("contact-us/form-submitted/", views.submitted, name="form-submitted"), # this is the form submitted page
    path("search/", views.search, name="search"), # this is the search page
]