#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

void func(int key)
{
  char overflowme[128];
  printf("overflow me : ");
  gets(overflowme);

  if(key == 0xcafebabe)
  {
    printf("You did it!\n");
    execl("/bin/cat", "cat", "flag.txt", NULL);
  }
  else
    printf("Nope. %x\n", key);
}

int main(int argc, char* argv[])
{
  func(0xdeadbeef);
  return 0;
}

