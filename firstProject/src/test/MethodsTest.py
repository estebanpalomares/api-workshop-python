import unittest

from src.main.rest.request import MethodsRequest


class TestMethods(unittest.TestCase):

    def test_get_method(self):
        payload = {"method": "GET", "name": "Jhon", "lastname": "Doe", "age": 33}
        response = MethodsRequest.GET_method(payload)
        print(response.json())
        assert response.status_code == 200

    def test_post_method(self):
        payload = {"method": "POST", "name": "Jhon", "lastname": "Doe", "age": 33}
        response = MethodsRequest.POST_method(payload)
        print(response.json())
        assert response.status_code == 200

    def test_patch_method(self):
        payload = {"method": "PATH", "name": "Jhon", "lastname": "Doe", "age": 33}
        response = MethodsRequest.PATCH_method(payload)
        print(response.json())
        assert response.status_code == 200

    def test_put_method(self):
        payload = {"method": "PUT", "name": "Jhon", "lastname": "Doe", "age": 33}
        response = MethodsRequest.PUT_method(payload)
        print(response.json())
        assert response.status_code == 200

    def test_delete_method(self):
        payload = {"method": "DELETE", "name": "Jhon", "lastname": "Doe", "age": 33}
        response = MethodsRequest.DELETE_method(payload)
        print(response.json())
        assert response.status_code == 200
