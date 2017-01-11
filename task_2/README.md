Dear students!

This is the description of the 'C security challenge'.

READ THIS FILE CAREFULLY.


If any questions occur do not hesitate to contact me via:
. The newsgroup: tu-graz.lv.einfuehrunginformationssicherheit
  . Use this for general questions
. By mail: david.bidner@student.tugraz.at
  . Use this for solution specific questions
. The #bs irc: sigttou
  . Use this for short questions (I am on there 24/7 but not reading all the time)


Basic structure:
. We have multiple challenges
. They differ in difficulty
. You do not need to solve all of them for a positive grade
. There are hints everywhere(!)


How do the challenges work?
(A simple example will be shown @ the tutorial lesson)
. You get the source and a binary
. You are the 'user' the binary has a setuid to '<CHALLENGE>'
. Calling commands via the binary are run as the other user
. For each challenge there's a flag owned by '<CHALLENGE>'
  (The SWEBPWN challenge is a little different)
. Your task is to read those flags
. You can achieve 13 Points from the Challenges
  . You will only get a maximum of 10 so you can leave out one challenge, if you want
  . I've marked the challenges with difficulty levels so you can work from easy to hard


The challenges:
  BUF(0.5 pts) - LEVEL 0:
    - get some knowledge of the C memory layout (the stack)
    - look at the source
    - write an exploit, get the flag
  PATH(0.5 pts) - LEVEL 0:
    - You can basically call commands with this one
    - But the input is filtered
    - Read man pages, get the flag
  SECBUF(3 pts) - LEVEL 5:
    - Look at the source, run the program
    - Is the code as secure as it states?
    - Show it isn't, get the flag
  UAF(3 pts) - LEVEL 5:
    - Look up 'use after free'
    - Look up how malloc works
    - Look up how objects are stored
    - Write an uaf exploit, get the flag
  SWEBPWN(3 pts) - LEVEL 3:
    - This is the sweb you know from the BS lecture
    - Checkout https://github.com/sigttou/sweb-1 
    - Switch to the 'swebpwn' branch
    - This time the flag is hidden in kernel memory
    - The 'getinfo' syscall will tell you at what address
    - Change the 'getinfo.c' file in 'userspace/tests/'
    - Read the kernel memory from userspace, get the flag
  STREAMME(3 pts) - LEVEL 2:
    - There is a new sound streaming service in the making
    - The code currently written is still in alpha state
    - After starting the binary it will listen on port 1337
    - It will only serve OGG vorbis files


Is there a flag format we can look for?
. IIS{/* some string */}
. In your VM the flag will be IIS{THIS_IS_A_DUMMY}


What about the VM?
. Find the link in the slides.
. ASLR is disabled, see '/etc/sysctl.conf'
. The username is 'iis' with the password 'iis', without the '
. On the desktop you'll find a folder IIS_C_1617
. It's a git repository with a configured readonly account
. It includes all challenges besides the SWEBPWN one
. There's another folder called sweb-1 for that on the desktop, it is the checked out repo
. In case you need to update(!), it will be announced by mail to 'git pull'
  . With the `make` command the binary will be rebuilt and its UID will be set correctly
. I set up tools needed to solve the challenges
  . If you need any other software on the test system for your exploit to work please send me a mail


How do I hand in my solutions?
(An example will be shown @ the tutorial lesson)
. Your exploit should work without user interaction 
  . It should print the flag in the end
. For each level create an exploit and describe it
. It will be checked by me and run on the reference system
. If the flag is found you will be awarded the full points
  . Other cases will be discussed at the assignment talk


What does the format of of the hand in look like?
. In the end you should hand in a submission.zip file to Stics
  . This archive should contain all exploits and writeups
    . For every <CHALLENGE> there should be a folder:
      . <challenge>/exploit.sh or <challenge>/exploit.py
      . <challenge>/readme.pdf or <challenge>/readme.txt
    . For the SWEBPWN challenge there should be a folder:
      . SWEBPWN/getinfo.c
      . SWEBPWN/readme.pdf or SWEBPWN/readme.txt
. Your submission will be tested automatically
  . If your submission fails, I'll do a manual check


Any notes on grading?
. You can achieve 10 points within this challenge
. The quality of your 'writeups' can give you extra points (not more than 10 points overall) 


Good Luck, and have fun hacking /* TODO: Insert some quality, nice emoji here */


Hints for challenges (This may be updated during the assignment):
SECBUF:
  . Study man pages, especially on what is the stack and how much space it has
  . I recommend to do this challenge in the end
SWEBPWN:
  . Can the kernel run code which is in userland?
    . Do we really need shellcode / asm for this challenge?
  . We do not have ASLR in basic sweb.
    . You can change syscalls to try stuff out!
