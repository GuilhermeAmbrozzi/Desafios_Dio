# Aqui vou colocar alguns modelos de Classes que temos em LIST os mais usados passado pelo professo.

# []APPEND, usado para adicionar um elemento a LIST colocando na ultima posição.Podemos adicionar como já vimos INT, FLOAT, STRING E BOOLEANO

lista = []

lista.append(1)
lista.append("Guilherme")
lista.append([2, 30, 12])
print(lista)

# []CLEAR, usado para remover elementos da lista, não é possível apagar somente um elemento.

lista.clear()
print(lista)

# []COPY, ele copia uma lista igual deixando essa lista em uma memória diferente, com isso posso mudar a lista original ou a copia sem alterar o valor de ambas.

lista = [1,25,35,"Guilherme"]

lista2 = lista.copy()
lista2.append("aires")
print(lista)
print(id(lista))
# Note que o id das listas são diferentes.
print(lista2)
print(id(lista2))

# []COUNT, Usado para contar quantos elementos iguais tem em uma lista, mais devemos passar o elementos que estamos procurando.

cores = ["azul", "vermelho", "verde", "azul","violeta","vermelho","amarelo"]

# Se eu nao passar um elemento vai dar erro.
# print(cores.count())
print(cores.count("azul"))
print(cores.count("vermelho"))

# []EXTEND, Posso usa-lo para adicionar elementos de uma lista para outra lista, esses elementos serão adicionados ao final da lista, também posso adicionar qualquer objeto sem ter a necessidade de ser uma lista.

linguagens = ["python", "js"]
print(linguagens)
linguagens2 = ["java", "c"]
print(linguagens2)
# adicionando os elementos de uma lista dentro da outra lista.
linguagens.extend(linguagens2)
print(linguagens)
# adicionando novos objetos dentro da lista, note que ele pode repetir algum elemento já existente.
linguagens2.extend(["C#", "Rubi", "c"])
print(linguagens2)

# []INSERT, usado para inserir um elemento, mais também podemos escolher o índice a qual ele será inserido.

thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.insert(1, "orange")
print(thislist)

# []INDEX, mostra o índice do elemento mais caso tenha 2 elementos iguais ele mostra o índice somente do primeiro.

lingua = ["ingles", "italiano", "português", "francês", "alemão", "português"]

print(lingua.index("alemão"))
print(lingua.index("português"))

#[]REMOVE, remove um item especifico da lista.

thislist = ["apple", "banana", "cherry","uva", "banana"]
# Se houver mais de um item com o valor especificado, o remove()método remove a primeira ocorrência:
thislist.remove("banana")
print(thislist)

#[]POP, Esse método remove o índice especificado ou o último elemento

# removendo por índice
thislist.pop(1)
print(thislist)
# Removendo o último elemento.
thislist.pop()
print(thislist)

#[]REVERSE, Inverte a ordem de classificação atual dos elementos.

thislist = ["banana", "Orange", "Kiwi", "cherry"]
print(thislist)

thislist.reverse()
print(thislist)

#[]SORT, Esse método ordenará a lista alfabeticamente, em ordem crescente, por padrão.

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(thislist)
thislist.sort()
print(thislist)

# classificar uma lista numericamente.
thislist = [100, 50, 65, 82, 23]
print(thislist)
thislist.sort()
print(thislist)

# Para classificar em ordem decrescente, use a palavra-chave argument reverse = True:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(thislist)
thislist.sort(reverse = True)
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(thislist)
# Organiza pelo tamanho das palavras.
thislist.sort(key=lambda x: len(x))
print(thislist)

# Organiza pelo tamanho das palavras invertida.
thislist.sort(key=lambda x: len(x), reverse=True)
print(thislist)

# Classifique a lista em ordem decrescente:

thislist = [100, 50, 65, 82, 23]
print(thislist)
thislist.sort(reverse = True)
print(thislist)

# []LEN, posso usalo para ver um tamanho de string mais também para ver o tamanho da lista.

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(len(thislist))

#ordena também por ordem alfabética 
print(sorted(cores))

print(sorted(cores, key=lambda x: len(x)))

print(sorted(cores, key=lambda x: len(x), reverse=True))