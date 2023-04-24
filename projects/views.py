from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .form import CustomUserCreationForm, ListPropertyForm
from .models import ListProperty, Profile, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required

def IndexPage(request):
    
    context ={}

    context["dataset"] = ListProperty.objects.all()
    return render(request, 'projects/index.html', context)

def ProductDescription(request, pk):
    
    productObj = ListProperty.objects.get(id=pk)
    context = {'productObj':productObj}
    
    return render(request, 'projects/product-description.html', context)

def LoginPage(request):
    
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'ERROR')
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'ERROR')
    
    return render(request, 'projects/login.html')

def RegisterPage(request):
    
    form = CustomUserCreationForm()
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'ERROR')
    
    
    context = {'form': form}
    
    return render(request, 'projects/register.html', context)

def logoutUser(request):
    logout(request)
    messages.info(request, 'User Was Logged Out')
    return redirect('index')

@login_required(login_url="login")
def ListPropertyFormView(request):
    
    profile = request.user.profile
    
    form = ListPropertyForm()
    
    if request.method == 'POST':
        form = ListPropertyForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('index')
        else:
            messages.error(request, 'ERROR')
    
    context = {'form': form, 'profile': profile}
    return render(request, 'projects/list_property_form.html', context)


def FilterPage(request, category_id):
    
  
    category = Category.objects.get(id=category_id)
    products = ListProperty.objects.filter(category=category)
    queryset = products.order_by('id')

    # Create the paginator
    paginator = Paginator(queryset, 2)

    # Get the current page
    page = request.GET.get('page')

    # Get the page object
    page_obj = paginator.get_page(page)
    categories = Category.objects.all()
    context = {'products': products, 'categories': categories, 'page_obj': page_obj}
    return render(request, 'projects/filter.html', context)

@login_required(login_url="login")
def UserProfile(request):
    
    profile = request.user.profile
    
    products = profile.listproperty_set.all()
    
    context = {'profile':profile, 'products':products}
    return render(request, 'projects/user-profile.html', context)

@login_required(login_url="login")
def UserProperty(request):
    
    profile = request.user.profile
    
    products = profile.listproperty_set.all()
    
    context = {'profile':profile, 'products':products}
    return render(request, 'projects/user-property.html', context)