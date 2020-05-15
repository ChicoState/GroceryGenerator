"""views for site"""
from urllib.parse import quote
import requests
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from .models import user_lists, list_item

# Create your views here.
def home_view(request):
    """View for home page of site"""
    # pylint: disable=line-too-long
    url = "https://api.spoonacular.com/recipes/random?number=6&apiKey=caced314aa254583a7713a5e8e77f883"
    response = requests.request("GET", url)
    data = response.json()

    return render(request, "index.html", {'data':data})





@require_http_methods(["GET", "POST"])
def register_user(request):
    """view to regiser user"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    form = UserCreationForm()
    return render(request, "registration/register.html", {'form': form})

def search(request):
    """view to search"""
    term = request.POST['term']
    param = quote(term)
    # pylint: disable=line-too-long
    url = "https://api.spoonacular.com/recipes/search?apiKey=caced314aa254583a7713a5e8e77f883&query=" + param + "&number=5"
    response = requests.request("GET", url)
    data = response.json()
    context = {
        'data' : data
    }
    return render(request, "search.html", context)

def recipe_view(request, recipe_id):
    """view for individual recipe"""
    # pylint: disable=line-too-long
    url = "https://api.spoonacular.com/recipes/" + str(recipe_id) + "/information?apiKey=caced314aa254583a7713a5e8e77f883"
    lists = user_lists.objects.all().filter(list_owner=request.user)

    response = requests.request("GET", url)
    data = response.json()
    context = {
        'data': data,
        'lists': lists
    }

    return render(request, "recipe.html", context)



def favorites_view(request, recipe_id):
    """view to see favorites"""
    # pylint: disable=line-too-long
    url = "https://api.spoonacular.com/recipes/" + str(recipe_id) + "/information?apiKey=caced314aa254583a7713a5e8e77f883"
    response = requests.request("GET", url)
    data = response.json()
    return render(request, "favorites.html", {'data': data})

def similar(request, recipe_id):
    """view for similar recipes"""
    # pylint: disable=line-too-long
    url = "https://api.spoonacular.com/recipes/" + str(recipe_id) + "/similar?apiKey=caced314aa254583a7713a5e8e77f883&number=5"
    response = requests.request("GET", url)
    data = response.json()
    context = {
        'data' : data
    }
    return render(request, "similar.html", context)

def create_list(request):
    """view to create list"""
    if request.method == 'POST':
        name = request.POST['list_name']
        new_list = user_lists.objects.create(list_name=name, list_owner=request.user)
        new_list.save()
    return render(request, "create_list.html")

def view_lists(request):
    """view to see lists"""
    lists = user_lists.objects.all().filter(list_owner=request.user)
    print(lists)
    context = {
        'data' : lists
    }
    return render(request, "user_lists.html", context)

def list_view(request, list_id):
    """view to see individual list"""
    list_items = list_item.objects.all().filter(item_list=list_id)
    context = {
        'data' : list_items
    }
    return render(request, "list.html", context)

# pylint: disable=unused-argument
def add(request, recipe_id, item_id, list_id):
    """view add item to list"""
    cur_list = user_lists.objects.get(id=list_id)
    # pylint: disable=line-too-long
    url = "https://api.spoonacular.com/recipes/" + str(recipe_id) + "/information?apiKey=caced314aa254583a7713a5e8e77f883"
    response = requests.request("GET", url)
    data = response.json()
    for item in data["extendedIngredients"]:
        if item["id"] == item_id:
            amount = item["amount"]
            item_name = item["originalName"]
            unit = item["unit"]
    item = list_item.objects.create(item_name=item_name, item_amount=amount, item_unit=unit, item_list=cur_list)
    item.save()
    return HttpResponseRedirect('/lists/')
