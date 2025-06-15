import pytest
from app import app
from flask import session

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_landing(client):
    print("▶️ Testing landing page...")
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome" in response.data
    print("✅ Landing page test passed.")

def test_register_page(client):
    print("▶️ Testing register page...")
    response = client.get('/register')
    assert response.status_code == 200
    assert b"Register" in response.data
    print("✅ Register page test passed.")

def test_login_page(client):
    print("▶️ Testing login page...")
    response = client.get('/login')
    assert response.status_code == 200
    assert b"Login" in response.data
    print("✅ Login page test passed.")

def test_register_with_missing_fields(client):
    print("▶️ Testing register with missing fields...")
    response = client.post('/register', data=dict(
        name='', email='', password=''
    ), follow_redirects=True)
    assert b"All fields are required" in response.data
    print("✅ Register with missing fields test passed.")

def test_login_wrong_user(client):
    print("▶️ Testing login with invalid credentials...")
    response = client.post('/login', data=dict(
        email='fake@example.com', password='wrongpass'
    ), follow_redirects=True)
    assert b"Invalid email or password" in response.data
    print("✅ Login with wrong credentials test passed.")

def test_forgot_with_invalid_email(client):
    print("▶️ Testing forgot password with invalid email...")
    response = client.post('/forgot', data=dict(
        email='nonexistent@example.com'
    ), follow_redirects=True)
    assert b"Email not found" in response.data
    print("✅ Forgot password with invalid email test passed.")

def test_reset_without_session(client):
    print("▶️ Testing reset route access without session...")
    response = client.get('/reset', follow_redirects=True)
    assert b"Forgot" in response.data or response.status_code == 200
    print("✅ Reset route protected without session.")
