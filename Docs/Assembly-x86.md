# Assembly (x86) #


## Registerss ##
If we run an application, and we insert a breakpoint somewhere in hte code, we can check the status of registers
'''
(gdb) info registers
GENERAL PURPOSE REGISTERS:
rax            0x40052d	4195629                     Accumulator
rbx            0x0	0                               Base
rcx            0x0	0                               Counter
rdx            0x7fffffffdde8	140737488346600       Data

GENERAL PURPOSE BUT KNOWN AS POINTERS AND INDEXES
rsi            0x7fffffffddd8	140737488346584       Source index - points to memory where data to be read is
rdi            0x1	1                               Destination index - points to memory where data to be written is
rbp            0x7fffffffdcf0	0x7fffffffdcf0        Base Pointer
rsp            0x7fffffffdcf0	0x7fffffffdcf0        Stack Pointer

r8             0x7ffff7dd4e80	140737351863936
r9             0x7ffff7dea560	140737351951712
r10            0x7fffffffdb80	140737488345984
r11            0x7ffff7a36dd0	140737348070864
r12            0x400440	4195392
r13            0x7fffffffddd0	140737488346576
r14            0x0	0
r15            0x0	0

rip            0x400531	0x400531 <main+4>           Instruction pointer- points to current executed instruction
  
EFLAGS registers - used to compare memory segmentations since the memory is split in several segments
eflags         0x246	[ PF ZF IF ]
cs             0x33	51
ss             0x2b	43
ds             0x0	0
es             0x0	0
fs             0x0	0
'''
