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


User = get_user_model()
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Yours ForrestofSorrows Account'
            message = render_to_string('user_login_register_app/account_activation_email.html',{
                'user':user,
                'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user)})
            send_mail(subject,message,'registration@infosecremedy.com',[user.email],)
            return redirect('user_login_register_app:account_activation_sent')



            # email = form.cleaned_data.get('email')
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # user = authenticate(email=email,password=password)
            # login(request,user)
            # return redirect('photos:home')
    else:
        form = SignUpForm()
    return render(request,'user_login_register_app/signup.html',{'form':form},)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        print('HERE!!!!!!!!!: '+uid)
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('user_login_register_app:login')
    else:
        return render(request, 'user_login_register_app/account_activation_invalid.html')

