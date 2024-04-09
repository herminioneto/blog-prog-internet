from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from blog.models import Post


# showing all posts
def main_page(request):
    posts = Post.objects.all()
    return render(request, "blog/components/main_page.html", {"posts": posts})


def post_detail(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return Http404("Post does not exist")

    return render(request, "blog/components/post_detail.html", {"post": post})


def delete_post(request, pk):
    print("Deletando post")
    try:
        Post.objects.filter(id=pk).delete()
    except Post.DoesNotExist:
        return Http404("Post with this id doesnt exits!")
    return redirect(reverse("main_page"))


def create_post(request):
    if request.method != "POST":
        return render(request, "blog/components/create_post.html")
    data = request.POST
    # Criando um novo post
    Post.objects.create(title=data["title"], content=data["content"])
    return redirect(reverse("main_page"))
