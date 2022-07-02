from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.update import UpdateView
from django.views.generic.delete import DeleteView
 
from .models import blog

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'list.html'


class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    success_urls = reverse_lazy('blog:all')
    template_name = 'base.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'


class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'
    success_urls = reverse_lazy('blog:all')
    template_name = 'update.html'


class PostDeleteView(DeleteView):
    model = Post
    fields = '__all__'
    success_urls = reverse_lazy('blog:all')
    template_name = 'delete.html'
