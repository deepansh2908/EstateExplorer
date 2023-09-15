from django.shortcuts import render
from django.http import HttpResponse
# even though this is the pages, we ca still import any model from any app
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices

# Create your views here.

#this method will be called when '' url is hit
def index(request):
    #but obviously we don't want to put in the entire html code inside here. So what we do instead is that we render a template from the template folder
    #return HttpResponse("<h1>Welcome to the Index page</h1>")

    #so instead of returning an HTTP response, we will now render a template. Since we already added the templates folder in the settings.py file, django automatically knows where to look for them. So we can just specify the path as pages/index.html instead of templates/pages/index.html

    # order by is a django thing, [:3] limits the number of listings to 3
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)[:3]

    context = {
        'listings': listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
    }

    return render(request, 'pages/index.html', context)

def about(request):
    # get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # get all those realtors that are mvp
    mvp_realtors = Realtor.objects.all().filter(is_mvp = True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors,
    }

    return render(request, 'pages/about.html', context)
