from email.mime import image

from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from blog.models import Post
from config import settings


# showing all posts
def main_page(request):
    posts = Post.objects.order_by("-created_at").all()
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
        toBeDeleted = Post.objects.filter(id=pk).first()
        toBeDeleted.image.delete()
        toBeDeleted.delete()
    except Post.DoesNotExist:
        return Http404("Post with this id doesnt exits!")
    return redirect(reverse("main_page"))


def create_post(request):
    if request.method != "POST":
        return render(request, "blog/components/create_post.html")
    data = request.POST

    # Criando um novo post
    cover_image = request.FILES.get("image")
    post = Post(
        title=data["title"],
        content=data["content"],
        image=cover_image,
    )
    post.save()
    return redirect(reverse("main_page"))
