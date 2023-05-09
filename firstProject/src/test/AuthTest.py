import json
import unittest

from src.main.rest.request import AuthRequest


class AuthMethods(unittest.TestCase):

    def test_req_with_auth(self):
        payload = {"method": "GET", "name": "Jhon", "lastname": "Doe", "age": 33}
        response = AuthRequest.req_with_auth(payload)
        response_json = response.json()
        objecttokenNumber = response_json['authenticated']
        print(response.json())
        assert objecttokenNumber == True
        assert response.status_code == 200

    def test_req_no_auth(self):
        payload = {"method": "GET", "name": "Jhon", "lastname": "Doe", "age": 33}
        response = AuthRequest.req_no_auth(payload)
        assert response.status_code == 401
