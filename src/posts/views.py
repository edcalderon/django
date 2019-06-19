from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from posts.models import Post

def post_list(request):
    query_set = Post.objects.all()
    context_data = {
        "object_list": query_set,
        "tittle": "Detail"
    }
    return  render(request,"index.html",context_data)

def post_create(request):
    context_data = {
        "tittle": "Create"
    }
    return  render(request,"index.html",context_data)

def post_detail(request, id=None): #retrive
    instance  = get_object_or_404(Post,id=id)
    context_data = {
        "tittle": instance.tittle,
        "instance": instance,
    }
    return  render(request,"post_detail.html",context_data)

def post_update(request):
    return  HttpResponse("<h1> update </h1>")

def post_delete(request):
    return  HttpResponse("<h1> delete</h1>")        