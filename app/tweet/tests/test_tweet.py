import pytest
import requests
import json

# Create your tests here.
def test_tweet_list_without_cookie_invalid(supply_url):
	url = supply_url + "/feeds/"
	resp = requests.get(url)
	j = json.loads(resp.text)
	assert resp.status_code == 401

@pytest.mark.parametrize("id",["1"])
def test_tweet_detail_without_cookie_invalid(supply_url, id):
	url = supply_url + "/feeds/" + id
	resp = requests.get(url)
	j = json.loads(resp.text)
	assert resp.status_code == 401
