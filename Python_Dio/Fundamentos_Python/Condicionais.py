# If pode ser usado para testar uma condição dentro do bloco de código.
# Quando temos somente um if é uma estrutura condicional simples.
# estrutura condicional simples exemplo:   
# if saldo < saque:
#     print("Saldo insuficiente!")

# Temos também uma estrutura condicional com dois desvios, com isso usamos o IF e ELSE.
# Se a primeira expressão for verdadeira executa o bloco do IF se for falsa executa o bloco do ELSE
# if saldo >= saque:
#     print("Realizando Saque!")
# else:
#     print("Saldo Insuficiente")   

# Já em Python diferente de outras linguagens temos o ELIF que seria o ELSE IF.
# ELIF é composto por uma nova expressão lógica, que será testada e caso verdadeiro o bloco de código do elif será executado.
# Não existe um número máximo de ELIF que podemos utilizar, porém é bom evitar criar estruturas condicionais muito grandes.
#exemplo do ELIF

#opcao = int(input("Informe uma opção [1] Sacar\n[2] Extrato: "))
#if opcao == 1:
#   valor = float(input("Informe a quantia para o saque: "))
      #....
#elif opcao == 2:
#   print("Exibindo o extrato..")
#else:
#   sys.exit("Opção inválida!") 

opcao = int(input("Informe uma opção [1] Sacar [2] Extrato: "))
if opcao == 1:
   valor = float(input("Informe a quantia para o saque: "))
      #....
elif opcao == 2:
   print("Exibindo o extrato..")
else:
   print("Opção inválida!")   
    