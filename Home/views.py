from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Post,extrainfo
from django.db.models import Q
# Create your views here.
def homepage(request):
    return render(request,"Home/homepage.html")
def Login(request):
    if request.method=='POST':
        username= request.POST['username']
        password= request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('blog')
        else:
            messages.error(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'Home/login.html')
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password1']
        password2=request.POST['password2']
        gender=request.POST['gender']
        country=request.POST['nationality']
        dayofbirth=request.POST['dayofbirth']
        monthofbirth=request.POST['monthofbirth']
        yearofbirth=request.POST['yearofbirth']
        profilepicture=request.FILES.get('profilepic')
    
        #check password match
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'unfortunately,this username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'unfortunately,this email is already used')
                    return redirect('register')
                else:
                    user= User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    extra=extrainfo(gender=gender,user=user,Nationality=country,dayofbirth=dayofbirth,monthofbirth=monthofbirth,yearofbirth=yearofbirth)
                    extra.save()
                    #login after registration
                    auth.login(request,user)
                    messages.success(request,'successfuly registered at FLIPER')
                    return redirect('blog')
        else:
            messages.error(request,'passwords dont match!')
            return redirect('register')
                
    else:
        return render(request,'Home/register.html')


def PostList(request):
    all_posts=Post.objects.all()
    context={'all_posts':all_posts}
    return render(request,"Home/blog.html",context)
    
def addpost(request):
    if request.method=='POST':
        title=request.POST['title']
        content=request.POST['content']
        status=request.POST['status']
        photo=request.FILES.get('myfile')
        
        post=Post(title=title,status=status,content=content,author=request.user,productimage=photo)
        post.save()
        return redirect('blog')
    else:
        return render(request,"Home/addpost.html")
   
def search(request):
    if request.method=='GET':
        search=request.GET['search']
        post=Post.objects.all().filter(title__contains=search)
        return render(request,'Home/results.html',{'post':post})
    
def terms(request):
    return render(request,"Home/terms.html")

def logout_view(request):
    logout(request)
    return redirect('home')
def profile(request):
    if request.method=='POST':
        newusern=request.POST['newusername']
        fn=request.POST['firstn']
        ln=request.POST['lastn']
        em=request.POST['ema']
        passw=request.POST['passwo']
        password2=request.POST['password2']
        if passw==password2:
            user=User.objects.get(username=request.user)
            user.username=newusern
            user.first_name=fn
            user.last_name=ln
            user.email=em
            user.password=passw
            user.set_password(user.password)
            user.save()
            return redirect('blog')
            
                
        else:
            messages.error(request,'passwords dont match!')
            return redirect('profile')
                


       
    else:
        return render(request,'Home/profile.html')