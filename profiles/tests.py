from django.test import TestCase
from unittest.mock import patch
from django.contrib.auth.models import User
from django.urls import resolve, reverse

import factory

from .views import HomePage 
from posts import models

class PostFactory(factory.Factory):
    class Meta:
        model = models.Post

    message = ""

class HomePageOpenTestCase(TestCase):

    def test_home_page_resolves(self):
        view = resolve(reverse('home'))
        self.assertEqual(view.func.__name__,
                        HomePage.as_view().__name__, )
        

class TestSuperHeroCheck(TestCase):

    def test_superhero_check_service(self):
        with patch('profiles.models.SuperHeroWebAPI') as ws:
            ws.is_hero.return_value = True
            u = User.objects.create(username = 't')
            res = u.profile.is_superhero()
            
        
        ws.is_hero.assert_called_with('t')
        self.assertTrue(res)


#test using factory pacakage 
class PostTestCase(TestCase):

    def setUp(self):
        self.blank_post = PostFactory.create()
        self.silly_post = PostFactory.create(message="silly")
    
    def test_post_title(self):
        self.assertEqual(self.blank_post.message, '')
        self.assertEqual(self.silly_post.message, 'silly')
