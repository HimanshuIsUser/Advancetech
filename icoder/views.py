from ast import Not
from contextlib import redirect_stderr
from django.shortcuts import render,HttpResponse,redirect
from icoder.models import Icodercomment, Post
from django.contrib.auth.models import User
from django.contrib import messages
from icoder.templatetags import extras

# Create your views here.
def icoderhome(request):
    allpost = Post.objects.all()
    context = {'allpost':allpost}
    return render(request,'icoder/icoderhome.html',context)

def icoderpost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    comments = Icodercomment.objects.filter(post=post,parent=None)
    post.views = post.views + 1
    post.save()
    replies = Icodercomment.objects.filter(post=post).exclude(parent=None)
    replydict={}
    for reply in replies:
        if reply.parent.sno not in replydict.keys():
            replydict[reply.parent.sno]=[reply]
        else:
            replydict[reply.parent.sno].append(reply)
    context = {'post':post,'comments': comments,'user':request.user,'replydict':replydict}
    return render(request,'icoder/icoderpost.html',context)

def postcomment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postsno = request.POST.get("postsno")
        post = Post.objects.get(sno=postsno)
        parentsno=request.POST.get('parentsno')

        if parentsno==None:
            comment = Icodercomment(comment=comment,user = user,post = post)
            comment.save()
            messages.success(request,'comment Posted')
        else:
            parent= Icodercomment.objects.get(sno=parentsno)
            comment = Icodercomment(comment=comment,user = user,post = post,parent=parent)
            comment.save() 
            messages.success(request,'reply Posted')  
    return redirect(f"/icoder/{post.slug}")
 