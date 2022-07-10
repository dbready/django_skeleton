from django.urls import reverse
from django.templatetags.static import static
from django.test import Client
import pytest


# based on advice from
# - https://evilmartians.com/chronicles/how-to-favicon-in-2021-six-files-that-fit-most-needs
# - https://www.leereamsnyder.com/blog/favicons-in-2021
@pytest.mark.parametrize(
    "icon_path",
    [
        "/favicon.ico",  # favicon must exist at root
        static("core/icon/android-icon-192x192.png"),
        static("core/icon/android-icon-512x512.png"),
        static("core/icon/apple-touch-icon.png"),
        static("core/icon/favicon.svg"),
    ],
)
def test_favicons(icon_path):
    c = Client()
    # expecting/allowing for redirects to handle django static assumptions
    resp = c.get(icon_path, follow=True)
    assert resp.status_code == 200


def test_android_favicon_manifest():
    manifest_url = reverse("manifest_webmanifest")
    c = Client()
    resp = c.get(manifest_url)
    assert resp.status_code == 200
    # confirm is parsable and contains icons
    data = resp.json()
    assert "icons" in data


def test_android_favicon_manifest_resources():
    # confirm the URLs in android manifest exist
    manifest_url = reverse("manifest_webmanifest")
    c = Client()
    resp = c.get(manifest_url)
    data = resp.json()
    for icon in data["icons"]:
        icon_url = icon["src"]
        resp = c.get(icon_url)
        assert resp.status_code == 200


def test_index(client):
    url = reverse("index")
    response = client.get(url)
    assert response.status_code == 200
