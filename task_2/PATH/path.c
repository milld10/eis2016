#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

void delenv();
int filter(char* c);

extern char** environ;

int main(int argc, char* argv[], char** envp)
{
  delenv();
  putenv("PATH=/this_is_your_only_way_out:.:\)");

  unsigned char i = 1;
  while(argv[i])
  {
    if(filter(argv[i]))
      return 0;
    printf("%s\n", argv[i++]);
  }
  
  execlp(argv[1], argv[2], argv[3], NULL);

  return 0;
}

void delenv()
{
  char** p;
  for(p=environ; *p; p++) memset(*p, 0, strlen(*p));
}

int filter(char* str)
{
  int cnt=0;
  cnt += strstr(str, "=")!=0;
  cnt += strstr(str, "PATH")!=0;
  cnt += strstr(str, "export")!=0;
  cnt += strstr(str, "/")!=0;
  cnt += strstr(str, "`")!=0;
  cnt += strstr(str, "flag")!=0;
  return cnt;
}

