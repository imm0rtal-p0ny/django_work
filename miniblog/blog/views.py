from django.urls import reverse_lazy
from .models import Post
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .forms import PostForm


class PostList(ListView):
    template_name = 'post_list.html'
    model = Post


class CreatePost(CreateView):
    template_name = 'create_post.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('home')


class UpdatePost(UpdateView):
    template_name = 'create_post.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('home')


class DetailPost(DetailView):
    template_name = 'detail_post.html'
    model = Post


class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy('home')


