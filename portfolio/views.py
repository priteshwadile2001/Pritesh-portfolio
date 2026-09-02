from django.shortcuts import render ,redirect
from django.contrib import messages
from .models import Contact , Blogs
# Create your views here.


def home_page(request):
    return render (request,'portfolio/apphome.html')

def about(request):
    return render (request,'about.html')

def contact(request):
    if request.method == "POST":
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        fphone_number = request.POST.get('pnumber')
        fdesc = request.POST.get('desc')

        query = Contact(
            name=fname,
            email=femail,
            phonenumber=fphone_number,
            desc=fdesc
        )
        query.save()

        messages.success(
            request,
            'Thanks for contacting us. We will get back to you soon.'
        )
        return redirect('/contact')

    return render(request, 'contact.html')

def blog(request):
    posts = Blogs.objects.all()
    context = {"posts":posts}
    print(context,"*******************")
    return render (request,'blog.html',context)


def Resume_skills(request):
    return render (request,'Resume_skills.html')