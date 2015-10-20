from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.apps import AppConfig
from models import *

@csrf_exempt
def create_user(request):
    try:
        u = User(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        u.save()
        return JsonResponse({'success': 'true', 'user_id': u.id})
    except:
        return JsonResponse({'success': 'false'})

@csrf_exempt
def get_user(request):
    try:
        u = User.objects.get(id=request.POST['user_id'])
        return JsonResponse({'success': 'true',
                             'first_name': u.first_name,
                             'last_name': u.last_name,
                             'phone': u.phone,
                             'email': u.email,
                             'image': u.image
                             })
    except:
        return JsonResponse({'success': 'false'})

@csrf_exempt
def create_item(request):
    try:
        i = Item(
            user_id=User.objects.get(id=request.POST['user_id']),
            name=request.POST['name'],
            description=request.POST['description'],
            status='Available'
        )
        i.save()
        
        create_hashtags(request.POST['hashtags'], i)
        
        return JsonResponse({'success': 'true'})
    except:
        return JsonResponse({'success': 'false'})

@csrf_exempt
def get_item(request):
    try:
        i = Item.objects.get(id=request.POST['item_id'])
        return JsonResponse({'success': 'true',
                             'user_id': i.user_id.id,
                             'name': i.name,
                             'description': i.description,
                             'status': i.status,
                             'image': i.image
                             })
    except:
        return JsonResponse({'success': 'false'})

@csrf_exempt
def get_items(request):
    try:
        i = Item.objects.all()[:10]
        return JsonResponse(serialize(i), safe=False)
    except:
        return JsonResponse({'success': 'false'})
    
@csrf_exempt
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

@csrf_exempt
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

@csrf_exempt
def login(request):
    try:
        u = User.objects.get(email=request.POST['email'], password=request.POST['password'])
        return JsonResponse({'success': 'true', 'user_id': u.id})
    except User.DoesNotExist:
        return JsonResponse({'success': 'false'})

@csrf_exempt
def search(request):
    try:
        hashtag = Hashtag.objects.get(hashtag=request.POST['keyword'])
        i = Item.objects.filter(hashtagitem__hashtag_id=hashtag.id)
        
        return JsonResponse(serialize(i))
    except User.DoesNotExist:
        return JsonResponse({'success': 'false'})

def populate(request):
    try:
        # create users
        u1 = User(
            first_name='Matt',
            last_name='Nielsen',
            phone='1234567890',
            email='matt@example.com',
            password='secret',
            image='matt'
        )
        u1.save()
        
        u2 = User(
            first_name='Roei',
            last_name='Curi-Hoory',
            phone='0987654321',
            email='roei@example.com',
            password='secret',
            image='roei'
        )
        u2.save()
        
        u3 = User(
            first_name='Kang Jun',
            last_name='Park',
            phone='5432167890',
            email='kang@example.com',
            password='secret',
            image='kang'
        )
        u3.save()
        
        # create items and hashtags
        i1 = Item(
            user_id=u1,
            name='Blue T-shirt',
            description='I am trying to give away this blue t-shirt.',
            status='Available',
            image='item1'
        )
        i1.save()
        
        create_hashtags('blue t-shirt fancy', i1)
        
        i2 = Item(
            user_id=u2,
            name='Red Sweater',
            description='I am trying to give away this red sweater.',
            status='Available',
            image='item2'
        )
        i2.save()
        
        create_hashtags('red sweater casual', i2)
        
        i3 = Item(
            user_id=u3,
            name='White Plates',
            description='I am trying to give away these white plates.',
            status='Available',
            image='item3'
        )
        i3.save()
        
        create_hashtags('white plates old', i3)
        
        i4 = Item(
            user_id=u1,
            name='Soft Blanket',
            description='I am trying to give away this wonderful blanket.',
            status='Available',
            image='item4'
        )
        i4.save()
        
        create_hashtags('soft blanket old', i4)
        
        i5 = Item(
            user_id=u2,
            name='Silverwear',
            description='I am trying to give away my old silverwear.',
            status='Available',
            image='item5'
        )
        i5.save()
        
        create_hashtags('silverwear kitchen old', i5)
        
        i6 = Item(
            user_id=u3,
            name='Blue Jeans',
            description='I am trying to give away these blue jeans.',
            status='Available',
            image='item6'
        )
        i6.save()
        
        create_hashtags('blue jeans casual', i5)
        
        return JsonResponse({'success': 'true'})
    except User.DoesNotExist:
        return JsonResponse({'success': 'false'})
