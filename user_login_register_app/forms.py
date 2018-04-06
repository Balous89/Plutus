from django import forms
from django.contrib.auth.forms import UserCreationForm
from user_login_register_app.models import User



class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('email', 'username', 'password1','password2')
