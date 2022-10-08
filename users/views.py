from unicodedata import category
from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from django.template import loader
from .forms import *
from .models import User

def index(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        print(username)
        print(password)
        if(User.objects.filter(username=username).exists()):
            user = User.objects.get(username=username)
            if user.password == password:
                if user.type=="1":
                    return redirect('doctor/'+str(user.id))
                else:
                    return redirect('patient/'+str(user.id))
            else:
                return render(request, "index.html", {'error':'Invalid credentials'})
        else:
            return render(request, "index.html", {'error':'Invalid credentials'})
    return render(request, "index.html")

def signup(request):
    form = Registeration()
    return render(request, "signup.html", {'form': form})

def signupdata(request):  
    if request.method == 'POST':  
        form =  Registeration(request.POST, request.FILES)  
        if form.is_valid():  
            user = form.save()  
            if user.type=="1":
                return redirect('doctor/'+str(user.id))
            else:
                return redirect('patient/'+str(user.id))
    return render(request, 'signup.html')  

def doctor(request, id):
    user = User.objects.get(id=id)
    template = loader.get_template('doctor.html')
    blog = newBlog()
    return HttpResponse(template.render({'user':user, 'blogform': blog}, request))

def patient(request, id):
    user = User.objects.get(id=id)
    template = loader.get_template('patient.html')
    return HttpResponse(template.render({'user':user},request))

def addblog(request):
    if request.method == 'POST':
        form =  newBlog(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.POST["userid"]
            blog.isdraft=2
            if request.POST.get("savedraft",False):
                blog.isdraft=1
                print("yes1")
            else:
                blog.isdraft=0
                print("yes2")
            print(blog.isdraft)
            blognew = Blog(title=blog.title, summary=blog.summary, content=blog.content, user=blog.user, isdraft=blog.isdraft, image=blog.image, category=blog.category)
            blognew.save()
        return redirect('doctor/'+str(request.POST["userid"]))

def update(request, id, blogid):
    blog = Blog.objects.get(id=blogid)
    template = loader.get_template('update.html')
    context = {
        'blog': blog,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id, blogid):
    blog = Blog.objects.get(id=blogid)
    blog.title = request.POST.get('title', "")
    blog.summary = request.POST.get('summary', "")
    blog.content = request.POST.get('content', "")
    blog.isdraft = 2
    if request.POST.get("savedraft",False):
        blog.isdraft=1
    else:
        blog.isdraft=0
    blog.save()
    return redirect('/doctor/'+str(id))

def drafts(request, id):
    user = User.objects.get(id=id)
    template = loader.get_template('drafts.html')
    blog = newBlog()
    draftblogs = Blog.objects.filter(user=id, isdraft=1)
    print(draftblogs)
    return HttpResponse(template.render({'user':user, 'blogform': blog, 'drafts':draftblogs}, request))

def blogs(request, id):
    user = User.objects.get(id=id)
    template = loader.get_template('blogs.html')
    blog = newBlog()
    publishedblogs = Blog.objects.filter(user=id, isdraft=0)
    return HttpResponse(template.render({'user':user, 'blogform': blog,'publishedblogs':publishedblogs}, request))

def viewblogs(request, id, catid):
    blogs = Blog.objects.filter(category=catid, isdraft=0)
    template = loader.get_template('viewblogs.html')
    user = User.objects.get(id=id)
    return HttpResponse(template.render({'user':user, 'blogs':blogs}, request))

def viewblog(request, id, blogid):
    blog = Blog.objects.get(id=blogid)
    template = loader.get_template('blog.html')
    user = User.objects.get(id=id)
    return HttpResponse(template.render({'user':user, 'blog':blog}, request))

def docviewblog(request, id, blogid):
    blog = Blog.objects.get(id=blogid)
    template = loader.get_template('docblog.html')
    user = User.objects.get(id=id)
    return HttpResponse(template.render({'user':user, 'blog':blog}, request))