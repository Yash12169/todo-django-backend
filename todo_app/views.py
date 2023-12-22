from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from rest_framework.response import Response
from todo_app.models import User,Todo
# Create your views here.
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,DestroyAPIView
from .serializers import ReadTodoListSerializer
from time import sleep,time

@login_required(login_url='sign_in')
def index_view(request):
    data={
        "todo_list" : Todo.objects.filter(user=request.user).order_by("-created_at")
    }
    return render(request,'index.html' ,context=data)


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




@login_required(login_url='sign_in')
def create_todo_view(request):
    todo_title=request.POST['todotitle']
    Todo.objects.create(
        title=todo_title,
        user=request.user
    )
    return redirect("index")







@login_required(login_url='sign_in')
def delete_todo_view(request):

    if request.method=='POST':
        todo_id=request.POST.get('todo_id')
        todo=get_object_or_404(Todo,id=todo_id)
        todo.delete()
        return redirect('index')

    else:
        return redirect('index')
    


class DrfListView(ListAPIView):
    queryset=Todo.objects.all()
    serializer_class = ReadTodoListSerializer
    pagination_class = None
    def list(self, request, *args, **kwargs):
        # time.sleep(5)
        return super().list(request, *args, **kwargs)

class DrfCreateView(APIView):
    def post(self,request):
        title = request.data.get('title')
        todo_object = Todo.objects.create(
            title=title
        )
        response_data = ReadTodoListSerializer(instance=todo_object).data
        return Response(response_data)


class DrfDeleteView(APIView):
   def post(self,request):
        todo_id = request.data.get('todo_id')
        todo_object = Todo.objects.get(pk=todo_id)
        todo_object.delete()
      
        return Response("Todo Deleted")