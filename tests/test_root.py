from tests import client


def test_landing(client):
    landing = client.get("/")
    html = landing.data.decode()

    assert "<a class=\"social-link\" href=\"https://www.linkedin.com/in/colin-skow/\" aria-label=\"linkedin\">" in html
    assert "<a href=\"https://www.github.com/skow0020\" aria-label=\"github\">" in html

    assert landing.status_code == 200


def test_landing_stats(client):
    landing = client.get("/#stats")
    assert landing.status_code == 200


def test_landing_about(client):
    landing = client.get("/#about")
    assert landing.status_code == 200


def test_landing_work(client):
    landing = client.get("/#work")
    assert landing.status_code == 200


def test_landing_quotes(client):
    landing = client.get("/#quotes")
    assert landing.status_code == 200


def test_landing_contact(client):
    landing = client.get("/#contact")
    assert landing.status_code == 200


def test_landing_fail(client):
    landing = client.get("/asdf")
    assert landing.status_code == 404
