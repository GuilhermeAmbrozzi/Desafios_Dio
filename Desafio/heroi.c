#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main(int argc, char *argv[]) {
	setlocale(LC_ALL, "");

	int xp = 0;

	printf("Qual a xp atual do seu Her�i ? ");
	scanf("%d", &xp);
	
	if (xp <= 1000) {
		printf("N�vel do seu Her�i � Ferro!!");
	} else if (xp > 1000 && xp <= 2000) {
		printf("N�vel do seu Her�i � Bronze!!");
	} else if (xp > 2000 && xp <= 5000) {
		printf("N�vel do seu Her�i � Prata Ouro!!");
	} else if (xp > 5000 && xp <= 8000) {
		printf("N�vel do seu Her�i � Platina Diamante!!");
	} else if (xp > 8000 && xp <= 9000) {
		printf("N�vel do seu Her�i � Ascendente!!");
	} else if (xp > 9000 && xp <= 10000) {
		printf("N�vel do seu Her�i � Imortal!!");
	} else {
		printf("N�vel do seu Her�i � Radiante!!");
	}

	return 0;
}

