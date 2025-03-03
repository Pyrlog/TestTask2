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


def test_Get_All_Brtands_List():
    response = requests.get('https://automationexercise.com/api/brandsList')
    json_response = response.json()
    assert json_response.get('responseCode') == 200
    assert type(json_response.get('brands')) == list

def test_PUT_To_All_Brands_List():
    response = requests.put("https://automationexercise.com/api/brandsList")
    json_response = response.json()
    assert json_response.get('responseCode') == 405
    assert json_response.get('message') == 'This request method is not supported.'