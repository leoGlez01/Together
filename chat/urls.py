from django.urls import path
from .views import user_login, home
from django.contrib.auth.views import LogoutView

urlpatterns =[
    path('home/',home, name='chat_home'),
    path('',user_login, name='login'),
    path("auth/logout/", LogoutView.as_view(), name="logout-user")
]