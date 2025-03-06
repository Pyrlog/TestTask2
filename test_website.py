import requests


def test_get_all_products_list(base_url, http_status_codes):
    response = requests.get(f'{base_url}productsList')
    json_response = response.json()
    assert json_response.get('responseCode') == http_status_codes['OK']
    assert type(json_response.get('products')) == list


def test_post_to_all_products_list(base_url, http_status_codes, response_messages):
    response = requests.post(f'{base_url}productsList')
    json_response = response.json()
    assert json_response.get('responseCode') == http_status_codes['METHOD_NOT_ALLOWED']
    assert json_response.get('message') == response_messages['METHOD_NOT_SUPPORTED']


def test_get_all_brands_list(base_url, http_status_codes):
    response = requests.get(f'{base_url}brandsList')
    json_response = response.json()
    assert json_response.get('responseCode') == http_status_codes['OK']
    assert type(json_response.get('brands')) == list


def test_put_to_all_brands_list(base_url, http_status_codes, response_messages):
    response = requests.put(f"{base_url}brandsList")
    json_response = response.json()
    assert json_response.get('responseCode') == http_status_codes['METHOD_NOT_ALLOWED']
    assert json_response.get('message') == response_messages['METHOD_NOT_SUPPORTED']


def test_post_to_search_product(base_url, http_status_codes):
    response = requests.post(f"{base_url}searchProduct", data = {"search_product": "top"})
    json_response = response.json()
    assert json_response.get('responseCode') == http_status_codes['OK']
    assert type(json_response.get('products')) == list


def test_post_to_search_product_without_search_product_parameter(base_url, http_status_codes, response_messages):
    response = requests.post(f"{base_url}searchProduct")
    json_response = response.json()
    assert json_response.get('responseCode') == http_status_codes['BAD_REQUEST']
    assert json_response.get('message') == response_messages['BAD_REQUEST_NO_SEARCH_PRODUCT']


def test_post_to_create_register_user_account(base_url, http_status_codes, response_messages):
    response = requests.post(f"{base_url}createAccount", data = {"name": "John", "email": "johndoe7654@gmail.com", "password": "password", "title": "Mr", "birth_date": "01", "birth_month": "01", "birth_year": "1991", "firstname": "John", "lastname": "Doe", "company": "Best_company", "address1": "Pushkina_5", "address2": "7", "country": "USA", "zipcode": "1111", "state": "Texas", "city": "Houston", "mobile_number": "123456"})
    json_response = response.json()
    assert json_response.get('responseCode') == http_status_codes['CREATED']
    assert json_response.get('message') == response_messages['USER_CREATED']


def test_post_to_verify_login_with_valid_details(base_url, http_status_codes, response_messages):
    response = requests.post(f"{base_url}verifyLogin", data = {"email": "johndoe7654@gmail.com", "password": "password"})
    json_response = response.json()
    assert json_response.get('responseCode') == http_status_codes['OK']
    assert json_response.get('message') == response_messages['USER_EXISTS']


def test_post_to_verify_login_without_email_parameter(base_url, http_status_codes, response_messages):
    response = requests.post(f"{base_url}verifyLogin", data = {"password": "password"})
    json_response = response.json()
    assert json_response.get('responseCode') == http_status_codes['BAD_REQUEST']
    assert json_response.get('message') == response_messages['BAD_REQUEST_NO_EMAIL_PASSWORD']


def test_post_to_verify_login_with_invalid_details(base_url, http_status_codes, response_messages):
    response = requests.post(f"{base_url}verifyLogin", data = {"email": "johndoe765@@gmail.com", "password": "password"})
    json_response = response.json()
    assert json_response.get('responseCode') == http_status_codes['NOT_FOUND']
    assert json_response.get('message') == response_messages['USER_NOT_FOUND']


def test_delete_to_verify_login(base_url, http_status_codes, response_messages):
    response = requests.delete(f"{base_url}verifyLogin")
    json_response = response.json()
    assert json_response.get('responseCode') == http_status_codes['METHOD_NOT_ALLOWED']
    assert json_response.get('message') == response_messages['METHOD_NOT_SUPPORTED']


def test_put_method_to_update_user_account(base_url, http_status_codes, response_messages):
    response = requests.put(f"{base_url}updateAccount", data = {"name": "John", "email": "johndoe7654@gmail.com", "password": "password", "title": "Mr", "birth_date": "04", "birth_month": "08", "birth_year": "1974", "firstname": "John", "lastname": "Doe", "company": "Best_company", "address1": "Pushkina_5", "address2": "7", "country": "USA", "zipcode": "1111", "state": "Texas", "city": "Houston", "mobile_number": "123456"})
    json_response = response.json()
    assert json_response.get('responseCode') == http_status_codes['OK']
    assert json_response.get('message') == response_messages['USER_UPDATED']


def test_get_user_account_detail_by_email(base_url, http_status_codes):
    response = requests.get(f"{base_url}getUserDetailByEmail", params = {"email": "johndoe7654@gmail.com"})
    json_response = response.json()
    assert json_response.get('responseCode') == http_status_codes['OK']
    assert 'user' in json_response
    assert json_response.get('user').get('email') == "johndoe7654@gmail.com"


def test_delete_method_to_delete_user_account(base_url, http_status_codes, response_messages):
    response = requests.delete(f"{base_url}deleteAccount", data = {"email": "johndoe7654@gmail.com", "password": "password"})
    json_response = response.json()
    assert json_response.get('responseCode') == http_status_codes['OK']
    assert json_response.get('message') == response_messages['ACCOUNT_DELETED']