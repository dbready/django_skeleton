from django.urls import reverse


def test_health_check(client):
    resp = client.get(reverse("zhealth"))
    assert resp.status_code == 200
