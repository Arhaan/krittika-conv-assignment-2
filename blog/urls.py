from django.urls import path
from . import views


urlpatterns = [
    path("view_blog/", views.PostListView.as_view(), name="posts-list"),
    path("view_blog/<pk>", views.PostDetailsView.as_view(), name="posts-detail"),
    path("createBlog/", views.PostCreateView.as_view(), name="posts-create"),
]