PATH:

Here the program clears the environment variables.
But then it sets the path variable to the current directory.
So we can execute programs with execlp from the current 
environment.

So our exploit creats a symlink to /bin/cat in the current
directory (where program path is also placed). Now it is 
possible to run the cat program from the current directory
(via symlink) with the path program.

Next we needed to pass the flag file to the path program, 
so it can be printed via the cat program. 
The path program checks if an argument with the name flag 
is passed. So we couldn't directly pass the flag.txt to
the path program.

So our exploit created a symlink to the flag.txt. The symlink
passes the filter method of the path program and so it was
possible to print the flag.txt file with the cat program
in the path program.