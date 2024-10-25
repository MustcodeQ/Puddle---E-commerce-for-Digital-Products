# from django.shortcuts import render
# # Create your views here.

# from core.models import Category, Item
# def index(request):
#     #Purpose: To display the latest 6
#     #items that are still available 
#     # (not sold yet). This makes sure the 
#     # user only sees relevant, unsold items.
#     items = Item.objects.filter(is_sold = False)[0:6]
#     #Purpose: To load all categories that items may
#     #  fall under, enabling users to
#     #  filter or explore items by category 
#     # on the homepage.

#     categories = Category.objects.all()
#     return render(request, 'core/index.html', {
#         'categories' : categories,
#         'items' : items,
#     })
#   # render(request, 'template-name, context != none)

# def contact(request):
#     return render(request, 'core/contact.html')
from django.shortcuts import render
from core.models import Category, Item
from .forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Q  # This helps with search queries

from django.contrib.auth import authenticate, login


def index(request):
    # Purpose: To display the latest 8
    # items that are still available 
    # (not sold yet).
    items = Item.objects.filter(is_sold=False)[0:6]  # Change from 6 to 8

    # Purpose: To load all categories that items may
    # fall under, enabling users to
    # filter or explore items by category 
    # on the homepage.
    categories = Category.objects.all()
    
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')
#-dashborad-page hyper
#@loginrequired
def dashboard(request):
    return render(request, 'core/dashboard.html')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})
      
# def custom_login_view(request):
#     if request.method == 'POST':
#         form = CustomLoginForm(request.POST)
#         if (form.is_valid()):
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username = username, password = password)
#             if (user is not None):
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 messages.error(request, 'Invalid username or password')
#     else:
#         form = CustomLoginForm()
#     return render(request, 'core/login.html', {'form':form})

# def test_view(request):
#     return render(request, 'test_template.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Correctly calls login with both arguments
                return redirect('home')  # Redirect to the home page or any other page
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form})

def settings(request):
    return render(request, 'core/settings.html')

# def product_list(request):
#     query = request.GET.get('q')  # Getting the search query from the request
#     if query:
#         # Use the Q object to search multiple fields
#         items = Item.objects.filter(
#             Q(name__icontains=query) | Q(description__icontains=query)
#         )
#     else:
#         items = Item.objects.all()  # Get all items if there's no search query

#     return render(request, 'core/product_list.html', {'items': items})




def items_view(request):
    query = request.GET.get('q')  # Get the search query from the URL
    if query:
        items = Item.objects.filter(name__icontains=query, is_sold=False)  # Filter items based on the search query
    else:
        items = Item.objects.filter(is_sold=False)  # Get all unsold items

    return render(request, 'core/items.html', {'items': items})
# def product_list(request):
#     query = request.GET.get('q')
#     category_filter = request.GET.get('category')
#     items = Item.objects.all()

#     if query:
#         items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

#     if category_filter:
#         items = items.filter(category=category_filter)

#     categories = Category.objects.all()  # Load all categories for filtering

#     return render(request, 'core/product_list.html', {
#         'items': items,
#         'categories': categories,
#     })
# def categories(request):
#     return render(request, 'core/categories.html')