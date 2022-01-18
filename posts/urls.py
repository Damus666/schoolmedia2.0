from django.urls import path
from .views import post_list, like_view, PostDeleteView, PostUpdateView

app_name = 'posts'

urlpatterns = [
    path('posts', post_list, name='main-post-view'),
    path('posts/like-post', like_view, name='like-post-view'),
    path('post/<pk>/delete-post',PostDeleteView.as_view(), name='post-delete'),
    path('post/<pk>/edit-post',PostUpdateView.as_view(), name='post-update'),
]