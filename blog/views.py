from django.shortcuts import render
from django.views import generic

from blog.models import Post


class PostListView(generic.ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'


def home(request):
    return render(request, 'base.html')
