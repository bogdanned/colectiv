from django.shortcuts import render

# Create your views here.

def IndexView(request):


    context = {

    }

    return render(request, "index.html", context)



def PricingView(request):


    context = {

    }

    if request.method=="POST":
        return render(request, "pricing.html", context)


    return render(request, "pricing.html", context)
