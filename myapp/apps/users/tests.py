from django.test import TestCase, RequestFactory

from .backends import JWTAuthentication
from .views import RegistrationView, LoginView

import json


class UsersAppTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.auth = JWTAuthentication()
        self.reg_user = {'user':
                         {
                             'username': 'user1',
                             'email': 'user1@gmail.com',
                             'password': 'password'
                         }
                         }

        self.reg_user2 = {'user':
                          {
                              'username': 'user2',
                              'email': 'user2@gmail.com',
                              'password': 'password'
                          }
                          }

        self.login_user = {
            'user': {'email': 'user1@gmail.com', 'password': 'password'}}
        self.login_user2 = {
            'user': {'email': 'user2@gmail.com', 'password': 'password'}}

    def register(self, user):
        request = self.factory.post('/api/v1/auth/signup/',
                                    data=json.dumps(user),
                                    content_type='application/json')
        response = RegistrationView.as_view()(request)
        return response

    def login(self, user):
        request = self.factory.post('/api/v1/auth/login/',
                                    data=json.dumps(user),
                                    content_type='application/json')
        response = LoginView.as_view()(request)
        return response

    def test_user_registration_success(self):
        response = self.register(self.reg_user)
        self.assertEqual(response.status_code, 201)

    def test_user_login_success(self):
        # register the user
        self.register(self.reg_user)
        # login the user
        response = self.login(self.login_user)
        self.assertEqual(response.status_code, 200)
