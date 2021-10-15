import pytest
from app import create_app


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client

def test_word_occurrences_get(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Website Word Occurrence Counter" in response.data

def test_word_occurrences_post_correct_url(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is is posted to (POST)
    THEN check that the response is valid
    """
    response = test_client.post('/', data=dict(url='http://www.bbc.co.uk'))
    assert response.status_code == 200
    assert b"Words" in response.data
    assert b"Occurrences" in response.data

def test_word_occurrences_post_incorrect_url(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is is posted to (POST)
    THEN check that the response is valid
    """
    response = test_client.post('/', data=dict(url='www.bbc.co.uk'))
    assert response.status_code == 200
    assert b"No schema supplied. Perhaps you meant" in response.data