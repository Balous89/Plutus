from django.urls import reverse
from django.test.client import Client
from django.contrib.auth import get_user_model

import pytest

User = get_user_model()

  

class TestUrls:

	@pytest.mark.parametrize('url_name,html_content',[
		('home_page','<title>Witaj nieznajomy!</title>'),
		('user_login_register_app:account_activation_sent','<title>Rejestracja powiodla sie!</title>'),
		('user_login_register_app:login','<title>Login</title>'),
		('user_login_register_app:logout','<title>Do zobaczenia!</title>'),
		])
	@pytest.mark.django_db
	def test_login_unrequire_pages(self,url_name,html_content):
		self.client = Client()
		request = self.client.get(reverse(url_name))
		response = str(request.getvalue()).replace('\\n','')
		
		assert html_content in response
		assert request.status_code == 200
	
	@pytest.mark.parametrize('url_name,code',[
		('scribe:transitrouteform',302),
		('user_login_register_app:profile',302)
		])
	def test_login_require_pages(self,url_name,code):
		self.client = Client()
		request = self.client.get(reverse(url_name))
		response = str(request.getvalue()).replace('\\n','')
		assert request.status_code == 302
		
	@pytest.mark.parametrize('url_name,html_content',[
		('scribe:transitrouteform','Zalogowany jako: testuser'),
		('user_login_register_app:profile','<title>Twoj profil</title>')
		])	 
	@pytest.mark.django_db
	def test_notatnik_page_content(self,url_name,html_content,user_client): 
		response = user_client.get(reverse(url_name))
		html = str(response.getvalue()).replace('\\n','')
		assert response.status_code == 200
		assert html_content in html

 
 
  

     
 