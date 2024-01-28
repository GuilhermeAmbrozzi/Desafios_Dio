# Comando FOR é utilizado e indicado quando sabemos o número máximo de repetição para o bloco determinado.

texto = input("Informe um texto.")

VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="\n") 
             
print()

# Função RENGE é uma função built-in no python, é usada para reproduzir uma sequência de números inteiros.
# Ela recebe 3 argumentos: Stop(Obrigatório se nao fica em um loop), start(opcional) e step (de quantos em quantos números ele deve aumentar ou diminuir)

# O 0 é da onde ele vai partir, o 51 é aonde ele vai parar de executar, 5 quantas casa ele deve pular, com isso mostramos a tabuada do 5.
for numero in range(0, 51, 5):
    print(numero, end=" ")