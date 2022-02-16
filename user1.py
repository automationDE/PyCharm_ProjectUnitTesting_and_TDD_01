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

# Leitor de arquivo csv
def ler_dados_do_csv():
        teste_dados_csv = []
        nome_arquivo = 'users.csv'
        try:
            with open(nome_arquivo,newline='') as csvfile:
                dados = csv.reader(csvfile,delimiter=',')
                next(dados)
                for linha in dados:
                    teste_dados_csv.append(linha)
            return teste_dados_csv
        except FileNotFoundError:
            print(f'Arquivo nao encontrado: {nome_arquivo}')
        except Exception as fail:
            print(f'Falha imprevista: {fail}')

@pytest.mark.parametrize('id, email, first_name, last_name, avatar', ler_dados_do_csv() )
def testing_data_users(id, email, first_name, last_name, avatar):  #' Function to test anything'
    try:
        response = requests.get(f'https://reqres.in/api/users/{id}')
        jsonResponse = response.json()
        id_obtido = jsonResponse['data'][id]
        email_obtido = jsonResponse['data']['email']
        nome_obtido = jsonResponse['data']['first_name']
        sobrenome_obtido = jsonResponse['data']['last_name']
        avatar_obtido = jsonResponse['data']['avatar']

        print(f'id: {id_obtido} - email: {email_obtido} - nome: {nome_obtido} - sobrenome: {sobrenome_obtido} - avatar: {avatar_obtido}')
        print(f'id: {id_obtido} \n email: {email_obtido} \n nome: {nome_obtido} \n sobrenome: {sobrenome_obtido} - avatar: {avatar_obtido}')

        #print(f'id:{} \n nome:{} \n sobrenome: {} \n email:{}.format(id_obtido,nome_obtido,sobrenome_obtido,email_obtido))
        print(json.dumps(jsonResponse, indent=2, sort_keys=True))

        assert id_obtido == id
        assert email_obtido == email
        assert nome_obtido == first_name
        assert sobrenome_obtido == last_name
        assert avatar_obtido == avatar

    except HTTPError as http_fail:
        print(f'Um erro de HTTP aconteceu: {http_fail}')
    except Exception as fail:
        print(f'Falha inesperada: {fail}')

# Function to test anything outside of my computer
# API to use and perform the test
# http://reqres.in/api/users{id}