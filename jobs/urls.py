from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # User
    path("user_login/", views.user_login, name="user_login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.Logout, name="logout"),


    # Company
    path("company_signup/", views.company_signup, name="company_signup"),
    path("company_login/", views.company_login, name="company_login"),


    # admin
    path("admin_login/", views.admin_login, name="admin_login"),
]