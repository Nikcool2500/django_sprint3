from django.shortcuts import get_object_or_404, render
from .models import Post, Category
from django.utils import timezone


def index(request):
    post_list = Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    ).select_related(
        'author', 'location', 'category'
    ).order_by('-pub_date')[:5]
    template = 'blog/index.html'
    context = {"post_list": post_list}
    return render(request, template, context)


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.select_related('author', 'location', 'category'),
        pk=post_id,
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )

    template = 'blog/detail.html'
    context = {"post": post}
    return render(request, template, context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    
    post_list = Post.objects.filter(
        category=category,
        pub_date__lte=timezone.now(),
        is_published=True
    ).select_related(
        'author', 'location', 'category'
    ).order_by('-pub_date')

    template = 'blog/category.html'
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)
