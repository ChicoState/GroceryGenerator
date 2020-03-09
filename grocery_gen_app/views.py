from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
import requests

# Create your views here.
def home_view(request, *args, **kwargs):
	
	url = "https://api.spoonacular.com/recipes/random?number=6&apiKey=caced314aa254583a7713a5e8e77f883"
	response = requests.request("GET", url)
	data = response.json()

	return render(request, "index.html", {'data':data})


def recipe_view(request, recipe_id):
	
	print ("In recipe view for recipe_id", recipe_id)
	
	# return render(request, "recipe.html/", {'recipe_id': recipe_id})
	url = "https://api.spoonacular.com/recipes/" + str(recipe_id) + "/information?apiKey=caced314aa254583a7713a5e8e77f883"
	
	response = requests.request("GET", url)
	data = response.json()
	# print ("data for recipe")
	# print (data)

	return render(request, "recipe.html", {'data':data})


@require_http_methods(["GET", "POST"])
def register_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('/')
	form = UserCreationForm();
	return render(request, "registration/register.html", {'form': form})