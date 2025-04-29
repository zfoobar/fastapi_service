from fastapi.testclient import TestClient
from main import app
import requests
import pytest
import os

client = TestClient(app)

if 'AUTH_KEY' not in os.environ:
    pytest.exit("You need to set AUTH_KEY environment variable.")
else:
    auth_token = os.environ['AUTH_KEY']

# Gandalf's quote should show up in Gandalf's list of quotes
def test_existent_quote():
    our_response = client.get("/quote/random/Gandalf")
    data = our_response.json()['data']
    url = "https://the-one-api.dev/v2/character/5cd99d4bde30eff6ebccfea0/quote"

    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

    their_response = requests.get(url,headers=headers)
    payload = their_response.json()['docs']
    quotes = [p['dialog'] for p in payload]
    assert data in quotes
    assert our_response.status_code == 200

# Suaron's quote should not show up in Gandalf's quotes
def test_non_existing_quote():
    our_response = client.get("/quote/random/Sauron")
    data = our_response.json()['data']
    url = "https://the-one-api.dev/v2/character/5cd99d4bde30eff6ebccfea0/quote"

    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

    their_response = requests.get(url,headers=headers)
    payload = their_response.json()['docs']
    quotes = [p['dialog'] for p in payload]
    assert data not in quotes
    assert our_response.status_code == 200
