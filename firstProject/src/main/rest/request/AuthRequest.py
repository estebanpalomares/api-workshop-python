from src.main.rest import HttpClient

baseUrl = 'https://www.httpbin.org/bearer'
headers = {"Content-Type": "application/json", "Accept": "application/json"}


def req_with_auth(payload):
    headers["Authorization"] = "Bearer token"
    response = HttpClient.RestMethods.get_method(baseUrl, payload, headers)
    return response


def req_no_auth(payload):
    response = HttpClient.RestMethods.get_method(baseUrl, payload, headers)
    return response
