from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from blog.models import Post


# Create your views here.

def post_list(request):
    post_list = Post.published.all()
    per_page = request.GET.get('per_page', 5)
    paginator = Paginator(post_list, per_page)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)
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



