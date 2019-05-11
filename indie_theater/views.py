from django.shortcuts import render, redirect
from .forms import ViewForm, CfForm, CommentForm, UserForm
from .models import Post, Comment, CfPost
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    post = Post.objects.all().order_by('-post_hit')
    return render(request, 'home.html', { 'posts' : post } )

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    return render(request, 'detail.html', { 'post' : post })

def mypage(request):
    post = Post.objects.all()
    return render(request, 'mypage.html', { 'posts' : post } )

def dit_detail(request):
    return render(request, 'dit_detail.html')

def crowdfunding(request):
    cfpost = CfPost.objects.all()
    return render(request, 'crowdfunding.html', { 'cfposts' : cfpost})

def crowd_new(request):
    if request.method == 'POST':
        form = CfForm(request.POST, request.FILES)
        cfpost = form.save(commit= False)
        cfpost.save()
        return redirect('crowd_detail', cfpost_pk = cfpost.pk)
    else:
        form = CfForm()
        return render(request, 'crowd_new.html', {'form': form})

def crowd_detail(request, cfpost_pk):
    cfpost= CfPost.objects.get(pk=cfpost_pk)
    return render(request, 'crowd_detail.html', { 'cfpost': cfpost })

def payment(request):
    return render(request, 'payment.html')

@login_required
def new(request):
    if request.method == 'POST':
        form = ViewForm(request.POST, request.FILES)
        post = form.save(commit= False)
        post.save()
        return redirect('detail', post_pk = post.pk)
    else:
        form =ViewForm()
        return render(request, 'new.html', {'form': form})

@login_required
def edit(request, post_pk):
    post = Post.objects.get(pk = post_pk)
    if request.method == 'POST':
        form = ViewForm(request.POST, instance = post)
        form.save()
        return redirect('detail', post.pk)
    else:
        form = ViewForm(instance = post)
    return render(request, 'edit.html', {'form':form})

@login_required
def delete(request, post_pk):
    post = Post.objects.get(pk = post_pk)
    post.delete()
    return redirect('home')

@login_required
def like(request, post_pk):
    post = Post.objects.get(pk = post_pk)
    post.post_like += 1
    post.save()
    return redirect('detail', post.pk)


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid(): #is_valid() : 장고 폼이 가진 valid한지 감별해주는 함수
            new_user = User.objects.create_user(**form.cleaned_data)
            auth.login(request, new_user)
            return redirect('home')
        else:
            form = UserForm()
            error = "아이디가 이미 존재합니다!"
            return render(request,'registration/signup.html', {'form': form, 'error': error})
    else:
        form = UserForm()
        return render(request, 'registration/signup.html', {'form' : form})
