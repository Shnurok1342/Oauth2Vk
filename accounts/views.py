from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import  logout as auth_logout
from django.contrib.auth.decorators import login_required
import requests


def login(request):
    return render(request, 'accounts/login.html')

@login_required(login_url='/login/')
def home(request):
    social_user = request.user.social_auth.filter(provider = 'vk-oauth2').first()
    if social_user:
        user_request_params = {
        'v': '5.92',
        'access_token': social_user.extra_data['access_token'],
        'count': '5',
        'fields': ['photo_50']
        }
        response = requests.get('https://api.vk.com/method/friends.get', params = user_request_params).json()
        return render(request, 'accounts/home.html', locals())
    else:
        auth_logout(request)
        return redirect('/')

def logout(request):
    auth_logout(request)
    return redirect('/')
