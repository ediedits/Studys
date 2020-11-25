#include <stdio.h>

int main () {

    int minhaidade = 15;          //int criar variavel tipo inteiro
    int maeidade = 40;
    int paiidade = 42;
    int irmaoidade = 9;
    int idadetotal = minhaidade + maeidade + paiidade + irmaoidade;
    int idademedia = idadetotal/4;
    printf ("minha idade e %i.\n",minhaidade);     //para declarar a variavel use %i.
    printf ("a idade total e %i.\n",idadetotal);
    printf ("a idade media da sua familia e %i.\n",idademedia);



    return 0;
}
