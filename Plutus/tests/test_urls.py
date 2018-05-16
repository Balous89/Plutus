from django.urls import reverse,resolve
from django.http import HttpRequest
from scribe.views import home_page
from user_login_register_app.views import signup
from django.test.client import Client
from django.contrib.auth import get_user_model
from django.contrib.auth.views import login as generic_login

import pytest

User = get_user_model()



class TestUrls:

	@pytest.mark.parametrize('url_name,html_content',[
		('home_page','<title>Witaj nieznajomy!</title>'),
		('user_login_register_app:account_activation_sent','<title>Rejestracja powiodla sie!</title>'),
		('user_login_register_app:login','<title>Login</title>'),
		('user_login_register_app:logout','<title>Do zobaczenia!</title>'),
		])
	def test_login_unrequire_pages(self,url_name,html_content):
		self.client = Client()
		request = self.client.get(reverse(url_name))
		response = str(request.getvalue()).replace('\\n','')
		print(response)
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
	def test_notatnik_page_content(self,url_name,html_content): 
		self.client = Client()
		self.user = User.objects.create_user('testuser@infosec_remedy.com',
			'testuser',password='bumerang',is_active=True)
		self.client.login(email='testuser@infosec_remedy.com', password='bumerang') 
		response = self.client.get(reverse(url_name))
		html = str(response.getvalue()).replace('\\n','')
		assert response.status_code == 200
		assert html_content in html

 
 
  

 
   
