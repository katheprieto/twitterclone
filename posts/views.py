from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy, reverse
from cloudinary.forms import cl_init_js_callbacks


def index(request):
    form = PostForm(request.POST, request.FILES)
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
       # If the form is valid
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form)

    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]

    # Show
    return render(request, 'posts.html',
                  {'posts': posts,'form':form})


def delete(request, post_id):
    # Find post
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')


def LikeView(request, post_id):
    post = Post.objects.get(id=post_id)
    new_value = post.likes + 1
    post.likes = new_value
    post.save()
    return HttpResponseRedirect('/')


def edit(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':

        form = PostForm(request.POST, request.FILES, instance=post)
    # if the form is valid
        if form.is_valid():

            # yes,save
            form.save()
        # Redirect to home
            return HttpResponseRedirect('/')

        else:

            # No, Show Error
            return HttpResponseRedirect(form.erros.as_json())

    return render(request, 'edit.html', {'post': post, })
