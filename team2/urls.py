"""team2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from indie_theater import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('detail/<int:post_pk>/', views.detail, name="detail"),
    path('edit/<int:post_pk>/', views.edit, name="edit"),
    path('delete/<int:post_pk>/', views.delete, name="delete"),
    path('mypage/', views.mypage, name="mypage"),
    path('dit_detail/', views.dit_detail, name="dit_detail"),
    path('crowdfunding/', views.crowdfunding, name="crowdfunding"),
    path('payment/', views.payment, name="payment"),
    path('crowd_detail/<int:cfpost_pk>/', views.crowd_detail, name="crowd_detail"),
    path('crowd_new/', views.crowd_new, name="crowd_new"),
    path('new/', views.new, name="new"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('like/<int:post_pk>/', views.like, name='like'),
    path('post/<int:post_pk>/<int:comment_pk>', views.comment_delete, name='delete_comment'),
    path('cfpost/<int:cfpost_pk>/<int:cfcomment_pk>', views.comment_delete_2, name='delete_comment_2'),
]
