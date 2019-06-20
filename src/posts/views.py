from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages


from posts.models import Post
from .forms import PostForm

def post_list(request):
    query_set = Post.objects.all()
    context= {
        "object_list": query_set,
        "tittle": "Detail"
    }
    return  render(request,"post_list.html",context)

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False) 
        # print (form.cleaned_data.get('tittle'))  
        instance.save()
        messages.success(request, "Successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request," Not Successfully created")
    context = {
        "form": form,
    }
    return  render(request,"post_form.html",context)

def post_update(request, id=None): 
    instance  = get_object_or_404(Post,id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False) 
        instance.save()
        messages.success(request, "<a href='#'>Item</a> Saved" , extra_tags='html_safe')
        return  HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "tittle": instance.tittle,
        "instance": instance,
        "form": form,
    }
    return  render(request,"post_form.html",context)

def post_detail(request, id=None):
    instance  = get_object_or_404(Post,id=id)
    context = {
        "tittle": instance.tittle,
        "instance": instance,
    }
    return  render(request,"post_detail.html",context)

def post_delete(request, id=None):
    instance = get_object_or_404(Post,id=id)
    instance.delete()
    messages.success(request, "Deleted")
    return redirect("posts:list")      