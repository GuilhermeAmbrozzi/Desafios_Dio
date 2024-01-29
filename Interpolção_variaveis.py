# Para ligar variáveis a strings, temos alguns modelos no python.

# O primeiro e menos recomendado é OLD STYLE%, por ficar complicado de dar manutenção no código, por sua difícil compreensão.

nome = "Guilherme"
idade = 31
profissao = "Vigilante"
curso = "Python"

# Analise como ficou mais complicado o entendimento, se as variáveis estiverem fora de ordem dará um erro.
print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s."%(nome, idade, profissao, curso))
# Exemplo do erro se inverter as variáveis.
print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s."%(curso, idade, profissao, nome))

# O segundo modo para ligar strings a variáveis é FORMAT, Nesse modo temos algumas ventagens comparado ao anterior.
# Posso seguir a ordem correta das variáveis, com isso não afetara o código.
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, curso))
# Mas caso, seja invertido a posição das variáveis e não declará las vai aver erro.
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(curso, profissao, idade, nome))
# Também posso associar as variáveis 
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {curso}.".format(curso=curso, profissao=profissao, idade=idade, nome=nome))
# Aqui a principal vantagem, podemos colocar a posição das variáveis, e também podemos repeti-las sem problemas.
print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(curso, profissao, idade, nome))

# Temos o método mais recomendado e usado F-STRING

# Note a facilidade do entendimento do código.
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {curso}.")

PI = 3.14159

# Forma correta de declarar casas decimais.
print(f"Valor de PI: {PI:.2f}")
# Caso eu queira colocar espaço, entre a string e o valor tenho que informar. 
print(f"Valor de PI: {PI:10.2f}")




