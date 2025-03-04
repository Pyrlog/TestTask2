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

def test_post_to_verify_login_with_valid_details():
    response = requests.post("https://automationexercise.com/api/verifyLogin", data = {"email": "johndoe765@gmail.com", "password": "password"})
    json_response = response.json()
    assert json_response.get('responseCode') == 200
    assert json_response.get('message') == 'User exists!'


def test_post_to_verify_login_without_email_parameter():
    response = requests.post("https://automationexercise.com/api/verifyLogin", data = {"password": "password"})
    json_response = response.json()
    assert json_response.get('responseCode') == 400
    assert json_response.get('message') == 'Bad request, email or password parameter is missing in POST request.'


#def test_post_to_create_register_user_acount():
#    response = requests.post("https://automationexercise.com/api/createAccount", data = {"name": "John", "email": "johndoe765@gmail.com", "password": "password", "title": "Mr", "birth_date": "01", "birth_month": "01", "birth_year": "1991", "firstname": "John", "lastname": "Doe", "company": "Best_company", "address1": "Pushkina_5", "address2": "7", "country": "USA", "zipcode": "1111", "state": "Texas", "city": "Houston", "mobile_number": "123456"})
#    json_response = response.json()
#    assert json_response.get('responseCode') == 201
#    assert json_response.get('message') == 'User created!'