Buf:

Our exploit just creates a output that is passed to the program 
as stdin argument.

The output consists of 3 parts. 
The first part just fills the array overflowme with 'a' characters.
Then the output contains 16 bytes of 'b' characters. This
overwrites everything between the end of the array overflowme and
the argument key.
Last but not least the output contains 0xcafebabe. This will be
used to overwrite the argument key.

We had to take care that 0xcafebabe is written to the output in reverse
order. So 0xbebafeca was written to the output. That needed to be 
done because the parameter is read from the bottom to the top.

When this output is passed to the program buf the argument key
is overwritten with 0xcafebabe and if check will be true and
the flag is returned.