# Essa condição dentro do python é quando queremos analisar uma condição em uma única linha. 
# Ele é composto por três partes, a primeira parte é o retorno caso a expressão retorne verdadeiro, a segunda parte é a expressão lógica e a terceira parte é o retorno caso a expressão não seja atendida.

saldo = 2000
saque = 500

# a primeira parte é "Sucesso"
# segunda parte é o IF e ELSE
# e a terceira parte é a "Falha"
status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")