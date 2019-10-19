from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
'''from .models import Post,Comment
from  .forms import PostForm,CommentForm'''
from django.contrib.auth.decorators import login_required 

def post_list(request):
    return render(request, 'blog/home.html', { })
#def login(request):
    #return render(request,'blog/registration/login.html',{ })    

# Create your views here.
