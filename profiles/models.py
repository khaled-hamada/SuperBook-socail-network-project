from django.db import models
from django.conf import settings 
import datetime

from .services import SuperHeroWebAPI


class BaseProfile(models.Model):
    USER_TYPES = (
        (0, 'Ordinary'),
        (1, 'SuperHero'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                primary_key=True)
    user_type = models.IntegerField(null=True, choices=USER_TYPES)
    bio = models.CharField(max_length=200, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.user}: {self.bio or "":.20}'
    
    @property
    def age(self):
        today = datetime.date.today()

        return (today.year - self.birthdate.year) - int(
                    (today.month, today.day) < 
                    (self.birthdate.month, self.birthdate.day)) 

    class Meta:
        abstract = True
    

class SuperHeroProfile(models.Model):
    origin = models.CharField(max_length = 100, blank=True, null=True)

    class Meta:
        abstract = True


class OrdinaryProfile(models.Model):
    address = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        abstract = True

class Profile(SuperHeroProfile, OrdinaryProfile,
                BaseProfile):
    
    def is_superhero(self):
        return SuperHeroWebAPI.is_hero(self.user.username) 

