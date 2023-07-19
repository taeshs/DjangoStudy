from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404

from blog.models import Post


# Create your views here.

def post_list(request):
    post_list = Post.published.all()
    per_page = request.GET.get('per_page', 5)
    paginator = Paginator(post_list, per_page)
    page_number = request.GET.get('page')
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("No Post found.")
    # return render(request,
    #               'blog/post/detail.html'
    #               , {'post': post})
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})



