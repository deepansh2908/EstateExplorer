from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from listings.choices import price_choices, bedroom_choices, state_choices

def index(request):
    # this fetches all the data in Listing model- sorted by date ie latest one is shown first- also show only if listing is published
    listings = Listing.objects.order_by('list_date').filter(is_published=True)

    # Pagination - we want to display only 3 listings per page
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    # this is basically a dictionary that we are passing
    context = {
        'listings': paged_listings,
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    # this gets the object if it exists or throws a 404 error otherwise
    # pk is the primary key
    listing = get_object_or_404(Listing, pk = listing_id)
    
    context = {
        'listing': listing,
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # if request query has any keywords in it
    if 'keywords'in request.GET:
        keywords = request.GET['keywords']
        # if keywords is not empty
        if keywords:
            # now we filter the listings such that the keywords are present in any description paragraph
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # if request query has any city in it
    if 'city'in request.GET:
        city = request.GET['city']
        # if keywords is not empty
        if city:
            # now we filter the listings such that the city field exactly matches the query city
            # note that ixact is case insensitive
            queryset_list = queryset_list.filter(city__iexact=city)

    # if request query has any state in it
    if 'state'in request.GET:
        state = request.GET['state']
        # if state is not empty
        if state:
            # now we filter the listings such that the state field exactly matches the query state
            # note that ixact is case insensitive
            queryset_list = queryset_list.filter(state__iexact=state)
    
    # if request query has any bedrooms in it
    if 'bedrooms'in request.GET:
        bedrooms = request.GET['bedrooms']
        # if bedrooms is not empty
        if bedrooms:
            # lte stands for less than or equal to
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # if request query has any price in it
    if 'price'in request.GET:
        price = request.GET['price']
        # if price is not empty
        if price:
            # lte stands for less than or equal to
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
