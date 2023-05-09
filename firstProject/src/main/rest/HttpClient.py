import json

import requests


class RestMethods:

    @staticmethod
    def get_method(url, payload, headers):
        response = requests.get(url, data=json.dumps(payload), headers=headers)

        return response

    @staticmethod
    def post_method(url, payload, headers):
        response = requests.post(url, data=json.dumps(payload), headers=headers)

        return response

    @staticmethod
    def put_method(url, payload, headers):
        response = requests.put(url, data=json.dumps(payload), headers=headers)

        return response

    @staticmethod
    def patch_method(url, payload, headers):
        response = requests.patch(url, data=json.dumps(payload), headers=headers)

        return response

    @staticmethod
    def delete_method(url, payload, headers):
        response = requests.delete(url, data=json.dumps(payload), headers=headers)

        return response
