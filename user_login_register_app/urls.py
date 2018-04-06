from django.urls import path,re_path
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.auth import views as auth_views

app_name = 'user_login_register_app'


urlpatterns = [
    path('signup/',views.signup,name='signup' ),
    path('login/', auth_views.login, {'template_name': 'user_login_register_app/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'template_name': 'user_login_register_app/logged_out.html'}, name='logout'),
    path('account_activation_sent/', TemplateView.as_view(template_name='user_login_register_app/account_activation_sent.html'), name='account_activation_sent'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]
