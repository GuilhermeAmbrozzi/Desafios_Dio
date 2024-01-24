#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>

/* Calculadora de partidas Rankeadas
**O Que deve ser utilizado**

- Vari�veis
- Operadores
- La�os de repeti��o
- Estruturas de decis�es
- Fun��es */

/* Objetivo:

Crie uma fun��o que recebe como par�metro a quantidade de vit�rias e derrotas de um jogador,
depois disso retorne o resultado para uma vari�vel, o saldo de Rankeadas deve ser feito atrav�s do calculo (vit�rias - derrotas)

Se vit�rias for menor do que 10 = Ferro
Se vit�rias for entre 11 e 20 = Bronze
Se vit�rias for entre 21 e 50 = Prata
Se vit�rias for entre 51 e 80 = Ouro
Se vit�rias for entre 81 e 90 = Diamante
Se vit�rias for entre 91 e 100= Lend�rio
Se vit�rias for maior ou igual a 101 = Imortal

## Sa�da

Ao final deve se exibir uma mensagem:
"O Her�i tem de saldo de **{saldoVitorias}** est� no n�vel de **{nivel}**" */

struct personagem{
	char nome [50];
	char classePersonagem[50];
	int vitorias;
	int derrotas;
	char rank[20];
};

int calculoDeVitorias (int vitorias, int derrotas){
	return(vitorias - derrotas);	
}

void calcularRank(struct personagem *p){
	int resultado = calculoDeVitorias(p->vitorias, p->derrotas);
	
	  if (resultado >= 0 && resultado <= 10) {
        strcpy(p->rank, "Ferro");
    } else if (resultado > 10 && resultado <= 20) {
        strcpy(p->rank, "Bronze");
    } else if (resultado > 20 && resultado <= 50) {
        strcpy(p->rank, "Prata");
    } else if (resultado > 50 && resultado <= 70) {
        strcpy(p->rank, "Ouro");
    } else if (resultado > 70 && resultado <= 80) {
        strcpy(p->rank, "Platina");
    } else if (resultado > 80 && resultado <= 90) {
        strcpy(p->rank, "Ascendente");
    } else if (resultado > 90 && resultado <= 100) {
        strcpy(p->rank, "Imortal");
    } else {
        strcpy(p->rank, "Radiante");
    }
}

int main(int argc, char *argv[]) {
	setlocale(LC_ALL, "");
	
	int i, criarPersonagens;
	struct personagem inicial[5];
	
	
	printf("Quantos personagens deseja criar ? ");
	scanf("%d", &criarPersonagens);
	
	for (i=0; i < criarPersonagens;i++){
		printf("Digite o nome do personagem:  " );
		scanf("%s", &inicial[i].nome);
		printf("Escolha a classe do seu personagem. 'Guerreiro', 'Mago', 'Arqueiro':  " );
		scanf("%s", &inicial[i].classePersonagem);
	}
	printf("Informe o numeros de derotas e vit�rias em cada personagem:\n ");
	for (i=0; i < criarPersonagens; i++){
		printf("Informe o numero de vit�rias: ");
		scanf("%d", &inicial[i].vitorias);
		printf("Informe o numero de derrotas: ");
		scanf("%d", &inicial[i].derrotas);
		calcularRank(&inicial[i]);
		printf("O resultado para %s �: %d\n", inicial[i].nome, calculoDeVitorias(inicial[i].vitorias, inicial[i].derrotas));
        printf("O rank para %s �: %s\n", inicial[i].nome, inicial[i].rank);
	}
	
	
	return 0;
}
