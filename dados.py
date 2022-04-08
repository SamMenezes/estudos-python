from cgitb import scanvars
from random import seed
from random import randint

numero_de_dados = int(input('Digite quantos dados você quer jogar: '))
a=0
for _ in range (numero_de_dados):
    num_dados = randint(1,6)
    a=a+num_dados
print('O valor total é: ', a)
