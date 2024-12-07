from django.urls import path

from . import views

urlpatterns = [
    path("", views.RsvpRequestView.as_view(), name="index"),
    path("<slug>", views.GuestListFormView.as_view(), name="rsvp")
]
