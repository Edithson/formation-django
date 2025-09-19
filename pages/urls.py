from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view()),
    # path("", views.home_page_view),
    path("contact/", views.MessageListView.as_view()),
    # path("contact/", views.contact_page_view),
    path("contact/create/", views.create_contact_page_view, name="create_contact"),
    path("info/", views.info_page_view)
]
