# Criando listas
# As listas em python podem ser armazenadas de maneira sequencial de qualquer tipo: int, float, bool e string.
# Podemos crias uma lista utilizando o comando LIST, a função RANGE (reproduz uma sequencia de valores inteiros.) ou colocamos valores separados por vírgula dentro dos colchetes[]. Lista são objetos mutáveis(é algo que pode ser mudado, sofrer alteração.),por isso podemos alterar seus valores após a sua criação.
# Exemplos:

# Declaração de uma lista.
frutas = ["laranja", "pera", "uva", "maça"]
print(frutas)
# Podemos declarar uma lista vazia.
fruta = []

# Nesse exemplo quando declaramos list com uma string dentro de () cada letra vira um elemento dentro da lista.
letras = list("Python")
print(letras)

# Nesse exemplo ele cria uma lista numerada lembrando que em python começa a partir do 0 então a contagem sempre n-1.
numeros = list(range(10))
print(numeros)

# Nesse exemplo mostramos que em python a LIST aceita todos os tipos ao mesmo tempo sem ter que fazer uma LIST para cada tipo.
# Com isso temos a marca, modelo, valor, ano, quilometragem, cidade e valor booleano verdadeiro.
carro = ["Ferrari", "F8", 42000000, 2020, 2900, "São Paulo", True]

# Listas é uma sequência, portanto podemos acessar seus dados utilizando índices. Lembrando que o índice de determinada sequência a partir do 0.

frutas = ["laranja", "pera", "uva", "maça"]
# Primeiro elemento
print(frutas[0])
print(frutas[2])
# também aceita valores negativos que vem da ultima letra a partir do -1
print(frutas[-1])
print(frutas[-3])

# Listas Aninhadas.

# Listas podem armazenar todos os tipos de objetos em python, portanto podemos ter listas que armazenam outras listas. Com isso podemos criar estruturas bidimensionais (matrizes/tabelas), e acessar informando os índices de linha e coluna.

matriz = [
    [1, "a", 2],
    ["b", 2, 4],
    [6, 5, "c"]
]

#chamando uma linha
print(matriz[0])
# chamando a linha 2
print(matriz[2])
# Para chamar um numero específicos 
print(matriz[0][0])
# chamando o ultimo número da linha
print(matriz[0][-1])
# vai chamar o ultimo elemento da matriz
print(matriz[-1][-1])

# Fatiamento 

# Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência. Para isso basta passar o índice inicial e/ou final para acessar o conjunto. podemos ainda informar quantas posições o cursor deve "pular" no acesso.
# Exemplo

lista = ["p", "y", "t", "h", "O", "n"]

print(lista[2:]) # ["t", "h", "O", "n"]
print(lista[:2]) # ["p", "y"]
print(lista[1:3]) # ["y", "t"]
print(lista[0:3:2]) # ["p", "t"]
print(lista[:]) # ["p", "y", "t", "h", "O", "n"]
print(lista[::-1]) # ["n", "o", "h", "t", "y", "p"]

# Agora veremos como percorrer essa lista e acessar todos os seus valores.
# A forma mais comum de percorrer uma lista é utilizando o comando FOR.
# Em Python, a palavra-chave in é usada dentro da estrutura de controle de fluxo for para iterar sobre os elementos de uma sequência (como uma lista, tupla, string, etc.) ou outros objetos iteráveis.
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)
    
# Função Enumerate

# Às vezes é necessário saber qual o índice do objeto dentro do laço FOR. para isso podemos usar a função ENUMERATE.
# O ENUMERATE vai numerar a partir do zero.
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
    
# Também posso adicionar a uma lista ou jogar elementos de uma lista para uma outra lista vazia temos 2 modos de fazer isso.

# Modificando valores versão 1.

numeros =[1,52,42,56,159,752,468,421,21,11]
pares = []

# Nesse comando temos a variável de controle numero com o comando IN, esse comando percorre uma sequência de elementos da variável NUMEROS, com isso ele cai dentro do bloco de teste IF que se o elemento for par ele joga esse elemento para a lista vazia PARES com o Método APPEND. O método APPEND serve para adicionar algo novo ao final da uma lista ou em uma nova lista vazia.
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
# Note que ele vai continuar com os seus elementos mesmo após o FOR.
print(numeros)
# Essa lista vai receber somente os elementos pares da lista numeros, mas esses elementos nao serão apagados da lista numeros.
print(pares)

# https://docs.python.org/3/tutorial/datastructures.html
# https://www.w3schools.com/python/python_lists_comprehension.asp

# List Comprehensions

# Oferece uma sintaxe mais curta para criar uma nova lista com base em valores de uma lista já existente.

# pares(nova lista) = [(variável de retorno para nova lista), FOR(condição de teste entre a variável de controle e a lista já existente), IF(condição para entrar na nova lista)]
pares = [numero for numero in numeros if numero % 2 == 0]

# Eu também posso modificar valores das listas usando o método de comprehension, para isso temos alguns métodos veja mais exemplos na documentação, deixei alguns links para você.