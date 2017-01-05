from django.shortcuts import render
from .forms import *

# Create your views here.


def IndexView(request):


    context = {

    }

    return render(request, "index.html", context)



def PricingView(request):


    context = {

    }

    if request.method=="POST":
        print(request.POST)
        form = indexForm(request.POST)
        if form.is_valid():
            origin = form.cleaned_data['origin']
            destiny = form.cleaned_data['destiny']
            context = {
                "origin": origin,
                "destiny": destiny,
            }

        else:
            context = {
                "origin": False,
                "destiny": False,
            }

        return render(request, "pricing.html", context)

    return render(request, "pricing.html", context)
