from django.http import JsonResponse
from django.shortcuts import render
from django.templatetags.static import static
from django.views.decorators.cache import cache_page


def error_bad_request(request, exception):
    return render(request, "core/error/400.html", {}, status=400)


def error_permission_denied(request, exception=None):
    return render(request, "core/error/403.html", {}, status=403)


def error_page_not_found(request, exception=None):
    return render(request, "core/error/404.html", {}, status=404)


def error_server(request, exception=None):
    return render(request, "core/error/500.html", {}, status=500)


@cache_page(60 * 30)
def manifest_webmanifest(request):
    """Android manifest.webmanifest definition for holding favorite icons"""
    context = {
        "icons": [
            {
                "src": static("core/favicon/android-icon-192x192.png"),
                "type": "image/png",
                "sizes": "192x192",
            },
            {
                "src": static("core/favicon/android-icon-512x512.png"),
                "type": "image/png",
                "sizes": "512x512",
            },
        ]
    }
    return JsonResponse(context)


def index(request):
    context = {}
    return render(request, "core/index.html", context)
