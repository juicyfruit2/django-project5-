from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login

# Create your views here.
def user_login(request):
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    
    if user is None:
        return HttpResponseRedirect(reverse('user_auth:login'))
    
    else:
        login(request, user)
        return HttpResponseRedirect(reverse('user_auth:show_user'))
