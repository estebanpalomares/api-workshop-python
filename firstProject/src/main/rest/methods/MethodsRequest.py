from src.main.rest import HttpClient

baseUrl = 'https://www.httpbin.org/'


def GET_method():
    response = HttpClient.RestMethods.get_method(baseUrl + '/get')
    return response


def POST_method():
    response = HttpClient.RestMethods.post_method(baseUrl + '/post')
    return response


def PATCH_method():
    response = HttpClient.RestMethods.patch_method(baseUrl + '/patch')
    return response


def PUT_method():
    response = HttpClient.RestMethods.put_method(baseUrl + '/put')
    return response


def DELETE_method():
    response = HttpClient.RestMethods.delete_method(baseUrl + '/delete')
    return response
