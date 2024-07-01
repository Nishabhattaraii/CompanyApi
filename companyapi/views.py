from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from api.forms import LoginPage # type: ignore

def home_page(request):
    print("home page requested")
    friends =[
        'ankita'
        'Rukmini'
        'Anarkali'
    ]
    return JsonResponse(friends,safe=False)


def login_page(request):
    return render(request, 'login.html')
