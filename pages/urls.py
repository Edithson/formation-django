from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page_view),
    path("contact/", views.contact_page_view),
    path("info/", views.info_page_view)
]
