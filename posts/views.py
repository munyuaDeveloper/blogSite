from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Post
from marketing.models import Signup


def index(request):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    if request.method == 'POST':
        email = request.POST['email']  # get the email from the foem
        new_signup = Signup()  # initialize signup model
        new_signup.email = email
        new_signup.save()

    context = {
        'posts': featured,
        'latest': latest,
    }
    return render(request, 'index.html', context)


def blog(request):
    post_list = Post.objects.all()
    most_recent = Post.objects.order_by('-timestamp')[:3]
    paginator = Paginator(post_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'posts_list': paginated_queryset,
        'page_request_var': page_request_var,
        'most_recent': most_recent
    }
    return render(request, 'blog.html', context)


def post(request, id):
    most_recent = Post.objects.order_by('-timestamp')[:3]
    post_details = Post.objects.get(id=id)
    context = {
        'post_details': post_details,
        'most_recent': most_recent
    }
    return render(request, 'post.html', context)
