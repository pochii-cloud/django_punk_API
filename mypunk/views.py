from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView, DeleteView

from mypunk.forms import Registerform
from mypunk.models import Favourites


def base(request):
    fav = Favourites()
    if request.POST:
        name = request.POST.get('name')
        image = request.POST.get('image')
        description = request.POST.get('description')
        if Favourites.objects.filter(name=name).exists():
            return HttpResponse("item in you favourites")
        fav.name = name
        fav.user = request.user
        fav.image = image
        fav.description = description
        fav.save()
        return redirect('favourite')
    return render(request, 'base.html')


class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = Registerform
    success_url = reverse_lazy('loginpage')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base')
        else:
            messages.info(request, 'username OR password incorrect')
    return render(request, 'login.html')


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('loginpage')


@login_required
def favourite(request):
    fav = Favourites.objects.filter(user=request.user)
    return render(request, 'favourites.html', {'fav': fav})


def delete(request, fav_id):
    fav = Favourites.objects.get(pk=fav_id)
    fav.delete()
    return redirect('favourite')
