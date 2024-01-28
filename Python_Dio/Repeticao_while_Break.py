# A estrutura de repeição while vai se mantendo repetindo enquando a condição dela for verdadeira, mais em python temos uma opção de colocar um bloco de parada diferente das demais linguagens, usamos o BREAK ele vai travar essa repetição se a condição for atendida.

# Comum encontrar nos códigos o while como sempre verdadeiro.
while True:
    numero = int(input("Informe um numero: "))
    
    # Vai testar se o número informado esta dentro da condição de parada.
    if numero == 10:
        # Comando para sair do loop.
        break
    
    if numero % 2 == 0:
        # Esse comando vai travar a exibição dos números pares mais se eu colocasse ele antes do break esse laço nunca iria parar.
        continue
    
    print(numero)