from django.shortcuts import render

# Create your views here.

def IndexView(request):


    context = {

    }

    return render(request, "index.html", context)
