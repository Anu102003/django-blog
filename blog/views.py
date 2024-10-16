from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
import logging
from .models import Post,AboutUs
from django.core.paginator import Paginator
from .form import ContactForm

# static demo data
# post = [
#     {"id": 1, "title": "Post 1", "content": "Content of Post 1"},
#     {"id": 2, "title": "Post 2", "content": "Content of Post 2"},
#     {"id": 3, "title": "Post 3", "content": "Content of Post 3"},
#     {"id": 4, "title": "Post 4", "content": "Content of Post 4"},
#     {"id": 5, "title": "Post 5", "content": "Content of Post 5"},
# ]

# Create your views here.
# def index(request):
#     return HttpResponse("Hlo World, You at blog's index")


def index(request):
    blog_title = "Latest Post of Index Page"
    all_post = Post.objects.all()
    
    paginator=Paginator(all_post,3)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request, "blog/index.html", {"blog_title": blog_title, "page_obj": page_obj})


# def details(request,post_id):
#     return HttpResponse(f"You are viewing post detail page, POST ID: {post_id}")


def details(request, slug):

    # static data
    # postData = next((item for item in post if item["id"] == int(post_id)), None)

    # logging
    # logger = logging.getLogger("Testing")
    # logger.debug(f'post variable {postData}')

    try:
        postData = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category=postData.category).exclude(pk=postData.id)
    except Post.DoesNotExist:
        raise Http404("Post id does not match")

    return render(request, "blog/details.html", {"postData": postData,"related_posts":related_posts})


# def old_url(request):
#     return redirect("new_url")


def old_url(request):
    return redirect(reverse("blog:new_page_url"))


def new_url(request):
    return HttpResponse("This is new Url")

def contact_view(request):
    if request.method=="POST":
        
        form=ContactForm(request.POST)
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        
        logger = logging.getLogger("Testing")
        
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            logger.debug(f'post variable name: {name}, email: {email}, message: {message}')
            success_message='Your Email has beed send'
            return render(request,"blog/contact.html",{"form":form,"success_message":success_message})
        else:
            logger.debug('Form validation failure')
        return render(request,"blog/contact.html",{'form':form,'name':name,'email':email,'message':message})
    return render(request,"blog/contact.html")

def about_view(request):
    about_content=AboutUs.objects.first().content
    return render(request,"blog/about.html",{'about_content':about_content})