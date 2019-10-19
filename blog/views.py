from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
'''from .models import Post,Comment
from  .forms import PostForm,CommentForm'''
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from .forms import UserForm
def post_list(request):
    return render(request, 'blog/home.html', { })
#def login(request):
    #return render(request,'blog/registration/login.html',{ })    

# Create your views here.
def registration(request):
    if request.method=='POST':
        form= UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name= form.cleaned_data['last_name']
            email= form.cleaned_data['email']
            password =form.cleaned_data['password']
            User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password,email=email)
            return redirect('post_list')
    else:
        form= UserForm()
    return render(request,'registration/signup.html',{'form' : form})    

