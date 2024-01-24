#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>

/* Calculadora de partidas Rankeadas
**O Que deve ser utilizado**

- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões
- Funções */

/* Objetivo:

Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)

Se vitórias for menor do que 10 = Ferro
Se vitórias for entre 11 e 20 = Bronze
Se vitórias for entre 21 e 50 = Prata
Se vitórias for entre 51 e 80 = Ouro
Se vitórias for entre 81 e 90 = Diamante
Se vitórias for entre 91 e 100= Lendário
Se vitórias for maior ou igual a 101 = Imortal

## Saída

Ao final deve se exibir uma mensagem:
"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**" */

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
	printf("Informe o numeros de derotas e vitórias em cada personagem:\n ");
	for (i=0; i < criarPersonagens; i++){
		printf("Informe o numero de vitórias: ");
		scanf("%d", &inicial[i].vitorias);
		printf("Informe o numero de derrotas: ");
		scanf("%d", &inicial[i].derrotas);
		calcularRank(&inicial[i]);
		printf("O resultado para %s é: %d\n", inicial[i].nome, calculoDeVitorias(inicial[i].vitorias, inicial[i].derrotas));
        printf("O rank para %s é: %s\n", inicial[i].nome, inicial[i].rank);
	}
	
	
	return 0;
}
