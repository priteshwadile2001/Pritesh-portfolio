from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
# from django.utils.encoding import force_bytes,force_text
from django.utils.encoding import force_bytes, force_str

from django.views import View
from .utiles import generate_token
from Project import settings
from django.utils.encoding import force_str
from django.contrib.auth import authenticate,login,logout
from django.contrib.sites.shortcuts import get_current_site

def Signup(request):
    if request.method == "POST":
        Email = request.POST.get('email')
        Password = request.POST.get('pass1')
        Confirm_Password = request.POST.get('pass2')

        if Password != Confirm_Password:
            messages.warning(request,"Password and confirm password not matching")
            # return HttpResponse("Password and Confirm Password do not match")
            # return render(request,'singup.html')
            return render(request, 'singup.html')

        if User.objects.filter(username=Email).exists():
            messages.warning(request,"Email is taken")
            return render(request, 'singup.html')
        
            # return HttpResponse("Email already exists")

        user = User.objects.create_user(
            username=Email,
            email=Email,
            password=Password
        )
        user.is_active = False
        user.save()
       
        
    #     email_subject = "Activate your account"
    #     message = render_to_string('activate.html', {
    #     'user': user,
    #     'domain': '127.0.0.1:8000',
    #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
    #     'token': generate_token.make_token(user),
    # })

     

        current_site = get_current_site(request)

        email_subject = "Activate your account"
        message = render_to_string('activate.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user),
        })

        email_message = EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[Email])
        email_message.send()
        messages.success(request,"Activate your account using the link sent to your email..")
        return redirect('/auth/login/')
        # messages.success(request,"User is created successfully")
        # return HttpResponse("User is Created Successfully")


    return render(request, 'singup.html')

class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception:
            user = None

        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, "Account Activated Successfully")
            return redirect('/auth/login/')

        return render(request, 'activatefail.html')
    
def Login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pass1')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login Success")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/auth/login/')

    return render(request, 'login.html')
 
   

def Logout(request):
    logout(request)
    messages.info(request,"Logout Success")
    return redirect('/auth/login/')
   