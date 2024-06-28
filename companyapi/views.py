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

def login_view(request):
    form = LoginPage(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace 'home' with your desired redirect URL
            else:
                form.add_error(None, "Invalid username or password")
    return render(request, 'myapp/login.html', {'form': form})
