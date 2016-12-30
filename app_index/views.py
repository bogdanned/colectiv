from django.shortcuts import render

# Create your views here.

def IndexView(request):


    context = {

    }

    return render(request, "base.html", context)
