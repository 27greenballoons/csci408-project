from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import ContactMessage, Location
from .forms import ContactForm

# Create your views here. They are the html pages 
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def submitted(request):
    return render(request, "form-submitted.html")

def contact_us(request):
    submitted = False 

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
            return HttpResponseRedirect('form-submitted/?submitted=True')
    else:   
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, "contact-us.html", {'form': form, 'submitted': submitted})

def search(request):
    if request.method == 'POST':

        searched = request.POST['searched']
        locations = Location.objects.filter(city__icontains=searched) | Location.objects.filter(state__icontains=searched) | Location.objects.filter(owner__icontains=searched)

        return render(request, "search.html", {'searched': searched, 'locations': locations})
    else:
        return render(request, "search.html")