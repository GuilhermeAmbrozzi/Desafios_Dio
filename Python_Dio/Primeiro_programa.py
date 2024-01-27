#Segue exemplos de Tipos dentro do Python

# exemplos de strings e os modelos aceitos em Python
print("Hello World!!!", 'olá!', """teste 3""")
#modelos de int números inteiros
print(11 + 10 - 1000)
#modelos de números reais float Python aceita você misturá-los 
print(1.5 + 1 + 0.5)
#exemplos de bool
print(True)
#exemplo de Bool
print(False)
#exemplo de lista que vem ser uma sequência dentro do Python
list = 12345
print(list)
my_list = [1,2,3]
# Retorna uma lista de atributos disponíveis para o objeto, se nenhum argumento for passado no dir ele retorna nomes de atributos do escopo local
print(dir(my_list))

# Mostra a documentação sobre algum comando como utiliza-lo e dando uma descrição completa de atributos e métodos para sair do help use a tecla Q.
help(int)

#Variáveis são valores que podem ser alteradas ao longo do algoritmo.
age = 31

#Constantes são valores imutável não pode ser alterado, em Python nao tem como entras linguagens um comando já pré definido, fica entendido que se o nome da variável estiver todo em maiúsculo ela é uma constante e não pode ser mudada.
DEBUG = True
STATES = [
  'SP',
  'RS',
  'MG'  
]