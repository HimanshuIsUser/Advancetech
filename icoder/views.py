from django.shortcuts import render,HttpResponse

# Create your views here.
def icoderhome(request):
    return render(request,'icoder/icoderhome.html')

def icoderpost(request,slug):
    return render(request,'icoder/icoderpost.html',{'slug':slug})