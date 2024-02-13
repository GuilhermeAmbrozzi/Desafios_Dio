# São muito parecidas com as Listas, a sua diferença marcante é que Tuplas são imutáveis já as Listas são mutáveis.
# Temos dois modos de declarar uma Tupla.

# 1º modo de declarar uma Tupla

numero = tuple([1, 2, 3, 4])

# 2º modo de declarar uma Tupla

# Nessa forma de declaração para o Python identificar é obrigatório a colocação da ultima vírgula.
frutas = ("laranja","uva","maçã","pera",)

# Para acessar os valores é igual a listas, por meio do seu índice por ser uma sequência.

print(frutas[2])
print(frutas[3])
print(frutas[-2])

# Tuplas tem poucos métodos que podem ser utilizados.

#()COUNT é um deles é usados para contar quantos elementos iguais tem dentro de uma Tupla.

#()INDEX Para saber qual posição o elementos esta dentro de uma Tupla.

#()LEN para contar quantos elementos temos dentro de uma Tupla.
