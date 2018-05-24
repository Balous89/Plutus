# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import httpretty
from unittest import mock
from google_hermes.views import GetDataFromGoogleMap
from django.test.client import Client
from django.urls import reverse
import pytest
from django.contrib.auth import get_user_model
from pprint import pprint
import json
from django.core.mail import send_mail
from django.core import mail
from django.utils.encoding import force_bytes
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from user_login_register_app.tokens import account_activation_token
from asyncio.transports import BaseTransport

from django.contrib.sites.models import Site

User = get_user_model()

class TestGetDataFromGoogleMap:

    def test_make_request(self):
        request_klass = GetDataFromGoogleMap()

        with mock.patch.object(GetDataFromGoogleMap, 'make_request') as mocked_method:
            mocked_method.return_value = {"destination_addresses": ["Petuniowa 9, 53-238 Wrocław, Poland"],
                                                     "origin_addresses": ["Osiedle Bolesława Śmiałego 38, Poznań, Poland"],
                                                     "rows": [{"elements": [{"distance": {"text": "184 km", "value": 184415},
                                                                             "duration": {"text": "2 hours 33 mins", "value": 9198}, "status": "OK"}]}], "status": "OK"
                                                     }

            response = request_klass.make_request(
                38, 'Osiedle Bolesława Śmiałego', 'Poznań', 'Wielkopolskie', 9, 'Petuniowa', 'Wrocław', 'Dolnośląskie')

        assert response['rows'][0]['elements'][0]['distance']['text'] == "184 km"


class TestSignUp:

    @classmethod
    def setup(cls):
        cls.client = Client()
        cls.req = cls.client.post(reverse('user_login_register_app:signup'), data={
                                    'email': 'testuser@gmail.com', 'password1': 'bumerang',
                                    'password2': 'bumerang', 'username': 'testuser'})
        cls.user = User.objects.get(username='testuser')
        cls.current_site = Site.objects.get_current()
        cls.message_context = {
                'user': cls.user,
                'domain': cls.current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(cls.user.pk)).decode(),
                'token': account_activation_token.make_token(cls.user)}
        cls.generated_activ_link = 'http://{}/activate/{}/{}/'.format(cls.message_context['domain'], cls.message_context['uid'], cls.message_context['token'])
        return cls.user, cls.generated_activ_link


    @pytest.mark.parametrize('user_model_attribute,signup_user_attribute', [
        ('self.user.email', 'testuser@gmail.com'),
        ('self.user.username', 'testuser'),
        ('self.user.active', False),
        ('self.user.staff', False),
        ('self.user.admin', False),
        ])
    @pytest.mark.django_db
    def test_signed_up_user_attributes(self, user_model_attribute, signup_user_attribute):
        assert eval(user_model_attribute) == signup_user_attribute
      
    @pytest.mark.django_db
    def test_send_activation_email(self):
        assert len(mail.outbox) == 1
       
    @pytest.mark.django_db
    def test_activation_email_contain_correct_activ_link(self):
        assert self.generated_activ_link in mail.outbox[0].body

    @pytest.mark.django_db
    def test_signup_get(self):
        request = self.client.get(reverse('user_login_register_app:signup'))
        assert request.status_code == 200

    # @pytest.mark.django_db
    # def test_activate(self):
    #     print(self.generated_activ_link)
    #     print(self.message_context['domain'])
    #     self.client.get(self.generated_activ_link)
    #     assert self.user.active == True
