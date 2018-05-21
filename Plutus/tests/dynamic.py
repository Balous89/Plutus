
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
        # success_mail = send_mail('Subject', 'Message', 'mail_from@infosecremedy.com', ['usermail@infosecremedy.com'])
        # assert success_mail == True
 
        self.client = Client()
        self.request = self.client.post(reverse('user_login_register_app:signup'), data={
                                    'email': 'testuser@gmail.com', 'password1': 'bumerang', 'password2': 'bumerang', 'username': 'testuser'})
        self.current_site = Site.objects.get_current()
        # current_site.domain
        # self.request.get_host()
        self.user = User.objects.get(username='testuser')
        message_context = {
                'user': self.user,
                'domain': self.current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(self.user.pk)).decode(),
                'token': account_activation_token.make_token(self.user)}

        assert len(mail.outbox) == 1
        generated_link = 'http://{}/activate/{}/{}/'.format(message_context['domain'], message_context['uid'], message_context['token'])


        assert mail.outbox[0].subject == 'Activate Yours ForrestofSorrows Account'
        assert generated_link in mail.outbox[0].body
