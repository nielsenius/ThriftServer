from django.db import models
import os

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

def create_hashtags(hashtags, item_id):    
    for ht in hashtags.split(' '):
        try:
            h = Hashtag.objects.get(hashtag=ht)
        except Hashtag.DoesNotExist:
            h = Hashtag(hashtag=ht)
            h.save()
        
        hi = HashtagItem(hashtag_id=h, item_id=Item.objects.get(id=item_id))
        hi.save()

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)

class Item(models.Model):
    user_id = models.ForeignKey(User, related_name='user')
    req_id = models.ForeignKey(User, related_name='request', null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=255)
    image1 = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    image2 = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    image3 = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    
class Hashtag(models.Model):
    hashtag = models.CharField(max_length=255)

class HashtagItem(models.Model):
    hashtag_id = models.ForeignKey(Hashtag)
    item_id = models.ForeignKey(Item)
