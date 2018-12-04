from django.test import TestCase
from .models import Post
from django.utils import timezone

class TestPostModel(TestCase):
    
    def test_can_create_a_post(self):
        post = Post(title='Test title', content='Test content')
        post.save()
        
        self.assertEqual(post.title, 'Test title')
        self.assertEqual(post.content, 'Test content')
        self.assertEqual(post.views, 0)
        self.assertEqual(post.image, None)
        self.assertTrue(post.created_date, True)
        self.assertEqual(post.__unicode__(), post.title)