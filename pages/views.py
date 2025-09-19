from django.shortcuts import render

from django.http import HttpResponse

from pages.models import ContactMessage

def home_page_view(request):
    context = {
        'nom' : 'John',
        'age' : 21,
        'taches' : ['métro', 'boulo', 'dodo'],
        'genre' : 'M',
    }
    return render(request, "home.html", context)

def contact_page_view(request):
    contacts = ContactMessage.objects.all()
    return render(
            request,
            "contact/list.html",
            context={'contacts' : contacts}
        )

def info_page_view(request):
    return HttpResponse("<h1>Page d'information</h1>\
        J'ai pas d'info pour vous ;)")