#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main(int argc, char *argv[]) {
	setlocale(LC_ALL, "");

	int xp = 0;
	char nome[50];
	
	printf("Qual o nome do seu Her�i ? ");
	scanf("%s", &nome);
	printf("Qual a xp atual do seu Her�i ? ");
	scanf("%d", &xp);
	
	if (xp <= 1000) {
		printf("O Her�i %s est� no n�vel Ferro!!",nome);
	} else if (xp > 1000 && xp <= 2000) {
		printf("O Her�i %s est� no n�vel Bronze!!",nome);
	} else if (xp > 2000 && xp <= 5000) {
		printf("O Her�i %s est� no n�vel Prata!!",nome);
	} else if (xp > 5000 && xp <= 7000) {
		printf("O Her�i %s est� no n�vel Ouro!!",nome);
	} else if (xp > 7000 && xp <= 8000) {
		printf("O Her�i %s est� no n�vel Platina!!",nome);
	} else if (xp > 8000 && xp <= 9000) {
		printf("O Her�i %s est� no n�vel Ascendente!!",nome);
	} else if (xp > 9000 && xp <= 10000) {
		printf("O Her�i %s est� no n�vel Imortal",nome);
	}else{
		printf("O Her�i %s est� no n�vel Radiante",nome);
	}
		
	return 0;
}

