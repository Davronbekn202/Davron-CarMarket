from django.contrib.auth.decorators import login_required
import random
import requests
from .forms import RegisterForm
from django.conf import settings
from .utils import send_reset_password_email
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import get_user_model


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('accounts:login')

    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form, })


def user_login(request):
    # POST (login attempt)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('carapp:base')

        return render(request, 'account/login.html', {
            'error': 'Username yoki Password xato'})

    return render(request, 'accounts/login.html')


def user_logout(request):
    logout(request)
    return redirect('accounts:login')


@login_required
def user_profile(request):
    info = request.user
    return render(request, 'accounts/profile.html', {'info': info})

#OAuth
User = get_user_model()
def send_google_auth(request):
    auth_url = (
        f"{settings.GOOGLE_AUTH_URL}"
        f"?client_id={settings.GOOGLE_CLIENT_ID}"
        f"&redirect_uri={settings.GOOGLE_REDIRECT_URI}"
        f"&response_type=code"
        f"&scope=openid email profile"
    )
    return redirect(auth_url)


def register_google_auth(request):
    code = request.GET.get('code')
    if not code:
        return JsonResponse({'error': 'Code yo‘q'}, status=400)

    token_data = {
        "code": code,
        "client_id": settings.GOOGLE_CLIENT_ID,
        "client_secret": settings.GOOGLE_CLIENT_SECRET,
        "redirect_uri": settings.GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }

    token_response = requests.post(settings.GOOGLE_TOKEN_URL, data=token_data)
    access_token = token_response.json().get("access_token")

    if not access_token:
        return JsonResponse({"error": "Access token yo‘q"}, status=400)

    user_info_response = requests.get(
        settings.GOOGLE_USER_INFO_URL,
        headers={"Authorization": f"Bearer {access_token}"}
    )

    email = user_info_response.json().get("email")

    if not email:
        return JsonResponse({'error': 'Email topilmadi'}, status=400)


    user, created = User.objects.get_or_create(
        email=email,
        defaults={
            "username": email,
            "phone_number": ""  # fallback
        }
    )

    login(request, user)
    return redirect('carapp:base')


# Forget Password
def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        code = random.randint(100000, 999999)

        request.session['reset_email'] = email
        request.session['reset_code'] = str(code)

        send_reset_password_email(email, code)
        return redirect('accounts:verify_otp')

    return render(request, "accounts/forgot.html")


def verify_otp(request):
    if request.method == "POST":
        user_code = request.POST.get("code")
        real_code = request.session.get('reset_code')

        if user_code == real_code:
            return redirect('accounts:reset_password')
        else:
            return render(request, "account/verify.html", {"error": "Wrong OTP"})
    return render(request, "accounts/verify.html")


def reset_password(request):
    if request.method == "POST":
        password = request.POST.get("password")
        email = request.session.get("reset_email")

        user = User.objects.get(email=email)
        user.set_password(password)
        user.save()

        return redirect('accounts:login')
    return render(request, "accounts/reset.html")
