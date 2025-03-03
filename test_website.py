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