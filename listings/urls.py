from django.urls import path
from . import views

urlpatterns = [
    #for the path '', we are calling the method index inside the views file
    path("", views.index, name="listings"),
    #here we are adding a parameter called listing_id to take us to a specific listing type. The url in this case will be like this: 'listing/12'
    path("<int:listing_id>", views.listing, name="listing"),
    path("search", views.search, name="search")
]
