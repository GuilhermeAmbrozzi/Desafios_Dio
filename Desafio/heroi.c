#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main(int argc, char *argv[]) {
	setlocale(LC_ALL, "");

	int xp = 0;

	printf("Qual a xp atual do seu Herói ? ");
	scanf("%d", &xp);
	
	if (xp <= 1000) {
		printf("Nível do seu Herói é Ferro!!");
	} else if (xp > 1000 && xp <= 2000) {
		printf("Nível do seu Herói é Bronze!!");
	} else if (xp > 2000 && xp <= 5000) {
		printf("Nível do seu Herói é Prata Ouro!!");
	} else if (xp > 5000 && xp <= 8000) {
		printf("Nível do seu Herói é Platina Diamante!!");
	} else if (xp > 8000 && xp <= 9000) {
		printf("Nível do seu Herói é Ascendente!!");
	} else if (xp > 9000 && xp <= 10000) {
		printf("Nível do seu Herói é Imortal!!");
	} else {
		printf("Nível do seu Herói é Radiante!!");
	}

	return 0;
}

