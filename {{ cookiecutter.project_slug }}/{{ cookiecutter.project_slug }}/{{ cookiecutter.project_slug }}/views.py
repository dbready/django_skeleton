from django.conf import settings
from django.http.response import JsonResponse


def commit(request) -> JsonResponse:
    commit_id = getattr(settings, "COMMIT_ID", "")
    return JsonResponse({"commit_id": commit_id})


def health(request) -> JsonResponse:
    return JsonResponse({"status": "OK"})
