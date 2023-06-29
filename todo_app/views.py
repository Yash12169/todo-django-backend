from django.shortcuts import render,HttpResponse,redirect
from todo_app.models import User
# Create your views here.
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
def index_view(request):
    
    return render(request,'index.html')


def sign_up_view(request):
    page_name='signup.html'
    if request.method == "POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
       
        if not email:
            return render(request,page_name,{'error':True,'message':'email is empty'})
        if not username:
            return render(request,page_name,{'error':True,'message':'username is empty'})
        if not password:
            return render(request,page_name,{'error':True,'message':'password is empty'})
        if User.objects.filter(username=username).exists():
             return render(request,page_name,{'error':True,'message':'User already exists !'})
        if User.objects.filter(email=email).exists():
             return render(request,page_name,{'error':True,'message':'This email id is associated with any other username !'})
        if User.objects.filter(username=username).exists():
             return render(request,page_name,{'error':True,'message':'User already exists !'})
        User.objects.create_user(username=username,email=email,password=password)
        user=auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return redirect('index')
        else:
            return render(request,page_name,{'error':True,'message':'Authentication failed'})
    else:
        return render(request,page_name)


def sign_in_view(request):
    page_name='signin.html'
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        if not username:
            return render(request,page_name,{'error':True,'message':'username is empty'})
        if not password:
            return render(request,page_name,{'error':True,'message':'password is empty'})
        user=auth.authenticate(username=username,password=password)
        if user:
            auth.login(
                request,
                user
            )
            return redirect('index')
        else:
            return render(request,page_name,{'error':True,'message':'Authentication failed'})
    else:
        return render(request,'signin.html')



@login_required(login_url='sign_in')
def sign_out_view(request):
    auth.logout(request)
    return redirect('index')