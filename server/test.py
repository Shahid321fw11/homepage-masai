import pytest
from app  import app


@pytest.fixture
def client():
    # Create a test client using your Flask application
    client = app.test_client()
    yield client

def test_home_endpoint(client):
    # Test the home endpoint
    response = client.get('/')
    assert response.status_code==200


def test_signup_positive(client):
    result=client.post('/signUp',json={
        'full_name':'tester111',
        'email':'tester111@gmail.com',
        'phone_number':'1234785657',
        'referral_code':'10111',
        'password':'aj@1234'
        
    })
    assert result.status_code==201
   

    

def test_signup_missing_name(client):
    result=client.post('/signUp',json={
        'full_name':'',
        'email':'tester2@gmail.com',
        'phone_number':'1234567891',
        'referral_code':'10111',
        'password':'1234567891'
        
    })
    assert result.status_code==400

def test_signup_missing_email(client):
    result=client.post('/signUp',json={
        'full_name':'tester3',
        'email':'',
        'phone_number':'1234567892',
        'referral_code':'10111',
        'password':'1234567892'
        
    })
    assert result.status_code==400

def test_signup_invalid_email_1(client):
    result=client.post('/signUp',json={
        'full_name':'tester4',
        'email':'tester4gmail.com',
        'phone_number':'1234567893',
        'referral_code':'10111',
        'password':'1234567893'
        
    })
    assert result.status_code==400


def test_signup_invalid_email_2(client):
    result=client.post('/signUp',json={
        'full_name':'tester5',
        'email':'tester5@gmail',
        'phone_number':'1234567894',
        'referral_code':'10111',
        'password':'1234567894'
        
    })
    assert result.status_code==400

def test_signup_invalid_phone(client):
    result=client.post('/signUp',json={
        'full_name':'tester6',
        'email':'tester6@gmail.com',
        'phone_number':'12345678',  #invalid number
        'referral_code':'10111',
        'password':'1234567895'
        
    })
    assert result.status_code==400


def test_signup_invalid_password(client):
    result=client.post('/signUp',json={
        'full_name':'tester7',
        'email':'tester7@gmail.com',
        'phone_number':'1234567895',
        'referral_code':'10111',
        'password':''
        
    })
    assert result.status_code==400

def test_signup_without_reffral(client):
    result=client.post('/signUp',json={
        'full_name':'tester12',
        'email':'tester8@gmail.com',
        'phone_number':'1234567897',
        'referral_code':'',
        'password':'1234567897'
        
    })
    assert result.status_code==201







