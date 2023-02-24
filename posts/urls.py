from django.urls import path
from posts.views import hello, get_index, get_about, get_contacts


urlpatterns = [
    path("hello/", hello, name = "hello-view"),    
    path("", get_index, name = "index-page"),
    path("conacts/", get_contacts, name = "contacts-view"),    
    path("about/", get_about, name = "about-view"),    
]