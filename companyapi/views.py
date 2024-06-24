from django.http import HttpResponse, JsonResponse # type: ignore

def home_page(request):
    print("home page requested")
    friends =[
        'ankita'
        'Rukmini'
        'Anarkali'
    ]
    return JsonResponse(friends,safe=False)
