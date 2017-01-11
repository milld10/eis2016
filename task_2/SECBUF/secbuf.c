/* It's really easy to write secure software. */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int canary;
char* buffer;
int size;

int test_it(void);
void cls_input(void);
int chk_canary(int);

int main(void)
{
  printf("To prevent buffer overflows we need 2 things:\n");
  printf("a) the size of the buffer, before writing\n");
  printf("b) a secure way to fill the buffer\n\n");
  return test_it();   
}

int test_it()
{
  printf("Length of your buffer?(byte) : ");
  scanf("%d", &size);
  cls_input();
  printf("Your random canary: ");
  scanf("%d", &canary);
  cls_input();

  buffer = alloca( size + 4 );  /* We need space for the canary */

  memcpy(buffer+size, &canary, 4);
  printf("You can fill your buffer now: \n");
  fgets(buffer, size, stdin);   /* This can't be exploited */

  chk_canary( *((int*)(buffer+size)) );
  return 0;
}

void cls_input(void)
{
  char c;
  do
  {
    c = getchar();
  } while (c != '\n' && c != EOF);
}

/* This will show you, that the buffer won't overflow */
int chk_canary(int i)
{
  int check = i ^ canary;
  int cset = i;
  int ccheck = canary;

  printf("canary set : %d\n", cset);
  printf("canary check : %d\n", ccheck);

  if(check)
    printf("o_O How could this happen?\n");
  else
    printf("You see, it is easy to write secure software\n");
  return check;
}

