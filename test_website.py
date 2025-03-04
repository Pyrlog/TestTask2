import requests


def test_get_all_products_list():
    response = requests.get('https://automationexercise.com/api/productsList')
    json_response = response.json()
    assert json_response.get('responseCode') == 200
    assert type(json_response.get('products')) == list


def test_post_to_all_products_list():
    response = requests.post('https://automationexercise.com/api/productsList')
    json_response = response.json()
    assert json_response.get('responseCode') == 405
    assert json_response.get('message') == 'This request method is not supported.'


def test_get_all_brands_list():
    response = requests.get('https://automationexercise.com/api/brandsList')
    json_response = response.json()
    assert json_response.get('responseCode') == 200
    assert type(json_response.get('brands')) == list


def test_put_to_all_brands_list():
    response = requests.put("https://automationexercise.com/api/brandsList")
    json_response = response.json()
    assert json_response.get('responseCode') == 405
    assert json_response.get('message') == 'This request method is not supported.'


def test_post_to_search_product():
    response = requests.post("https://automationexercise.com/api/searchProduct", data = {"search_product": "top"})
    json_response = response.json()
    assert json_response.get('responseCode') == 200
    assert type(json_response.get('products')) == list


def test_post_to_search_product_without_search_product_parameter():
    response = requests.post("https://automationexercise.com/api/searchProduct")
    json_response = response.json()
    assert json_response.get('responseCode') == 400
    assert json_response.get('message') == 'Bad request, search_product parameter is missing in POST request.'


def test_post_to_create_register_user_account():
    response = requests.post("https://automationexercise.com/api/createAccount", data = {"name": "John", "email": "johndoe7654@gmail.com", "password": "password", "title": "Mr", "birth_date": "01", "birth_month": "01", "birth_year": "1991", "firstname": "John", "lastname": "Doe", "company": "Best_company", "address1": "Pushkina_5", "address2": "7", "country": "USA", "zipcode": "1111", "state": "Texas", "city": "Houston", "mobile_number": "123456"})
    json_response = response.json()
    assert json_response.get('responseCode') == 201
    assert json_response.get('message') == 'User created!'


def test_post_to_verify_login_with_valid_details():
    response = requests.post("https://automationexercise.com/api/verifyLogin", data = {"email": "johndoe7654@gmail.com", "password": "password"})
    json_response = response.json()
    assert json_response.get('responseCode') == 200
    assert json_response.get('message') == 'User exists!'


def test_post_to_verify_login_without_email_parameter():
    response = requests.post("https://automationexercise.com/api/verifyLogin", data = {"password": "password"})
    json_response = response.json()
    assert json_response.get('responseCode') == 400
    assert json_response.get('message') == 'Bad request, email or password parameter is missing in POST request.'


def test_post_to_verify_login_with_invalid_details():
    response = requests.post("https://automationexercise.com/api/verifyLogin", data = {"email": "johndoe765@@gmail.com", "password": "password"})
    json_response = response.json()
    assert json_response.get('responseCode') == 404
    assert json_response.get('message') == 'User not found!'


def test_delete_to_verify_login():
    response = requests.delete("https://automationexercise.com/api/verifyLogin")
    json_response = response.json()
    assert json_response.get('responseCode') == 405
    assert json_response.get('message') == 'This request method is not supported.'


def test_put_method_to_update_user_account():
    response = requests.put("https://automationexercise.com/api/updateAccount", data = {"name": "John", "email": "johndoe7654@gmail.com", "password": "password", "title": "Mr", "birth_date": "04", "birth_month": "08", "birth_year": "1974", "firstname": "John", "lastname": "Doe", "company": "Best_company", "address1": "Pushkina_5", "address2": "7", "country": "USA", "zipcode": "1111", "state": "Texas", "city": "Houston", "mobile_number": "123456"})
    json_response = response.json()
    assert json_response.get('responseCode') == 200
    assert json_response.get('message') == 'User updated!'


def test_get_user_account_detail_by_email():
    response = requests.get("https://automationexercise.com/api/getUserDetailByEmail", params = {"email": "johndoe7654@gmail.com"})
    json_response = response.json()
    assert json_response.get('responseCode') == 200
    assert 'user' in json_response
    assert json_response.get('user').get('email') == "johndoe7654@gmail.com"


def test_delete_method_to_delete_user_account():
    response = requests.delete("https://automationexercise.com/api/deleteAccount", data = {"email": "johndoe7654@gmail.com", "password": "password"})
    json_response = response.json()
    assert json_response.get('responseCode') == 200
    assert json_response.get('message') == 'Account deleted!'