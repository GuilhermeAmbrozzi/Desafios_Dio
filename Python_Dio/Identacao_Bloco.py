# Indentação em python é importante, além de facilitar a visibilidade também ajuda na manutenção do código, mais em python se um bloco de comandos nao estiver indentado, voltará um erro e não funcionara o código.
# Analise no código os espaços que temos em cada um deles, isso delimita o código, mostrando onde começa e termina de acordo com o espaço.
def sacar(valor):
    # Note o espaço do def para saldo
    saldo = 500
    
    if saldo >= valor:
        # note espaço do if para o comando print
        # print pertence ao bloco IF, so irá aparecer se o programa executar o IF.
        print("Valor Sacado")
        print("Retire o seu dinheiro na boca do caixa.")
    # esse print pertence ao bloco DEF, mostrará mesmo que o IF não seja executado.        
    print("Obrigado por ser nosso cliente, tenha um bom dia!")

# Nesse exemplo vai retornar erro!!
#def depositar(valor):
#saldo = 500
#saldo += valor 
    
sacar(100)