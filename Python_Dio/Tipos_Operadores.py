#Operadores Aritméticos

#Divisão
print(12 / 3)
# Divisão Inteira
print (12 // 3)
#Módulo
print(10 % 3)
#Exponenciação
print(2 ** 3)

#Regras para calcular dentro do Python segue a matemática
#1° Os parênteses
x = (10 + 5) * 2
print(f'1° = {x}' )
#2° Expoentes
x = 10 ** 2 -5
print(f'2° = {x}')
#3° Multiplicação e Divisão (da esquerda para a direita)
x = 10 * 2 / 2
print(f'3° = {x}')
#4° Soma e Subtração (da esquerda para a direita)
x = 10 + 5 - 7
print(f'4° = {x}')

# Operadores de Comparação

# Usamos os operadores de comparação para identificar se as afirmação são ou nao verdadeiras.
# Igualdade
saldo = 230
saque = 120
print(saldo == saque)

# Diferença
saldo = 230
saque = 120
print(saldo != saque)

# Maior que / Maior ou Igual
saldo = 230
saque = 120
print(saldo > saque)
print(saldo >= saque)

# Menor que / Menor ou Igual
saldo = 230
saque = 120
print(saldo < saque)
print(saldo <= saque)

# Atribuição

# Atribuição Simples
saldo = 500
print(saldo)

# Atribuição com Adição
saldo += 200
print(saldo)

# Atribuição com Divisão
saldo = 500
saldo /= 5 # resultado em float
print(saldo)
saldo = 500
saldo //= 5 # resultado em int
print(saldo)

# Atribuição com Módulo 
saldo = 500
saldo %= 480
print(saldo)

# Atribuição com Exponenciação
saldo = 80
saldo **= 2
print(saldo)

# Operadores Lógicos

# Operador E conjunção em Python é AND
saldo = 1000
saque = 250
limite = 200
conta_especial = True

# Operador E conjunção
exp = saldo >= saque and saque <= saldo
print(exp)

# Operador OU Disjunção em Python é OR
exp_2 = saldo >= limite or limite <= saque
print(exp_2)

# Operador NÃO é negação em Python é NOT
exp_3 = not conta_especial
print(exp_3)

# Operadores de Identidade

# É usado para saber se variáveis diferentes ocupam o mesmo local de memória

saldo = 1000
limite = 1000
# Comparação de variáveis ocupando mesmo espaço na memória
print(saldo is limite)
# Comando de negação da comparação de identidade
print(saldo is not limite)

# Operadores de Identidade
# Usado para comparar variáveis se estão ocupando o mesmo local na memória
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200,200

# comparação de identidade
print(curso is nome_curso)
print(saldo is limite)
# negação de identidade
print(saldo is not limite )

# Operador de associação
# Usado para verificar se um objeto esta presente em uma sequência.

curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

#comparação de associação
print("Python" in curso)
print("maçã" not in frutas)
#comparação de negação de associação
print(200 in saques)