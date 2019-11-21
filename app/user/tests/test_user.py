import pytest
import requests
import json

# Create your tests here.
@pytest.mark.parametrize("email, password",[("user1@example.com","Test@123"),("user2@example.com","Test@123")])
def test_user_login_valid(supply_url, email, password):
	url = supply_url + "/users/login/"
	resp = requests.post(url, data={"email": email, "password": password})
	j = json.loads(resp.text)
	assert resp.status_code == 200
	assert j['data']['email'] == email

@pytest.mark.parametrize("email, password",[("user1@example.com","Test@123"),("user2@example.com","Test@123")])
def test_user_login_invalid_method(supply_url, email, password):
	url = supply_url + "/users/login/"
	resp = requests.get(url, data={"email": email, "password": password})
	j = json.loads(resp.text)
	assert resp.status_code == 405

@pytest.mark.parametrize("email, password",[("user1@example.com","Test@1234")])
def test_user_login_invalid_credentials(supply_url, email, password):
	url = supply_url + "/users/login/"
	resp = requests.post(url, data={"email": email, "password": password})
	j = json.loads(resp.text)
	assert resp.status_code == 400


def test_user_details_invalid(supply_url):
	url = supply_url + "/users/details/"
	resp = requests.get(url)
	j = json.loads(resp.text)
	assert resp.status_code == 401