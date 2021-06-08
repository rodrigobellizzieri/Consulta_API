import requests
from requests import status_codes
from requests.exceptions import FileModeWarning
from requests.models import HTTPBasicAuth

url = 'https://imunizacao-es.saude.gov.br/_search'
user = 'imunizacao_public'
password = 'qlto5t&7r_@+#Tlstigi'

r = requests.get(url, auth=HTTPBasicAuth(user, password))

resultado = r.json()
print(resultado)
"""
for i in resultado['hits']['hits']:
    print(i['_source']['vacina_lote'])"""
