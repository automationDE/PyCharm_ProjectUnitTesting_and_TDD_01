# 1 - imports
import json

import pytest
import csv

import requests as requests
from requests import HTTPError

test_data_current_users = [
    (1, 'george.bluth@reqres.in', 'George', 'Bluth', 'https://reqres.in/img/faces/1-image.jpg'),      # User 1
    (2, 'janet.weaver@reqres.in', 'Janet', 'Weaver', 'https://reqres.in/img/faces/2-image.jpg'),      # User 2
    (3, 'emma.wong@reqres.in', 'Emma', 'Wong', 'https://reqres.in/img/faces/3-image.jpg'),            # User 3
]

@pytest.mark.parametrize('id, email_1, first_name_1, last_name_1, avatar_1', test_data_current_users)
def testing_data_users(id, email_1, first_name_1, last_name_1, avatar_1):  #' Function to test anything'
    try:
        response = requests.get(f'https://reqres.in/api/users/{id}')
        jsonResponse = response.json()
        id_obtido = jsonResponse['data']['id']
        email_obtido = jsonResponse['data']['email']
        nome_obtido = jsonResponse['data']['first_name']
        sobrenome_obtido = jsonResponse['data']['last_name']
        avatar_obtido = jsonResponse['data']['avatar']

        #print(f'id: {id_obtido} - email: {email_obtido} - nome: {nome_obtido} - sobrenome: {sobrenome_obtido} - avatar: {avatar_obtido}')
        print(f'id: {id_obtido} \n email: {email_obtido} \n nome: {nome_obtido} \n sobrenome: {sobrenome_obtido} - avatar: {avatar_obtido}')

        #print(f'id: {id_obtido} \n nome: {nome_obtido} \n spbrenome: {sobrenome} \n email: {}.format(id_obtido,nome_obtido,sobrenome_obtido,email_obtido))

        #assert id_obtido == id
        #assert email_obtido == email_1
        #assert nome_obtido == first_name_1
        #assert sobrenome_obtido == last_name_1
        #assert avatar_obtido == avatar_1

    except HTTPError as http_fail:
        print(f'Um erro de HTTP aconteceu: {http_fail}')
    except Exception as fail:
        print(f'Falha inesperada: {fail}')




    #print(f'Success!!')

# Function to test anything outside of my computer
# API to use and perform the test
# http://reqres.in/api/users{id}