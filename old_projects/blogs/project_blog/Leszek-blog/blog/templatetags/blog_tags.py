from django import template
from django.db.models import Count
register = template.Library() #var is needed to register own filters and template tags

from ..models import Post

@register.simple_tag # (s_t) is helper function - method of template.Library
def total_posts():
    '''Function (s_t) defines tag 'total_posts'.'''
    return Post.published.count()
    
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    '''Function (i_t) defines tag 'show-latest-post'.'''
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}
    
@register.assignment_tag
def get_most_commented_posts(count=5):
    '''Function (a_t) defines tag 'get_most_commented_posts'.'''
    return Post.published.annotate(
        total_comments=Count('comments')).order_by('-total_comments')[:count]