from django.shortcuts import render, reverse, redirect
from .forms import *
from django.http import JsonResponse



def IndexView(request):


    context = {

    }

    return render(request, "index.html", context)


def ProfileView(request):


    context = {

    }

    return render(request, "profile.html", context)




def PricingCommuteView(request):

    form_route = RouteForm()

    context = {
        'form_route': form_route,
    }

    if request.method=="POST":
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

        return render(request, "pricing_commute.html", context)

    return render(request, "pricing_commute.html", context)


def PricingTaxiView(request):

    form_route = RouteForm()

    context = {
        'form_route': form_route,
    }

    if request.method=="POST":
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

        return render(request, "pricing_taxi.html", context)

    return render(request, "pricing_taxi.html", context)



def RouteView(request):
    form = RouteForm()
    context = {
        'form': form,
    }
    success = False
    if request.method == "POST":
        form = RouteForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            success = True
            try:
                route = form.save()
                request.session['route_id'] = route.id
                return JsonResponse({'route_id': route.id})
            except:
                pass

        return JsonResponse({'route_id': None})
    return redirect(reverse('index'))


def EmailProfileView(request):

    context = {

    }


    return render(request, "profile.html", context)


def getEmail(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        print()
        if form.is_valid():
            email = form.save(commit=True)
            print(email)
            route_id = request.session.__getitem__('route_id')
            route = Route.objects.get(pk=route_id)
            route.email = email
            route.save()
            print(route.email)
            return redirect(reverse('email-profile'))
