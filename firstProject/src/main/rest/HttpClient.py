import requests


class RestMethods:

    @staticmethod
    def get_method(url):
        response = requests.get(url)

        return response

    @staticmethod
    def post_method(url):
        response = requests.post(url)

        return response

    @staticmethod
    def put_method(url):
        response = requests.put(url)

        return response

    @staticmethod
    def patch_method(url):
        response = requests.patch(url)

        return response

    @staticmethod
    def delete_method(url):
        response = requests.delete(url)

        return response
