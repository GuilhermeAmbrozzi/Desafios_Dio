# Desafio fazer um sistema bancário com 3 operações: depósitos, saque e extrato.
import sys

tela_inicial = f"""
---------------Menu---------------
Bem Vindo. Escolha a sua operação.

[a] Depósito
[b] Saques
[c] Extrato
[d] Sair
----------------------------------
"""
saldo = 0
deposito = 0
limite = 500
extrato = ""
saque = 0
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(tela_inicial)
    
    if opcao == "a":
        deposito = float(input("Depósito informe o valor: "))
        if deposito < 0 :
            print("Valor inválido!!")
            print("Essa operação será encerrada!!")
            sys.exit()  # Encerra a execução do programa
        else:
                saldo += deposito
                extrato += f"Depósito: + R${deposito:.2f}\n"
    elif opcao == "b":
        
        saque = float(input(" Saque informe o valor: "))

        if saldo < 0:
            print("Saldo insuficiente!!")
            sys.exit()
        
        if saque < 0 or saque > 500:
            print("Valor inválido!!")
            print("Essa operação será encerrada!!")
            sys.exit()  
        
        if numero_saques < LIMITE_SAQUES:
            saldo -= saque
            extrato += f"Saque: - R$ {saque:.2f}\n"
            numero_saques += 1
        else:
            print("Número de limites de saques atingidos. Volte amanhã!!")
            sys.exit()
    elif opcao == "c":
            if not extrato:
                print("Não há movimentações no extrato.")
            else:
                print("Extrato:")
                print(extrato)
                print(f"Saldo em conta R$ {saldo}")
    elif opcao == "d":
        sys.exit()