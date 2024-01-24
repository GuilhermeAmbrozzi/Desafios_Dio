#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main(int argc, char *argv[]) {
	setlocale(LC_ALL, "");

	int xp = 0;
	char nome[50];
	
	printf("Qual o nome do seu Herói ? ");
	scanf("%s", &nome);
	printf("Qual a xp atual do seu Herói ? ");
	scanf("%d", &xp);
	
	if (xp <= 1000) {
		printf("O Herói %s está no nível Ferro!!",nome);
	} else if (xp > 1000 && xp <= 2000) {
		printf("O Herói %s está no nível Bronze!!",nome);
	} else if (xp > 2000 && xp <= 5000) {
		printf("O Herói %s está no nível Prata!!",nome);
	} else if (xp > 5000 && xp <= 7000) {
		printf("O Herói %s está no nível Ouro!!",nome);
	} else if (xp > 7000 && xp <= 8000) {
		printf("O Herói %s está no nível Platina!!",nome);
	} else if (xp > 8000 && xp <= 9000) {
		printf("O Herói %s está no nível Ascendente!!",nome);
	} else if (xp > 9000 && xp <= 10000) {
		printf("O Herói %s está no nível Imortal",nome);
	}else{
		printf("O Herói %s está no nível Radiante",nome);
	}
		
	return 0;
}

