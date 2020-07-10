from django.db import models
from django.db.models import signals
from datetime import datetime
from elasticsearch import Elasticsearch
from django.core import serializers
import inspect
import json
# Create your models here.

def create_animal(sender, instance, created, **kwargs):
    es = Elasticsearch()
    data = serializers.serialize('json', (instance, ))
    caller_function = inspect.stack()[0][3]
    doc = {
        'sender': 'Animal',
        'instance': data,
        'receiver': caller_function,
        'timestamp': datetime.now(),
    }

    print(doc)

    res = es.index(index="log-index", body=doc)
    print(res['result'])
    #print(instance.__dict__)
    #print(instance)
    #print(sender.__name__)
    #print(kwargs)
    print("an animal created!!!!")

class Animal(models.Model):
    name = models.CharField(max_length=100)
    sound = models.CharField(max_length=100)

    def speak(self):
        return  'The {} says \"{}\"'.format(self.name, self.sound)

    def __str__(self):
        return "{} {}".format(self.name, self.sound)

signals.post_save.connect(receiver=create_animal, sender=Animal)
