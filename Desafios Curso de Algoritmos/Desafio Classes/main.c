#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

/* Escrevendo as classes de um Jogo

**O Que deve ser utilizado**

- Vari�veis
- Operadores
- La�os de repeti��o
- Estruturas de decis�es
- Fun��es
- Classes e Objetos

## Objetivo:

Crie uma classe generica que represente um her�i de uma aventura e que possua as seguintes propriedades:

- nome
- idade
- tipo (ex: guerreiro, mago, monge, ninja )

al�m disso, deve ter um m�todo chamado atacar que deve atender os seguientes requisitos:

- exibir a mensagem: "o {tipo} atacou usando {ataque}")
- aonde o {tipo} deve ser concatenando o tipo que est� na propriedade da classe
- e no {ataque} deve seguir uma descri��o diferente conforme o tipo, seguindo a tabela abaixo:

se mago -> no ataque exibir (usou magia)
se guerreiro -> no ataque exibir (usou espada)
se monge -> no ataque exibir (usou artes marciais)
se ninja -> no ataque exibir (usou shuriken)

## Sa�da

Ao final deve se exibir uma mensagem:

- "o {tipo} atacou usando {ataque}"
  ex: mago atacou usando magia
  guerreiro atacou usando espada.  */

struct heroi {
	char nome [20];
	int idade;
	char tipo [20];
};

struct atacar{
	char magia[20];
	char espada[20];
	char artesmarciais[20];
	char shuriken[20];
};

int main(int argc, char *argv[]) {
	setlocale(LC_ALL, "");
		
	struct heroi personagem;
	    struct atacar ataques[4] = {
        {"magia", "", "", ""},        
        {"", "espada", "", ""},       
        {"", "", "artes marciais", ""}, 
        {"", "", "", "shuriken"}       
    };
	int op;
	
	
	printf("Digite um nome para o seu her�i: ");
	scanf("%s", &personagem.nome);
	
	printf("Qual sera a idade do seu her�i ? ");
	scanf("%d", &personagem.idade);
	
	printf("Escolha a sua classe de her�i: 1 - Mago, 2 - Guerreiro, 3 - Monje, 4 - Ninja\n");
	scanf("%s", &personagem.tipo);
	
	if (strcmp(personagem.tipo, "1") == 0) {
        printf("Voc� escolheu Mago!\n");
    } else if (strcmp(personagem.tipo, "2") == 0) {
        printf("Voc� escolheu Guerreiro!\n");
    } else if (strcmp(personagem.tipo, "3") == 0) {
        printf("Voc� escolheu Monje!\n");
    } else if (strcmp(personagem.tipo, "4") == 0) {
        printf("Voc� escolheu Ninja!\n");
    } else {
        printf("Classe Desconhecida!\n");
    }
    
    printf("%s atacou usando ", personagem.nome);


    if (strcmp(personagem.tipo, "1") == 0) {
        printf("%s\n", ataques[0].magia);
    } else if (strcmp(personagem.tipo, "2") == 0) {
        printf("%s\n", ataques[1].espada);
    } else if (strcmp(personagem.tipo, "3") == 0) {
        printf("%s\n", ataques[2].artesmarciais);
    } else if (strcmp(personagem.tipo, "4") == 0) {
        printf("%s\n", ataques[3].shuriken);
    }
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
	return 0;
}
