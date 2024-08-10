from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import Loginform, UserCreationModel


def loginView(request):
    request.META['title'] = 'Login'
    form = Loginform()
    if request.method == 'POST':
        form = Loginform(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,
                                username=data['username'],
                                password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Siz muvaffaqiyatli ro'yxatdan o'tdiz")
                else:
                    return HttpResponse("Hisobingiz aktiv holatda emas")
            else:
                return HttpResponse("Login yoki parolda xatolik bor")

    context = {
        'form': form
    }
    return render(request, template_name='registration/login.html', context=context)


def logoutView(request):
    request.META['title'] = 'Logout'
    logout(request)
    return render(request, "registration/logged_out.html", {})


@login_required
def profileView(request):
    request.META['title'] = 'Profile'
    user = request.user
    context = {
        'user': user
    }
    return render(request, template_name='profile/profile_page.html', context=context)


def useCreationView(request):
    request.META['title'] = 'Registration'
    form = UserCreationModel()
    if request.method == 'POST':
        form = UserCreationModel(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data['password']
            )
            new_user.save()
            return render(request, 'registration/register_done.html', {'form': form})

    return render(request, template_name='registration/sign_up.html', context={
        'form': form
    })



