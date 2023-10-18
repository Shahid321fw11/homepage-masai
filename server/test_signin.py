import pytest
from app  import app


@pytest.fixture
def client():
    # Create a test client using your Flask application
    client = app.test_client()
    yield client

def test_sigin_email_positive(client):
    result=client.post('/signIn',json={
        
        'identifier':'tester111@gmail.com',
        
        'password':'aj@1234'
        
      })
    assert result.status_code==200

# def test_sigin_phone_positive(client):
#     result=client.post('/signIn',json={
        
#         'phone_number':'1234785657',
        
#         'password':'aj@1234'
        
#       })
#     assert result.status_code==200

def test_sigin_phone_missing(client):
    result=client.post('/signIn',json={
        
        'phone_number':'',
        
        'password':'aj@1234'
        
      })
    assert result.status_code==401


def test_sigin_phone_password(client):
    result=client.post('/signIn',json={
        
        'phone_number':'1234785657',
        
        'password':''
        
      })
    assert result.status_code==401