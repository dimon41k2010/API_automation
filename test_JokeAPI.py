import requests
import json
import pytest

url = "https://api.jokes.one/jod/categories"
# params_data = open("params.json", "r").read()

try:
    response = requests.get(url, timeout=1)
    json = response.json()

except requests.exceptions.RequestException as e:
    print(e)
    print("Error: Your URL is invalid")

@pytest.mark.smoke
def test_status_code_200():
    assert response.status_code, 200
    print("test_status_code_200 is passed")

@pytest.mark.smoke
def test_header_if_application_json():
    expected = "application/json; charset=utf-8"
    actual = response.headers["Content-Type"]
    assert actual, expected
    print("test_header_if_application_json is passed")

@pytest.mark.regression
def test_availability_contents_in_response_body():
    key = 'contents'
    actual = key in json.keys()
    assert actual == True
    print("test_contents_jsonForm is passed")

@pytest.mark.regression
def test_availability_success_in_response_body():
    key = "success"
    actual = key in json.keys()
    assert actual
    print("test_availability_success_in_response_body is completed")

@pytest.mark.regression
def test_category_jod_in_responce_body():
    actual = json['contents']["categories"][0]["name"]
    expected = "jod"
    assert actual, expected
    print("test_category_jod_in_responce_body is passed")

@pytest.mark.regression
def test_total_number_of_categories():
    actual = len(json["contents"]["categories"])
    expected = int(json["success"]["total"])
    assert actual, expected
    print("test_total_number_of_categories is completed")

@pytest.mark.smoke
def test_description_isString():
    actual = type(json["contents"]["categories"][0]["description"])
    expected = type('')
    assert actual, expected
    print("test_description_isString is completed")