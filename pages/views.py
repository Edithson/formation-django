from django.shortcuts import render

from django.http import HttpResponse

from pages.models import ContactMessage
from .forms import ContactForms
from django.views.generic import TemplateView
from django.views.generic import ListView

# def home_page_view(request):
#     context = {
#         'nom' : 'John',
#         'age' : 21,
#         'taches' : ['métro', 'boulo', 'dodo'],
#         'genre' : 'M',
#     }
#     return render(request, "home.html", context)

class HomePageView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nom"] = 'John Doe'
        context["age"] = 21
        context["taches"] = ['métro', 'boulo', 'dodo']
        context["genre"] = 'F'
        return context
    
# def contact_page_view(request):
#     contacts = ContactMessage.objects.all()
#     return render(
#             request,
#             "contact/list.html",
#             context={'contacts' : contacts}
#         )
    
class MessageListView(ListView):
    model = ContactMessage
    template_name = 'contact/list.html'
    context_object_name = 'contacts'
    
    def get_queryset(self):
        return ContactMessage.objects.filter(is_treated=False)
    

def create_contact_page_view(request):
    success_msg = None
    if request.POST :
        form = ContactForms(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForms() #on vide le formulaire
            success_msg = "Votre demande a bien été envoyée"
    else :
        form = ContactForms()
    context = {
        'form': form,
        'success_msg': success_msg
    }
    return render(request, "contact/create.html", context)

def info_page_view(request):
    return HttpResponse("<h1>Page d'information</h1>\
        J'ai pas d'info pour vous ;)")