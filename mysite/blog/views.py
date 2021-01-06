import json

from django.views.generic import (
    ListView,
    DetailView,
    FormView
)
from django.conf import settings
from django.db.models import Q
from django.urls import reverse_lazy
from django.shortcuts import render

from blog.models import Post, Category
from blog.forms import PostSearchForm


class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'

    def get_queryset(self):
        posts = Post.objects.all()
        for post in posts:
            post.jsonify_content()
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context


class PostDV(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_url = self.object.get_absolute_url()
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}-{self.object.slug}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{post_url}"
        context['disqus_title'] = f"{self.object.slug}"
        context['object'].content = json.dumps(context['object'].content)
        return context


class ObjectsByCategoryLV(ListView):
    template_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category__name=self.kwargs.get('category'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_name'] = self.kwargs['category']
        return context


class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        search_word = form.cleaned_data['search_word']
        post_list = Post.objects.filter(
                            Q(title__icontains=search_word) |
                            Q(description__icontains=search_word)).distinct()
        context = {}
        context['form'] = form
        context['search_term'] = search_word
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)
