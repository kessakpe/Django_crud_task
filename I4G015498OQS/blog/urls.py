from django.urls import path
from .views import PostCreateView, PostListView





urlpatterns = [
    path('list/', views.PostListView.as_view(), name='all'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('delete/<slug:slug>', views.PostDeleteView.as_view(), name='post_delete'),
    path('update/<slug:slug>', views.PostUpdateView.as_view(), name='post_update'),
    path('detail/<slug:slug>', views.PostDetailView.as_view(), name='post_detail'),
]