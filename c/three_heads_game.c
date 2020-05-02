#include <stdlib.h>
#include <time.h>
#include <stdio.h>

int main(){
  printf("Let's flip a coin!\n");

  int heads = 0;
  int toss = 0;
  srand(time(NULL));

  while (heads < 3)
  {
      int flip = (rand() % 2);

      if (flip == 1)
      {
          printf("heads\n");
          heads++;
      }
      else 
      {
          printf("Tails\n");
          heads = 0;
      }
      toss++;
  }

  printf("\nIt took %d tosses to get 3 concecutive heads.\n", toss);
  
  return 0;
}