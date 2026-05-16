from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('log-in/', views.user_login, name='login'),
    path('log-out/', views.user_logout, name='logout'),
    path('profile/',views.user_profile,name='profile'),

    # login by Google
    path('google-auth/', views.send_google_auth, name='google-auth'),
    path('google/login/callback/', views.register_google_auth, name='google-callback'),

    # Forget Password
    path("forgot/", views.forgot_password, name="forgot"),
    path("verify/", views.verify_otp, name="verify_otp"),
    path("reset/", views.reset_password, name="reset_password"),
]