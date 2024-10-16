from django.urls import path
from . import views

app_name="blog"

urlpatterns=[
    path("",views.index,name="index"),
    
    # path("post/<int:post_id>",views.details,name="details")
    path("post/<str:slug>",views.details,name="details"),

    path("old_url",views.old_url,name="old_url"),
    # path("new_url>",views.new_url,name="new_url"),
    path("contact",views.contact_view,name="contact"),
    path("about",views.about_view,name="about"),
    path("new_something_url",views.new_url,name="new_page_url"),

]