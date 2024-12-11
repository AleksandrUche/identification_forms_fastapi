from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

URL = "/get_form"
HEADERS = {'content-type': 'application/x-www-form-urlencoded'}


def test_valid_data_order_form():
    data = {
        "user_email": "test@example.com",
        "user_phone": "+7 123 456 78 90",
        "order_date": "2024-12-01"
    }
    response = client.post(URL, data=data, headers=HEADERS)
    assert response.status_code == 200
    assert response.json() == {"template_name": "Order Form"}


def test_valid_data_order_form_many_fields():
    data = {
        "user_email": "test@example.com",
        "user_phone": "+7 123 456 78 90",
        "text": "test text",
        "description": 'test description',
        "order_date": "2024-12-01"
    }
    response = client.post(URL, data=data, headers=HEADERS)
    assert response.status_code == 200
    assert response.json() == {"template_name": "Order Form"}


def test_valid_data_registration_form():
    data = {
        "email": "test@example.com",
        "phone": "+7 123 456 78 90",
    }
    response = client.post(URL, data=data, headers=HEADERS)
    assert response.status_code == 200
    assert response.json() == {"template_name": "Registration Form"}


def test_valid_data_registration_form_many_fields():
    data = {
        "email": "test@example.com",
        "phone": "+7 123 456 78 90",
        "text": "test text",
        "description": 'test description'
    }
    response = client.post(URL, data=data, headers=HEADERS)
    assert response.status_code == 200
    assert response.json() == {"template_name": "Registration Form"}


def test_not_valid_data_1():
    data = {
        "email": "not_email",
        "phone": "+7 123 45",
        "random_field": "hello world"
    }
    response = client.post(URL, data=data, headers=HEADERS)
    assert response.status_code == 200
    assert response.json() == {"email": "text", "phone": "text", "random_field": "text"}


def test_not_valid_data_2():
    data = {
        "email": "test@mail.ru",
        "phone": "+7 123 45",
        "random_field": "hello world"
    }
    response = client.post(URL, data=data, headers=HEADERS)
    assert response.status_code == 200
    assert response.json() == {
        "email": "email", "phone": "text", "random_field": "text"
    }


def test_not_valid_data_3():
    data = {
        "email": "test_",
        "phone": "+7 123 455 55 55",
        "random_field": "hello world"
    }
    response = client.post(URL, data=data, headers=HEADERS)
    assert response.status_code == 200
    assert response.json() == {
        "email": "text", "phone": "phone", "random_field": "text"
    }


def test_not_valid_data_4():
    data = {'dd': 'dd'}
    response = client.post(URL, data=data, headers=HEADERS)
    assert response.status_code == 200
    assert response.json() == {"dd": "text"}
