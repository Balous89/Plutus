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







# def __init__(self, *args, **kwargs):
# 	super(SignUpForm, self).__init__(*args, **kwargs)

# 	# self.fields['email'].label = _('Adres email')
# 	#self.fields['password1'].label = _('Hasło')
# 	self.fields['password2'].label = _('Potwierdź hasło')

# 	    # self.fields['password1'].widget.attrs['class'] = 'form-control'
# 	    # self.fields['password2'].widget.attrs['class'] = 'form-control'

# class EditProfileForm(UserChangeForm):

# 	class Meta:
# 		model=Profile
# 		fields = 