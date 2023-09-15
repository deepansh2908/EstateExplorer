from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

def register(request):
    if request.method == 'POST':
        # get from values
        # since the request is POST
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check for password
        if password == password2:
            # check for duplicate username
            # for this we will need user model, which comes default with django
            if User.objects.filter(username=username).exists():
                # since we already have a user with that username
                messages.error(request, 'That username already exists')
                return redirect('register')
            else:
                # now check for email
                if User.objects.filter(email=email).exists():
                    # since we already have a user with that email
                    messages.error(request, 'That email already exists')
                    return redirect('register')
                else:
                    # now all username, password and email are unique
                    # create a new user in the User model
                    user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            # show error message
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')

def login(request):
    # if the request method is POST, we know it is a form submission
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # now authenticate this user with the following credentials
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # this means that the user is matched in the database
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
    'contacts': user_contacts
    }
    
    return render(request, 'accounts/dashboard.html', context)
