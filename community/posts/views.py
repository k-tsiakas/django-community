from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from braces.views import SelectRelatedMixin

from posts.models import Post
from posts import forms


from django.contrib.auth import get_user_model
User = get_user_model() # get current user logged in
# Create your views here.




class PostListView(SelectRelatedMixin,  ListView):
    model = Post
    select_related = ["user"]
    ordering = ['-date']
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.order_by('-date')

    def get_context_data(self,**kwargs):
        context = super(PostListView,self).get_context_data(**kwargs)
        context['header'] = 'All Posts'
        return context


class UserPostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        print(self.request.user)
        return Post.objects.filter(user=self.request.user).order_by('-date')

    def get_context_data(self,**kwargs):
        context = super(UserPostListView,self).get_context_data(**kwargs)
        context['header'] = 'My Posts'
        return context

class PostDetailView(SelectRelatedMixin, DetailView):
    model = Post
    select_related = ['user']
    template_name = 'posts/post_detail.html'

class PostCreateView(LoginRequiredMixin, SelectRelatedMixin, CreateView):
    model = Post
    template_name = 'posts/post_create_form.html'
    fields = ['title', 'content', 'file']

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'posts/post_update_form.html'
    fields = ['title', 'content', 'file']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, SelectRelatedMixin, DeleteView):
    model = Post
    select_related = ['user']
    success_url = reverse_lazy('posts:all')
    template_name = 'posts/post_delete.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)
