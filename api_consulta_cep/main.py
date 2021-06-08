from sys import argv
import requests
import os
from time import sleep


#Criando Funções

#Função que mostra um titulo na tela
def dash_principal():
    print('='*22)
    titulo = 'CONSULTE O SEU CEP'
    print(titulo.center(22))
    print('='*22)

#Função que pede cep e valida se foi digitado corretamente
def pede_cep():
    cep = input('Digite o seu CEP: ').replace('-', '').strip().lstrip()
    while len(cep) != 8:
        print('\033[1;31mCEP INVALIDO\033[0;0m')
        print('\033[1;31mO CEP NÃO PODE CONTER CARACTERES ESPECIAIS\033[0;0m')
        cep = input('Digite o seu CEP novamente: ').replace('-', '').strip().lstrip()
    return(cep)

#Função que faz a requisição
def request(arg):
    resposta = requests.get(f'https://viacep.com.br/ws/{var_cep}/json/')
    print(resposta.json())

var_cep = pede_cep()

#Função de Sucesso
def sucesso():    
    print('='*22)
    titulo = '\033[1;32mENDEREÇO LOCALIZADO\033[0;0m'
    print(titulo.center(22))
    print('='*22)
   

def limpa_tela():
    os.system('cls')


#Iniciando o programa
dash_principal()

pede_cep()

request(var_cep)




