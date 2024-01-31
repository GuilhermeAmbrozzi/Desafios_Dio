# Strings de múçtiplas linhas são definidas informando 3 aspas simples ou duplas durante a atribuição.
# Elas podem ocupar várias linhas do código, e todos os espaços em branco são incluídos na string final.


nome = "Guilherme"
mensagem = f"""
Olá meu nome é {nome},
Eu estou aprendendo python
"""
print(mensagem)

# Nesse segundo exemplo mostramos que mostra os espaços em branco também.

nome = "Rafael"

mensagem = f"""
         Olá meu nome é {nome},
Eu estou aprendendo python
          Essa mensagem tem diferentes recuos.
"""
print(mensagem)

test = "rafael"