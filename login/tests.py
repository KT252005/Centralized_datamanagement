from django.test import TestCase
from login.models import *
# Create your tests here.
class ChatSignupTestCase(TestCase):
 def setUp(self):
        # Set up data for the whole TestCase
        Chat_signup.objects.create(
            username='testuser',
            first_name='Test',
            last_name='User',
            email='testuser@example.com',
            password='testpassword'
        )
 def test_chat_signup_creation(self):
        """Test the creation of a Chat_signup record"""
        user = Chat_signup.objects.get(username='testuser')
        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.last_name, 'User')
        self.assertEqual(user.email, 'testuser@example.com')      


