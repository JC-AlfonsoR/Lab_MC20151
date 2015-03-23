/*
Grabar la voz usando comandos de la terminal
*/

#include <stdio.h>

main(){
  printf("Por favor diga su nombre\nTiene 5 segundos\n");
  system("arecord -d 5 test.wav");
  return 0;
}

/*
J. Camilo Alfonso R.
201114819
*/
