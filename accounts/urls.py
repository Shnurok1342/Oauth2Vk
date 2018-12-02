from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('login/', views.login, name = "login"),
    path('logout/', views.logout, name = "logout"),
    path('', include('social_django.urls', namespace='social')),
    path('', views.home, name = "home"),
]
