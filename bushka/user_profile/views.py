from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import csrf_protect
from . forms import UserUpdateForm, UserProfileUpdateForm


@login_required
def view_my_profile(request):
    return render(request, 'user_profile/view_profile.html')


def view_user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user_profile/view_profile.html', {'user': user})


@login_required
def edit_profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.user_profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, _('Vartotojo {} duomenys atnaujinti').format(request.user))
            return redirect('view_profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileUpdateForm(instance=request.user.user_profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'user_profile/edit_profile.html', context)


@csrf_protect
def register(request):
    if request.method == "POST":
        # duomenu surinkimas
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        # validuosim forma, tikrindami ar sutampa slaptažodžiai, ar egzistuoja vartotojas
        error = False
        if not password or password != password2:
            messages.error(request, _('Slaptažodžiai nesutampa arba neįvesti.'))
            error = True
        if not username or User.objects.filter(username=username).exists():
            messages.error(request, _('Vartotojas {} jau egzistuoja arba neįvestas.').format(username))
            error = True
        if not email or User.objects.filter(email=email).exists():
            messages.error(request, _('Vartotojas su el.praštu {} jau egzistuoja arba neįvestas.').format(email))
            error = True
        if error:
            return redirect('register')
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, _('Vartotojas {} užregistruotas sėkmingai. Galite prisijungti').format(username))
            return redirect('bushka_site:index')
    return render(request, 'user_profile/register.html')
