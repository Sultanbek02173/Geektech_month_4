from django.urls import path
from posts.views import hello, get_index, get_about, get_contacts, get_post, update_post, delete_post


urlpatterns = [
    path("hello/", hello, name = "hello-view"),    
    path("", get_index, name = "index-page"),
    path("conacts/", get_contacts, name = "contacts-view"),    
    path("about/", get_about, name = "about-view"),    
    path("post_creat/", get_post, name = "post-creat"),    
    path("update_post/", update_post, name = "update-post"),    
    path("delete_post/", delete_post, name = "delete_post"),    
]