from django.shortcuts import render

from blog.models import Post

# showing all posts
def main_page(request):
    posts = Post.objects.all()
    return render(request, "blog/components/main_page.html", {"posts": posts})
    