from django.shortcuts import render
from .forms import BlogPostForm, BlogForm
from .models import BlogCategory, BlogPost
from django.views.generic import CreateView, UpdateView, FormView, DeleteView, DetailView, ListView
from django.utils.text import slugify
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
import json


def test(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)

    return render(request, 'blog/test.html', {})


class CreateBlog(LoginRequiredMixin, CreateView):
    form_class = BlogForm
    template_name = 'blog/create_blog.html'
    success_url = 'home'

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.owner = self.request.user
        blog_obj.slug = slugify(blog_obj.title)

        blog_obj.save()
        messages.success(self.request, '%s, You have successfully created your blog.' % (self.request.user.username))
        return HttpResponseRedirect(reverse('home'))

    def form_invalid(self, form):
        print(form.errors)


class ListBlog(LoginRequiredMixin, ListView):
    model = BlogCategory
    template_name = 'blog/list_blog.html'

    def get_queryset(self):
        qs = BlogCategory.objects.filter(Q(owner=self.request.user))
        return qs


class UpdateBlog(LoginRequiredMixin, UpdateView):
    model = BlogCategory
    fields = ['title', 'category']
    template_name = 'blog/update_blog.html'
    success_url = 'home'

    def get_queryset(self):
        queryset = super(UpdateBlog, self).get_queryset()
        return queryset.filter(owner=self.request.user)

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.owner = self.request.user
        blog_obj.slug = slugify(blog_obj.title)

        blog_obj.save()
        messages.success(self.request, '%s, You have successfully updated your blog.' % (self.request.user.username))
        return HttpResponseRedirect(reverse('blog:list-blog'))

    def form_invalid(self, form):
        print(form.errors)


class DeleteBlog(DeleteView):
    pass


class UpdateBlogPost(UpdateView):
    model = BlogPost
    fields = ['title', 'body', 'blog_image']
    template_name = 'blog/update_blog_post.html'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, '%s, You have successfully Inserted an entry in your blog.'
                         % (self.request.user.username))
        return HttpResponseRedirect(reverse('blog:list-blog'))


class ListBlogPost(ListView):
    pass


class CreateBlogPost(CreateView):
    model = BlogPost
    fields = ['title', 'body', 'blog_image']
    template_name = 'blog/create_blog_post.html'
    success_url = 'home'

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        related_blog = BlogCategory.objects.get(slug=self.kwargs['blog'])
        blog_obj.blog = related_blog

        blog_obj.save()
        messages.success(self.request, '%s, You have successfully Inserted an entry in your blog.'
                         % (self.request.user.username))
        return HttpResponseRedirect(reverse('blog:list-blog'))

    def get_context_data(self, **kwargs):
        ctx = super(CreateBlogPost, self).get_context_data(**kwargs)
        ctx['related_blog'] = BlogCategory.objects.get(slug=self.kwargs['blog'])
        return ctx


class DetailBlog(DetailView):
    model = BlogCategory
    template_name = 'blog/detail_blog.html'


class DeleteBlogPost(DeleteView):
    pass


class DetailBlogPost(DetailView):
    pass
