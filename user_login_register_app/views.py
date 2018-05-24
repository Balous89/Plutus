from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from .forms import UserProfileForm

 
User = get_user_model()
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form['email'])
        if form.is_valid():
            user = form.save(commit=False)
            user.active = False
            user.email = form.cleaned_data.get('email') 
            user.save()
           
            current_site = get_current_site(request)
            subject = 'Activate Yours ForrestofSorrows Account'
            message_context = {
                'user':user,
                'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user)}
            message = render_to_string('user_login_register_app/account_activation_email.html',message_context)
            send_mail(subject,message,'registration@infosecremedy.com',[user.email],)
            return redirect('user_login_register_app:account_activation_sent')
    else:
        form = SignUpForm()
    return render(request,'user_login_register_app/signup.html',{'form':form},)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        print('USER:',user.username)
        print('TOKEN CORRECT:',bool(account_activation_token.check_token(user, token)))
        user.active = True
        print('ACTIVE')
        user.profile.email_confirmed = True
        print('CONFIRMED')
        user.save()
        print('SAVED')
        login(request, user)
        return redirect('user_login_register_app:profile')
    else:
        return render(request, 'user_login_register_app/account_activation_invalid.html')


class UserProfileView(View):


    def get(self,request):
        if request.user.is_authenticated:
            user = request.user
            pln_per_km_form = UserProfileForm()
            return render(request,'user_login_register_app/profile.html',{'user':request.user,'pln_per_km_form':pln_per_km_form})
        #else:
        return redirect('user_login_register_app:login')
    def post(self,request):
        if request.user.is_authenticated:
            pln_per_km_form = UserProfileForm(request.POST)
            if request.method == 'POST':
                if pln_per_km_form.is_valid():
                    request.user.profile.user_pln_per_km = pln_per_km_form.cleaned_data['_user_pln_per_km']
                    request.user.profile.save()
                    return render(request,'user_login_register_app/profile.html',{'user':request.user,'pln_per_km_form':pln_per_km_form})
        return redirect('user_login_register_app:login')

         