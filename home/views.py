from re import L
import re
from django.shortcuts import render,HttpResponse,redirect
from icoder.models import Post
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.db.models import Max

# Create your views here.
def home(request):
    allpost = Post.objects.all().order_by('-views')[0:3]
    # for i in allposts:
    #     if i in replydict:
    #         pass
    #     elif i not in replydict and i.views > allpost.keys:
    #         replydict[i.views].append(i)
    context = {'allpost':allpost}
    print(allpost)
    return render(request,'home/home.html',context)

def about(request):
    return render(request,"home/about.html")

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request,'Please fill the form correctly')
        else:
            content = Contact(name=name,email=email,phone=phone,content=content)
            content.save()
            messages.success(request,'your form has been successfull')
    return render(request,"home/contact.html")

def search(request):
    query = request.GET["query"]
    if len(query)>78:
        allpost=Post.objects.none()
    else:
        tallpost=Post.objects.filter(title__icontains=query)
        callpost=Post.objects.filter(content__icontains= query)
        allpost=tallpost.union(callpost)

    if allpost.count() == 0:
        messages.warning(request,"please fill the form correctly")
    result = {'allpost':allpost,'query':query}
    print(result)
    return render(request,"home/search.html",result)

def handlesignup(request):
    if request.method == 'POST':
        #Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        # check for errorneous inputs
        if len(username) > 10 :
            messages.error(request,"the username has more then 10 characters")
            return redirect('home')


        if  password != password2:
            messages.error(request,"Your password doesn't match")
            return redirect('home')

        if not username.isalnum():
            messages.error(request,"Invalid username")
            return redirect('home')


        #create the user
        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = fname
        myuser.last_name  = lname
        myuser.save()
        messages.success(request,"Your ICoder account has been successfully created")
        return redirect('home')
    else:
        return HttpResponse("404 - NOT FOUND")

def handlelogin(request):
    if request.method == 'POST':
        #Get the post parameters
        loginusername  = request.POST['logusername']
        loginpassword  = request.POST['logpassword']
        user = authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"successfully login")
            return redirect('home')
        else:
            messages.error(request,'Invalid Credentials, please try again')
            return redirect('home')

    return HttpResponse("404 - Page Not Found")



def handlelogout(request):
    logout(request)
    messages.success(request,"successfully Logout")
    return redirect('home')