import unittest
from src.main.rest.methods import MethodsRequest


class TestMethods(unittest.TestCase):

    def test_get_method(self):
        response = MethodsRequest.GET_method()
        assert response.status_code == 200

    def test_post_method(self):
        response = MethodsRequest.POST_method()
        assert response.status_code == 200

    def test_patch_method(self):
        response = MethodsRequest.PATCH_method()
        assert response.status_code == 200

    def test_put_method(self):
        response = MethodsRequest.PUT_method()
        assert response.status_code == 200

    def test_delete_method(self):
        response = MethodsRequest.DELETE_method()
        assert response.status_code == 200
