from django.db import models
from django.core import serializers
import json

# helper functions

def create_hashtags(hashtags, item):    
    for ht in hashtags.split(' '):
        try:
            h = Hashtag.objects.get(hashtag=ht)
        except Hashtag.DoesNotExist:
            h = Hashtag(hashtag=ht)
            h.save()
        
        hi = HashtagItem(hashtag_id=h, item_id=item)
        hi.save()

def serialize(objects):
    a = []
    for o in objects:
        obj_serial = serializers.serialize('json', [o])
        obj_dict = json.loads(obj_serial)[0]['fields']
        obj_dict['item_id'] = o.id
        a.append(obj_dict)
    return a

# database definition

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    image = models.CharField(max_length=255)

class Item(models.Model):
    user_id = models.ForeignKey(User, related_name='user')
    req_id = models.ForeignKey(User, related_name='request', null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    
class Hashtag(models.Model):
    hashtag = models.CharField(max_length=255)

class HashtagItem(models.Model):
    hashtag_id = models.ForeignKey(Hashtag)
    item_id = models.ForeignKey(Item)
