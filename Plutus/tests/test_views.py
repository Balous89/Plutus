# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from unittest import mock
from google_hermes.views import GetDataFromGoogleMap
from django.test.client import Client
from django.urls import reverse
import pytest
from django.contrib.auth import get_user_model
from django.core import mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from user_login_register_app.tokens import account_activation_token
from django.contrib.sites.models import Site
import requests



User = get_user_model()

# class TestGetDataFromGoogleMap:

#     


class TestGetDataFromGoogleMap:

    def test_request_post_to_api(self):
        with mock.patch.object(requests, 'post') as mocked_method:
            mocked_method.return_value.status_code = 200
           
            response = requests.post(reverse('scribe:transitrouteform'),data={'destination_city':'Wroclaw',
                                                                        'destination_district':'Dolnośląskie',
                                                                        'destination_number':34,
                                                                        'destination_street':'Hallera',
                                                                        'origin_city':'Klodzko',
                                                                        'origin_district':'Dolnośląskie',
                                                                        'origin_number':1,
                                                                        'origin_street':'Walecznych'})
            assert response.status_code == 200


    def test_make_request(self):
        request_klass = GetDataFromGoogleMap()

        with mock.patch.object(GetDataFromGoogleMap, 'make_request') as mocked_method:
            mocked_method.return_value = ('Osiedle Bolesława Śmiałego 38','Poznań','Hallera 182','Wrocław',float(189))

            response = request_klass.make_request(
                38, 'Osiedle Bolesława Śmiałego', 'Poznań', 'Wielkopolskie', 182, 'Hallera', 'Wrocław', 'Dolnośląskie')

            assert response[4] == 189.0



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
        return cls.user, cls.generated_activ_link, 


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

    @pytest.mark.django_db
    def test_activate(self):
        response = self.client.get(self.generated_activ_link)
        assert response.status_code == 302
        assert response.url == '/profile/'

    @pytest.mark.django_db
    def test_activation_fail(self):
        activation_link_with_bad_user = self.generated_activ_link.replace(urlsafe_base64_encode(force_bytes(self.user.pk)).decode(),'LTE')
        response = self.client.get(activation_link_with_bad_user)
        response_html = (str(response.getvalue()).replace('\\n',''))
        assert response.status_code == 200
        assert '<title>Invalid activation!</title>' in response_html
        
   
    @pytest.mark.django_db
    def test_auth_user_profile_access_and_post(self,user_client):
        response = user_client.post(reverse('user_login_register_app:profile'),data={'_user_pln_per_km':2})
        user = User.objects.get(email='testuser@gmail.com')
        assert response.status_code == 200
        assert user.profile._user_pln_per_km == 2


    @pytest.mark.django_db
    def test_unauth_user_profile_access(self):
        response = self.client.post(reverse('user_login_register_app:profile'),data={'_user_pln_per_km':2})
        assert response.status_code == 302
  
