#CONVERSÃO DE TIPOS
#algumas vezes vamos ter que fazer algumas conversões dentro dos códigos isso é normal, sempre lembrando que um int para float ou float para int o valor sera arredondado perdendo sua casa decimal. Segue os exemplos de conversões de tipos.
#float
preco = 10.50
#int
idade = 28

#conversão para string
print(str(preco))
#conversão para string
print(str(idade))

#no Python para concatenar variáveis temos que colocar o F antes e colocar as variáveis dentro de {}
texto = f'idade {idade} preço {preco} '

print(texto)
#tipo string
preco = '12.45'

#tipo string
idade = '31'

#conversão de string para float
print(float(preco))

#conversão de string para int
print(int(idade))

#se tentar converter uma string para um float ou int que seja um texto ocorrera um erro dentro do programa por que não é um numero e sim uma sequência de carácter.
preco = 'python'

#Em Python para atribuir um valor a uma variável a qual sera feita uma pergunta ao usuário usamos o comando input, com isso ele jogará automaticamente o valor recebido para dentro da variável.

#aqui esta jogando a resposta do usuário para dentro de uma variável que será uma string
nome = input ("Informe seu nome: ")
#aqui esta jogando a resposta do usuário para dentro de uma variável que será um int
idade = input ("Informe a sua idade: ")

#aqui ele exibirá na tela os valores informados.
print(nome, idade)
#Aqui vai exibir os valores colocando os ... e dando uma quebra de linha.
print(nome, idade, end = "... \n")

#Aqui vai exibir os valores colocando # entre os valores.
print(nome, idade, sep = "#")
