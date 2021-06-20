from django.urls import path
from . import views

urlpatterns = [
    path('' , views.bloghome , name="bloghome"),
    path('<int:slug>/' , views.blogpost , name="blogpost"),
    path('postcomment/' , views.postcomment , name="postcomment")
]
