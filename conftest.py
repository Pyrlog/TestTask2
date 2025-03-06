import pytest

@pytest.fixture()
def base_url():
    return "https://automationexercise.com/api/"


@pytest.fixture()
def http_status_codes():
    return {
        "OK": 200,
        "CREATED": 201,
        "NO_CONTENT": 204,
        "BAD_REQUEST": 400,
        "UNAUTHORIZED": 401,
        "FORBIDDEN": 403,
        "NOT_FOUND": 404,
        "METHOD_NOT_ALLOWED": 405,
        "INTERNAL_SERVER_ERROR": 500,
    }


@pytest.fixture()
def response_messages():
    return {
        "METHOD_NOT_SUPPORTED": 'This request method is not supported.',
        "BAD_REQUEST_NO_SEARCH_PRODUCT": 'Bad request, search_product parameter is missing in POST request.',
        "USER_CREATED": 'User created!',
        "USER_EXISTS": 'User exists!',
        "BAD_REQUEST_NO_EMAIL_PASSWORD": 'Bad request, email or password parameter is missing in POST request.',
        "USER_NOT_FOUND": 'User not found!',
        "USER_UPDATED": 'User updated!',
        "ACCOUNT_DELETED": 'Account deleted!'
    }