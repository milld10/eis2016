SWEPPWN Challenge

This challenge uses a bug in the read-syscall.
The syscall does not check whether the given buffer it
should read to is in the kernelspace or not.

So after checking at which exact position the correct 
location of the return address used by the kernelspace
read-function lies, we could inject or own pointer there.

Therefore we wrote the pointer to a file. 
This file was read by the syscall and the buffer it should read
to points to the return address on the kernel stack.

The kernelspace read function returns to our userspace function,
which just prints out the flag, which position is known beforehand.
