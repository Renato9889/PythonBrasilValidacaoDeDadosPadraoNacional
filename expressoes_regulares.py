import re
#Expressoes regulares
print("-----------------------------------------------------")
padrao = "[0-9][a-z]{2}[0-9]"
texto = "123 1ac2 1cc aa1"
resposta = re.search(padrao,texto)
print(resposta.group())

padrao2 = "\w{5,50}@[a-z]{3,10}.com.br"
texto2 = "aaabbbcc wanda123@gmail.com.br ccbbbaaa2 vision3@gmail.com.br"
resposta2 = re.search(padrao2, texto2)
resposta3 = re.findall(padrao2,texto2)

print(resposta2.group())
print(resposta3)