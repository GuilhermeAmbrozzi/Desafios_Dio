# Vamos entender o que cada método faz dentro do python e sua funcionalidade.

nome = "GuIlHeRmE"

# coloca todas as letras em maiúsculas.
print(nome.upper())
# Coloca todas as letras em minúsculas.
print(nome.lower())
# Coloca somente a primeira letra em maiúscula e restante em minúsculas.
print(nome.title())

texto = " Olá Mundo!    "

# Retira os espaços da string.
print(texto.strip() + ".")
# Retira o espaço da direita, mais mantém os espaços do lado esquerdo.
print(texto.lstrip() + ".")
# Mantém o espado da direita, mas retira os espaços da esquerda.
print(texto.rstrip() + ".")

texto = "Guilherme"
# Esse método centraliza a string ao centro;após, ele pode adicionar um elemento ou espaço em branco.
print(texto.center(14, "#"))
# vai passar em sequência na string adicionando algum elemento ou valor.
print(".".join(texto))
