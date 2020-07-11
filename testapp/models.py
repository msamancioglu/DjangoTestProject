from django.db import models
from django.db.models import signals
from datetime import datetime
from elasticsearch import Elasticsearch
from django.core import serializers
from django.forms.models import model_to_dict


import inspect
import json
# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=100)
    sound = models.CharField(max_length=100)

    def speak(self):
        return  'The {} says \"{}\"'.format(self.name, self.sound)

    def __str__(self):
        return "{} {}".format(self.name, self.sound)

def create_animal(sender, instance, created, **kwargs):
    es = Elasticsearch()
    data = serializers.serialize('json', [instance, ])
    #struct = json.loads(data)
    #data = json.dumps(struct[0])
    caller_function = inspect.stack()[0][3]
    import ast
    doc = {
        'sender':  type(instance).__name__,
        'instance': ast.literal_eval(data),
        'receiver': caller_function,
        'timestamp': datetime.now(),
    }
    print(doc)
    res = es.index(index="log-index", doc_type="logs",  body=doc)
    print(res['result'])
    print(ast.literal_eval(data))
    print("an animal created!!!!")

signals.post_save.connect(receiver=create_animal, sender=Animal)
