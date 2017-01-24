STRAMME Challenge

DISCLAIMER: The exploit did not work as of the deadline.

There are two threads running on the server.
The first one processes requests, loads a requested file, checks this 
file, (if it is valid) creates a info datastructure and hands it to the 
second thread.

The second one then just sends a file specified by the datastructure
to the receiver. 

The exploit is based on the fact, that both threads are using the same
filesize variable in the info structure *without* locking.

If a (small and valid) file is requested, the info structure based on the small file is written.

If a second (big and valid) file is requested *before* the sending has begun, the filesize parameter is overwritten.

This will cause the sending thread to send starting at the old buffer 
pointer, but rather than sending until the small file has reached its
end, it keeps sending. So the requester receives the internals of a 
piece of heap memory.

If on this heap memory the flag is requested, it can be read by the 
requester, which leads to the following attack procedure:

1) request flag.txt
	This will fail, but the flag now is located at the memors
2) request a small file
3) request a big file

The attack then and only then succeeds, if the sending thread was 
*not* scheduled before the second request was processed by the main
thread. 
Otherwise the sending has already started and a change in the filesize
has no effect as the sending OS function is called by value.

However this is very unlikely as the main thread calls a OS function
that awaits incoming requests, which internally yields. If this 
happens, the other thread begins with its execution.

We then tried several combination of requesting threads and busy
threads, in the hope that the OS will decide to *not* schedule our
sending thread, but with no success.
