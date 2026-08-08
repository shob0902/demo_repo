import pytest

from app import app, users

VALID_EMAIL = "person@example.com"
# 10 chars, letter + digit -- deliberately still valid if a password-strength
# rule gets added later, so an additive change can't turn this suite red.
VALID_PASSWORD = "hunter2024"


@pytest.fixture
def client():
    users.clear()
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


def test_signup_accepts_valid_email(client):
    resp = client.post("/signup", json={"email": VALID_EMAIL, "password": VALID_PASSWORD})
    assert resp.status_code == 201


def test_signup_rejects_invalid_email(client):
    resp = client.post("/signup", json={"email": "not-an-email", "password": VALID_PASSWORD})
    assert resp.status_code == 400


def test_signup_rejects_missing_password(client):
    resp = client.post("/signup", json={"email": VALID_EMAIL})
    assert resp.status_code == 400


def test_signup_rejects_empty_password(client):
    resp = client.post("/signup", json={"email": VALID_EMAIL, "password": ""})
    assert resp.status_code == 400


def test_list_users_returns_registered_emails(client):
    client.post("/signup", json={"email": VALID_EMAIL, "password": VALID_PASSWORD})
    resp = client.get("/users")
    assert resp.status_code == 200
    assert VALID_EMAIL in resp.get_json()["users"]
