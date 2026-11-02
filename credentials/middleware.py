from django.shortcuts import redirect
from django.contrib import messages


class CustomAuthenticationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Pages that do not require login
        public_paths = [
            "/cred/login/",
            "/cred/register/",
            "/admin/",
            "/"
        ]

        # Check whether the requested page is public
        if request.path not in public_paths:

            # Check whether the user is logged in
            if not request.user.is_authenticated:
                messages.error(
                    request,
                    "Please log in to access this page."
                )
                return redirect("/cred/login/")

        response = self.get_response(request)
        return response