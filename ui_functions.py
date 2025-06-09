#-*- coding: UTF-8 -*-

import requests
import json


def request_cnpj(cnpj):
    """ Pesquisar por um CNPJ informado pelo usuário """
    
    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
    querystring = {"token": "XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX", "cnpj": "06990590000123", "plugin": "RF"}
    response = requests.request("GET", url, params=querystring)
    
    data = json.loads(response.text)
    
    print(data)
    
