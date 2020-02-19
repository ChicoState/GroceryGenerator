from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home_view(request, *args, **kwargs):
	return render(request, "index.html", {})

def register_user(request):
	form = UserCreationForm;
	return render(request, "registration/register.html", {'form': form})