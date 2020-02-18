from blog.models import Post
from django import template
register = template.Library()


@register.simple_tag(name='my_tag')
def total_posts():
    return Post.objects.count()


@register.inclusion_tag('blog/latest_posts123.html')
def show_latest_posts(count=3):
    latest_posts = Post.objects.order_by('-publish')[:count]
    return {'latest_posts':latest_posts}

from django.db.models import Count

@register.simple_tag #assignment_tag=simple_tag
def get_most_commented_posts(count=5):
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

# Django 1.4 added the assignment_tag helper to ease the creation of template tags that store results in a
 #template variable. The simple_tag() helper has gained this same ability,
 #making the assignment_tag obsolete. Tags that use assignment_tag should be updated to use simple_tag.
