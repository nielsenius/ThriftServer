from django.http import HttpResponse, JsonResponse
from django.apps import AppConfig

def create_user(request):
    u = User(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        phone=request.POST['phone'],
        email=request.POST['email'],
        password=request.POST['password'],
    )
    u.save()
    return HttpResponse('success')

def edit_user(request):
    return HttpResponse('failure')

def create_item(request):
    i = Item(
        user_id=request.POST['user_id'],
        name=request.POST['name'],
        description=request.POST['description'],
        status='Available'
    )
    i.save()
    return HttpResponse('success')

def edit_item(request):
    return HttpResponse('failure')

def request_item(request):    
    try:
        i = Item.objects.get(id=request.POST['item_id'])
        u = User.objects.get(id=request.POST['user_id'])
        
        if i.req_id == None:
            i.req_id = u.id
            i.status = 'Requested'
            i.save()
            return HttpResponse('success')
        else:
            return HttpResponse('failure')
    except Item.DoesNotExist:
        return HttpResponse('failure')

def give_item(request):
    try:
        i = Item.objects.get(id=request.POST['item_id'])
        
        if i.status == 'Requested':
            i.status = 'Given'
            i.save()
            return HttpResponse('success')
        else:
            return HttpResponse('failure')
    except Item.DoesNotExist:
        return HttpResponse('failure')

def create_hashtag(request):
    i_id = request.POST['item_id']
    
    try:
        h = Hashtag.objects.get(hashtag=request.POST['hashtag'])
    except Hashtag.DoesNotExist:
        h = Hashtag(hashtag=request.POST['hashtag'])
        h.save()
    
    hi = HashtagItem(hashtag_id=h.id, item_id=i_id)
    hi.save()
    HttpResponse('success')
        

def login(request):
    if User.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
        return HttpResponse('success')
    else:
        return HttpResponse('failure')
