from documentos import Documento
from TelefonesBr import TelefonesBr
from validate_docbr import CNPJ
import re
from datetime import datetime, timedelta
from datas_br import DatasBr
from acesso_cep import BuscaEndereco
import requests

print("-------------------------Validando CPF e CNPJ----------------------------")
print("-------------------------------------------------------------------------")
exemplo_cpf = "15316264754"
exemplo_cnpj = "35379838000112"

documento1 = Documento.cria_documento(exemplo_cpf)
documento2 = Documento.cria_documento(exemplo_cnpj)


print(documento1)
print(documento2)

#Expressoes regulares
print("-------------------------Expressoes regulares----------------------------")
print("-------------------------------------------------------------------------")

#padrao_molde = "(xx)aaaa-wwww"
#padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
#texto = "eu gosto do numero 2126451234"
#resposta = re.search(padrao,texto)

#print(resposta.group())

telefone = "2126481234"

telefone_objeto = TelefonesBr(telefone)

print(telefone_objeto)

#Manipulando e formatando datas
print("------------------------Manipulando e formatando datas-----------------------------")
print("-----------------------------------------------------------------------------------")
#print(datetime.today())

cadastro = DatasBr()

print(cadastro.mes_cadastro())
print(cadastro.dia_semana())

print(cadastro)

hoje = datetime.today()
amanha = datetime.today()+timedelta(days=1,hours=13)

print(amanha-hoje)


objeto_hoje = DatasBr()

print(objeto_hoje.tempo_cadastro())

#trabalhando com CEP e acessando uma API
print("---------------------trabalhando com CEP e acessando uma API--------------------------------")
print("--------------------------------------------------------------------------------------------")

cep = "77015567"
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)

#r = requests.get("https://viacep.com.br/ws/01001000/json/")
#print(r.text)

bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)