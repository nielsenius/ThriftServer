from django.http import HttpResponse, JsonResponse
from django.apps import AppConfig

def create_user(request):
    pass

def edit_user(request):
    pass

def create_item(request):
    i = Item(
        user_id=request.POST['user_id'],
        name=request.POST['name'],
        description=request.POST['description'],
        status='Available'
    )
    i.save()
    return HttpResponse("success")

def edit_item(request):
    pass

def request_item(request):
    pass

def give_item(request):
    pass

def create_hashtag(request):
    pass

def login(request):
    pass
