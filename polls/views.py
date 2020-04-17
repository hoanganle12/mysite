from django.http import HttpResponseRedirect
from .forms import RegistrationForm
from django.shortcuts import render

# Create your views here.


def index(request):
    name1 = "Movie Library"
    context = {"name": name1}
    return render(request, "polls/index.html", context)


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, "polls/register.html", {'form': form})
