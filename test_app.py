mport pytest
from app import create_app
from urllib.parse import quoate

@pytest.fixture
def app():
    return create_app()

@pytest.fixture
def client(app):
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    expected_text = quote('Hello, world! This is a simple flask app 12333.')
    assert expected_text.encode() in response.data