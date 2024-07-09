import django.contrib.auth as auth
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.urls import reverse

from blog.models import Author, Post


# showing all posts
@login_required
def main_page(request):
    posts = Post.objects.order_by("-created_at").all()
    return render(
        request,
        "blog/components/main_page.html",
        {"posts": posts},
    )


# Mostrando um post só, com detalhes
@login_required
def post_detail(request, pk):

    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return Http404("Post does not exist")

    author = request.user.author
    return render(
        request,
        "blog/components/post_detail.html",
        {
            "post": post,
            "author": author,
        },
    )


@login_required
def delete_post(request, pk):
    print("Deletando post")
    try:
        toBeDeleted = Post.objects.filter(id=pk).first()
        toBeDeleted.image.delete()
        toBeDeleted.delete()
    except Post.DoesNotExist:
        return Http404("Post with this id doesnt exits!")
    return redirect(reverse("main_page"))


@login_required
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
        owner=request.user.author,
    )
    post.save()
    return redirect(reverse("main_page"))


# Cria um autor e assosia as credenciais dele
def sign_up(request):
    match request.method:
        case "GET":
            return render(request, "blog/components/signup.html")

        case "POST":
            data = request.POST
            if not data:
                return HttpResponseBadRequest()
            user = User(
                username=data["username"],
            )
            fullname: str = data["full_name"]
            user.first_name, user.last_name = fullname.split(" ")[:2]
            user.set_password(data["password"])
            user.is_active = False
            user.save()
            Author.objects.create(user=user, bio="")
            # TODO: Redirecionar para a página de detalhes do autor
            return redirect(reverse("main_page"))


def login(request):
    match request.method:
        case "GET":
            return render(request, "blog/components/login.html")

        case "POST":
            data = request.POST
            if not data:
                return HttpResponseBadRequest()
            user = authenticate(username=data["username"], password=data["password"])
            if not user:
                return render(request, "blog/components/login.html")
            auth.login(request, user)

            # TODO: Redirecionar para a página de detalhes do autor
            return render(request, "blog/components/main_page.html")


def logout_view(request):
    logout(request)
    return redirect(reverse("login"))
