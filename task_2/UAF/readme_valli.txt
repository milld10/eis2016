UAF challenge

The solution for printing the flag is to override the internal 
buffer pointer in the std::string object to let it point to the buffer
of the flag.
This can be done because the after an animal is deleted and its buffer
freed, the vector holding the animals is not being shrunk.
So the memory area can be overwritten by a fake animal structure.
We created such a fake structure in which the internal std::string
buffer pointer points to a memory area where our flag was loaded.
When now the name of the "animal" is printed, it actually prints out
the flag.

Our exploit does the following steps:
1) Create a script to input the program which does:
	1.1) Create a symlink from the flag to a filename that will be used
				as input for the program
	1.2) Load the food (containing the flag)
	1.3) Create a cow
	1.4) Delete the cow
	1.5) Create a symlink from out flag to the very filename that is
				used as input
	1.6) Load the food (containing the fake structure)
	1.7) Print the name of the cow
2) Start the script
3) Via Piping use the output of the script as input to the program
4) grep for the flag

