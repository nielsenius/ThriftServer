from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.apps import AppConfig

def create_user(request):
    try:
        u = User(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            password=request.POST['password'],
        )
        u.save()
        return JsonResponse({'success': 'true', 'user_id': u.id})
    except:
        return JsonResponse({'success': 'false'})

def get_user(request):
    try:
        u = User.objects.get(id=request.POST['user_id'])
        return JsonResponse({'success': 'true',
                             'first_name': u.first_name,
                             'last_name': u.last_name,
                             'phone': u.phone,
                             'email': u.email
                             })
    except:
        return JsonResponse({'success': 'false'})

def create_item(request):
    try:
        i = Item(
            user_id=request.POST['user_id'],
            name=request.POST['name'],
            description=request.POST['description'],
            status='Available'
        )
        i.save()
        
        create_hashtags(request.POST['hashtags'])
        
        return JsonResponse({'success': 'true'})
    except:
        return JsonResponse({'success': 'false'})

def get_item(request):
    try:
        i = Item.objects.get(id=request.POST['item_id'])
        return JsonResponse({'success': 'true',
                             'user_id': i.user_id,
                             'name': i.name,
                             'description': i.description,
                             'status': i.status
                             })
    except:
        return JsonResponse({'success': 'false'})

def get_items(request):
    try:
        i = Items.objects.all()[:10]
        return JsonResponse(serializers.serialize('json', i))
    except:
        return JsonResponse({'success': 'false'})
    

def request_item(request):    
    try:
        i = Item.objects.get(id=request.POST['item_id'])
        u = User.objects.get(id=request.POST['user_id'])
        
        if i.req_id == None:
            i.req_id = u.id
            i.status = 'Requested'
            i.save()
            return JsonResponse({'success': 'true'})
        else:
            return JsonResponse({'success': 'false'})
    except Item.DoesNotExist:
        return JsonResponse({'success': 'false'})

def give_item(request):
    try:
        i = Item.objects.get(id=request.POST['item_id'])
        
        if i.status == 'Requested':
            i.status = 'Given'
            i.save()
            return JsonResponse({'success': 'true'})
        else:
            return JsonResponse({'success': 'false'})
    except Item.DoesNotExist:
        return JsonResponse({'success': 'false'})

def login(request):
    try:
        u = User.objects.get(email=request.POST['email'], password=request.POST['password'])
        return JsonResponse({'success': 'true', 'user_id': u.id})
    except User.DoesNotExist:
        return JsonResponse({'success': 'false'})

def search(request):
    try:
        hashtag = Hashtag.objects.get(hashtag=request.POST['keyword'])
        i = Item.objects.filter(hashtagitem__hashtag_id=hashtag.id)
        
        return JsonResponse(serializers.serialize('json', i))
    except User.DoesNotExist:
        return JsonResponse({'success': 'false'})
