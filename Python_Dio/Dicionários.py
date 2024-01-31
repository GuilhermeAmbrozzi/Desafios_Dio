# Os dicionários são coleção de itens e seus elementos são armazenados de forma não ordenada.
# A chave serve para indexar(posicionar) um elemento no dicionário e o valor esta relacionado a sua chave.
# Os valores podem ser de vários tipo: lista, outros dicionários, int, string e etc.
# Exemplo:

month = int(input("Informe um número de 1 a 12."))

#if (month < 0) or (month > 12):
#    print("Número inválido digite novamente.")
#    month = int(input("Informe um número de 1 a 12."))
 
month_dict = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
} 

result = month_dict.get(month)

# Get retorna o valor dentro do dicionário, mas com ele podemos atribuir um retorno negativo aso não tenha o valor informado dentro do DICT
if result is not None:
    print(result)
else:
    print("Invalid month")
    
# tem vários método nos dicionários vou deixar um link caso volte ter dúvidas foi onde achei essas informações.
# https://pythonacademy.com.br/blog/dicts-ou-dicionarios-no-python#criando-dicion%C3%A1rios