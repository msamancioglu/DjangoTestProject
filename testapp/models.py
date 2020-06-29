from django.db import models

# Create your models here.


class Animal(models.Model):
    name = models.CharField(max_length=100)
    sound = models.CharField(max_length=100)

    def speak(self):
        return  'The {} says \"{}\"'.format(self.name, self.sound)

    def __str__(self):
        return "{} {}".format(self.name, self.sound)


