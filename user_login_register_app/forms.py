from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from user_login_register_app.models import User,Profile
from django.utils.translation import ugettext_lazy as _


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254,label=_('Adres email'))#,default=request)

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')
        labels = {'username': _('Nazwa użytkownika'),'password1': _('Haslo'),'password2': _('Potwierdź hasło'),}


class UserProfileForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ('_user_pln_per_km',)
		labels = {'_user_pln_per_km':_('Stawka za przejechany kilometr w PLN')}







