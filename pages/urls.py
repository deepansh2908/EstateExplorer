from django.urls import path
from . import views

urlpatterns = [
    #for the path '', we are calling the method index inside the views file
    path("", views.index, name="index"),
    path("about", views.about, name="about")
]
