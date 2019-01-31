from django.test import TestCase
from .models import Feature
from django.utils import timezone
from django.contrib.auth.models import User


class TestFeatureModel(TestCase):
    '''test Feature model'''
    
    def test_can_create_a_feature(self):
        '''Test I can create a feature'''
        
        user = User.objects.create_user(username='Ems_1', password='generic')
        feature = Feature(feature_author=user, feature_title='Test feature', details='Test this feature', price=50.00)
        feature.save()
        
        self.assertEqual(feature.feature_author, user)
        self.assertEqual(feature.feature_title, 'Test feature')
        self.assertEqual(feature.details, 'Test this feature')
        self.assertTrue(feature.created_date, True)
        self.assertEqual(feature.__str__(), feature.feature_title)
        