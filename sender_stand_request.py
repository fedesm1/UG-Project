import requests
import configuration
import data

# La funcion post_new_user realiza una solicitud al servidor para registrar un nuevo usuario con las datos del archivo configuration.py
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

# La funcion post_new_client_kit realiza una solicitud al servidor para registrar un nuevo kit con las datos del archivo configuration.py
def post_new_client_kit(kit_body, token):
    post_headers = data.headers.copy()
    post_headers['Authorization'] = token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=post_headers)






