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

    #body = '{"destination_addresses" : [ "Petuniowa 9, 53-238 Wrocław, Poland" ],"origin_addresses" : [ "Osiedle Bolesława Śmiałego 38, Poznań, Poland" ],"rows" : [{"elements" : [{"distance" : {"text" : "184 km","value" : 184415},"duration" : {"text" : "2 hours 33 mins","value" : 9198},"status" : "OK"}]}],"status" : "OK" }'

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

    @pytest.mark.django_db
    def test_signup(self):
        self.client = Client()
        resquest = self.client.post(reverse('user_login_register_app:signup'), data={
                                    'email': 'testuser@gmail.com', 'password1': 'bumerang', 'password2': 'bumerang', 'username': 'testuser'})

        user = User.objects.get(username='testuser')

        assert user.email == 'testuser@gmail.com'
        assert user.username == 'testuser'
        assert user.active == False
        assert user.staff == False
        assert user.admin == False

    @pytest.mark.django_db
    def test_signup(self):
        self.client = Client()
        resquest = self.client.post(reverse('user_login_register_app:signup'), data={
                                    'email': 'testuser@gmail.com', 'password1': 'bumerang', 'password2': 'bumerang', 'username': 'testuser'})

        user = User.objects.get(username='testuser')

        assert user.email == 'testuser@gmail.com'
        assert user.username == 'testuser'
        assert user.active == False
        assert user.staff == False
        assert user.admin == False



    @pytest.mark.django_db
    def test_send_email(self,request):
        self.client = Client()
        self.request = self.client.post(reverse('user_login_register_app:signup'), data={
                                    'email': 'testuser@gmail.com', 'password1': 'bumerang', 'password2': 'bumerang', 'username': 'testuser'})
        self.current_site = Site.objects.get_current()
      
        self.user = User.objects.get(username='testuser')
        message_context = {
                'user': self.user,
                'domain': self.current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(self.user.pk)).decode(),
                'token': account_activation_token.make_token(self.user)}

        assert len(mail.outbox) == 1
        generated_link = 'http://{}/activate/{}/{}/'.format(message_context['domain'], message_context['uid'], message_context['token'])
        assert generated_link in mail.outbox[0].body

    def test_signup_get(self):
        self.client = Client()
        request = self.client.get(reverse('user_login_register_app:signup'))
        assert request.status_code == 200

    # def test_activate(self):
