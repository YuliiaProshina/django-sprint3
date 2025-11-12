from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Category, Post


VISIBLE_POSTS_NUMBER = 5


def get_posts_queryset():
    """Возвращает базовый QuerySet опубликованных постов с нужными связями."""
    return (
        Post.objects.select_related('category')
        .filter(is_published=True, pub_date__lte=timezone.now(),
                category__is_published=True)
    )


def index(request):
    """Рендеринг главной страницы."""
    post_list = get_posts_queryset().order_by(
        '-pub_date')[:VISIBLE_POSTS_NUMBER]
    context = {
        'post_list': post_list
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """Рендеринг страницы статьи."""
    post = get_object_or_404(
        get_posts_queryset(),
        pk=post_id
    )
    context = {
        'post': post
    }
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """Рендеринг статьи по категории."""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = get_posts_queryset().filter(
        category=category.id).order_by('-pub_date')

    context = {
        'category': category,
        'post_list': posts
    }
    return render(request, 'blog/category.html', context)
