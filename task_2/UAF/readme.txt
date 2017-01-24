UAF:

the exploit starts the uaf program with the following arguments:
./uaf 56 food.txt
food.txt - needed to get the flag and some code into the program
56 - lenght of animal object

Then our exploit creates a symlink named food.txt
to the flag.txt. Then the exploit enters 4 so that the
flag.txt is loaded into the program (via the symlink 
food.txt). Then we noted where on the heap the flag was
stored (if you do the same steps as mentioned, the flag
will always be stored on the same position because there
is no security mechanism enabled)

Then the exploit creates a cow with the following commands:
1 - command for creating a cow
cow - cow name
loc - location name

The cow/animal object is placed on the heap and contains 56 bytes. It consists
of the vtable(4 Bytes), the space variable (4 Bytes) and the two string
variables location and name (each 24 Bytes).

Afterwards the exploit deletes the created cow with the following commands:
3 - command for deleting 
0 - index of the cow pointer

Next the exploit deletes the symlink to the flag.txt and
creates a new food.txt file. This file consists of 56 Bytes
(as long as the cow object). The exploit uses this file to 
load it into the uaf program. Owing to the fact it is 56 Bytes
long, it is placed where the previous deleted 56 Bytes cow 
object was stored when it is loaded into the heap. So the 
exploit uses this file to get flag information on the heap.

The food.txt file looks as follows:
The first 4 Bytes of the food.txt file represent the 4 Bytes of the 
vtable of the deleted cow object (we needed to do that otherwise it 
was not possible to "reuse" the cow object). The next 4 Bytes 
represents the integer variable space. Here you can find the values
0x00 in the file. The following 4 bytes represent the address where 
the location string is stored. Here is the address of the flag in the heap 
placed (The address is represented in reverse order - address read
from bottom to top). The other places in the 56 bytes file were trivial
because we already had overwritten the location. So the exploit 
fills it with some random numbers.

When the exploit finished creating the food.txt, it loads it into the
uaf program. It is placed where the previous deleted cow object 
was placed. So the object has been overwritten.

Now the exploit enters the command to print the information of the
object at index 0 in the storage vector. Now the flag is printed
because we pointed the location of the deleted cow object to the
flag address on the heap.

All addresses that we needed (vtable of cow object, flag on heap etc.) 
we looked up with the gdb.

We first tried another approach. There we overwrote the vtable of
the cow object so that when we executed the treatment method of
the cow object we got to the animal::shell method. But then 
we were not able to push parameters on the stack that the execl
could execute.