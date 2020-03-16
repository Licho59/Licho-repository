from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count

from .models import Post, Comment
from .forms import EmailPostForm, CommentForm

def post_share(request, post_id):
    '''View to manage the posts' form and after checking it to send as an email; taking post according to its idenification number.'''
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    
    if request.method == 'POST': 
        form = EmailPostForm(request.POST) # form has been dispatched
        if form.is_valid():
            cd = form.cleaned_data # after checking email can be sent, attr. 'cleaned_data' is a dictionary with form's fields and values
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) invites to reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read the post "{} on website {}\n\n Comment added by {}: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'lesadmin@myblog.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,
                                                         'form': form})
             
                    
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

def post_list(request, tag_slug=None):
    '''View for list of posts.''' 
    object_list = Post.published.all()
    tag = None
    
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list, 3) # three posts on every page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1) # first page if variable page not integer
    except EmptyPage:
        posts = paginator.page(paginator.num_pages) # last page if variable page bigger than number of last page
    # request - demand for webpage path - address, page template, variables to generate in template
    return render(request,
                'blog/post/list.html', 
                {'page': page, 'posts': posts, 'tag': tag}) 
                          
def post_detail(request, year, month, day, post):
    '''View for singular post.'''
    post = get_object_or_404(Post, slug=post,
                                    status='published',
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day)
                                    
    # List of active comments for individual post.
    comments = post.comments.filter(active=True)
    
    if request.method == 'POST':
        # Comment has been published.
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Comment object created but not saved yet in database.
            new_comment = comment_form.save(commit=False)
            # New comment assigned to current post.
            new_comment.post = post
            # Comment saved in database.
            new_comment.save()
    else:
        comment_form = CommentForm
    
    # List of similar posts.
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]                    
    return render(request, 
                'blog/post/detail.html',
                {'post': post, 'comments': comments, 'comment_form': comment_form, 'similar_post': similar_posts})   