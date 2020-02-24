from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

# Create your views here.
def home_view(request, *args, **kwargs):
	return render(request, "index.html", {})

def register_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		print("HERE")
		if form.is_valid():
			print("SAVING")
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('/')
	form = UserCreationForm;
	return render(request, "registration/register.html", {'form': form})