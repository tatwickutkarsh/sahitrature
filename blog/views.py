from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
'''from .models import Post,Comment
from  .forms import PostForm,CommentForm'''
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth import login,authenticate
def post_list(request):
    return render(request, 'blog/home.html', { })
#def login(request):
    #return render(request,'blog/registration/login.html',{ })    

# Create your views here.
def registration(request):
    if request.method=='POST':
        form= UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password =form.cleaned_data.get('password')
            user=authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('post_list')
    else:
        form= UserForm()
    return render(request,'registration/signup.html',{'form' : form})    

