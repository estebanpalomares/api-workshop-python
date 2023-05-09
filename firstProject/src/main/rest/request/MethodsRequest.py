from src.main.rest import HttpClient

baseUrl = 'https://www.httpbin.org/anything'
headers = {"Content-Type": "application/json", "Accept": "application/json"}


def GET_method(payload):
    response = HttpClient.RestMethods.get_method(baseUrl, payload, headers)
    return response


def POST_method(payload):
    response = HttpClient.RestMethods.post_method(baseUrl, payload, headers)
    return response


def PATCH_method(payload):
    response = HttpClient.RestMethods.patch_method(baseUrl, payload, headers)
    return response


def PUT_method(payload):
    response = HttpClient.RestMethods.put_method(baseUrl, payload, headers)
    return response


def DELETE_method(payload):
    response = HttpClient.RestMethods.delete_method(baseUrl, payload, headers)
    return response
