from django.db import models
import os

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class User(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    phone = models.CharField()
    email = models.CharField()
    password = models.CharField()
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)

class Item(models.Model):
    user_id = models.ForeignKey(User)
    req_id = models.ForeignKey(User)
    name = models.CharField()
    description = models.TextField()
    status = models.CharField()
    image1 = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    image2 = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    image3 = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    
class Hashtag(models.Model):
    hashtag = models.CharField()

class HashtagItem(models.Model):
    hashtag_id = models.ForeignKey(Hashtag)
    item_id = models.ForeignKey(Item)
