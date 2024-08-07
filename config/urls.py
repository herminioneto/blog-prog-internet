"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from blog import views

app_name = "blog"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", views.sign_up, name="sign_up"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout_view),
    path("", views.main_page, name="main_page"),
    path("post/<pk>/", views.post_detail, name="post_detail"),
    path("post/delete/<pk>/", views.delete_post, name="delete_post"),
    path("post/create", views.create_post, name="create_post"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
