from django.shortcuts import render, redirect
from .models import *
from .utils import check_read_articles, check_ratings
# Create your views here.


def home_page(request):
    categories = Category.objects.all()
    posts = Post.objects.all()

    data = {
        'categories' : categories,
        'posts' : posts
    }

    return render(request=request, template_name='index.html', context=data)


def detail_view(request, pk):
    categories = Category.objects.all()
    post = Post.objects.get(id=pk)

    request.session.modified = True

    if post.id in check_read_articles(request):
        pass
    else:
        check_read_articles(request).append(post.id)
        post.views += 1
        post.save()

    if request.method == 'POST':
        name = request.POST.get('name')
        comment = request.POST.get('comment')
        if all([name, comment]):
            Comment.objects.create(
                author=name,
                comment=comment,
                post=post
            )

    return render(request, 'detail.html', context={'post': post, 'categories' : categories})


def set_rating(request, value, id):
    post = Post.objects.get(pk=id)
    value = int(value)

    request.session.modified = True

    if post.id in check_ratings(request):
        pass
    else:
        check_ratings(request).append(post.id)
        post.views += 1
        post.save()

    if all([post, value]):
        Rating.objects.create(
            post=post,
            value=value
        )
        return redirect('/')