from django.contrib import admin
from .models import Contact

# Register your models here - so that you can see them in the admin area

class ContactAdmin(admin.ModelAdmin):
    # this is the number of columns in the admin table
    list_display = ("id", "name", "listing", "email", "contact_date")
    list_display_links = ("id", "name")
    search_fields = ("name", "email", "listing")
    list_per_page = 25


# name of the model is Contact and name of the class is ContactAdmin
admin.site.register(Contact, ContactAdmin)
