from typing import Any

from django.shortcuts import redirect
from django.urls import reverse


class LoginRequiredMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request) -> Any:
        non_required_login_paths = [reverse("login"), reverse("sign_up")]
        if request.path.startswith(any(non_required_login_paths)):
            return self.get_response(request)
        if not request.user.is_authenticated:
            if not request.path.startswith(
                reverse("admin:login")
            ) and not request.path.startswith(reverse("sign_up")):
                return redirect(reverse("sign_up"))
        response = self.get_response(request)
        return response
