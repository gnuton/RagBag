# Assembly (x86) #


## Registers ##
If we run an application, and we insert a breakpoint somewhere in hte code, we can check the status of registers
```
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
```

### Disassembling a simple function ###
```cpp
#include <stdio.h>

int myFunc() {
  return 12;
}

int main() {
  myFunc();
}
```
Let's disassemble the code produced by GCC using Intel syntax (More readable than AT&T one)

```assembly
gnuton@biggoliath:/tmp$ objdump -D a.out -Mintel | grep -A 20 myFunc
00000000004004ed <myFunc>:
  4004ed:	55                   	push   rbp
  4004ee:	48 89 e5             	mov    rbp,rsp
  4004f1:	b8 0c 00 00 00       	mov    eax,0xc  // Copy 12 (0xC) to EAX register
  4004f6:	5d                   	pop    rbp
  4004f7:	c3                   	ret             // Returns value of EAX and execution to caller

00000000004004f8 <main>:
  4004f8:	55                   	push   rbp
  4004f9:	48 89 e5             	mov    rbp,rsp
  4004fc:	b8 00 00 00 00       	mov    eax,0x0         // copy 0 to EAX
  400501:	e8 e7 ff ff ff       	call   4004ed <myFunc> // calls myFunc at address 4004ed
  400506:	5d                   	pop    rbp
  400507:	c3                   	ret                   // returns EAX
```

### Disassembling an Hello world ###
```cpp
#include <stdio.h>

int main() {
  printf("Hello world\n");
  return 0; 
}
```
Let's disassemble it! :D
```assembly
gnuton@biggoliath:/tmp$ objdump -D a.out -Mintel | grep -A 20 main
000000000040052d <main>:
  40052d:	55                   	push   rbp               // function prologue
  40052e:	48 89 e5             	mov    rbp,rsp           // function prologue
  400531:	bf d4 05 40 00       	mov    edi,0x4005d4
  400536:	e8 d5 fe ff ff       	call   400410 <puts@plt> // Calls puts in the PLT
  40053b:	b8 00 00 00 00       	mov    eax,0x0            
  400540:	5d                   	pop    rbp               // function epilogue
  400541:	c3                   	ret    
```
In the code above, the compiler has replaced printf with puts function since there is no formatting implied
and puts is faster.
The puts function is in the PLT or [Program Linker Table](http://www.iecc.com/linker/linker10.html) and 0x400410 is the address that points to the entry of such function.
More info about function prologue and epilogue can be found prologue [here ](https://en.wikipedia.org/wiki/Function_prologue)
A trick to visualize better our disassembled code (if we have the source code) is to compile it
using -g option of gcc.

```assembly
gnuton@biggoliath:/tmp$ objdump -S  a.out -M intel
000000000040052d <main>:
#include <stdio.h>


int main() {
  40052d:	55                   	push   rbp
  40052e:	48 89 e5             	mov    rbp,rsp
  printf("Hello world\n");
  400531:	bf d4 05 40 00       	mov    edi,0x4005d4
  400536:	e8 d5 fe ff ff       	call   400410 <puts@plt>
  return 0; 
  40053b:	b8 00 00 00 00       	mov    eax,0x0
}
  400540:	5d                   	pop    rbp
  400541:	c3                   	ret   
```
We can also use gdb to dissassemble our code (here in AT&T syntax)
```assembly
gnuton@biggoliath:/tmp$ gdb -q a.out
Reading symbols from a.out...done.
(gdb) list
No symbol table is loaded.  Use the "file" command.
(gdb) quit
gnuton@biggoliath:/tmp$ gdb -q a.out
Reading symbols from a.out...done.
(gdb) list
1	#include <stdio.h>
2	
3	
4	int main() {
5	  printf("Hello world\n");
6	  return 0; 
7	}
(gdb) disassemble main
Dump of assembler code for function main:
   0x000000000040052d <+0>:	push   rbp        
   0x000000000040052e <+1>:	mov    rbp,rsp
   0x0000000000400531 <+4>:	mov    edi,0x4005d4
   0x0000000000400536 <+9>:	call   0x400410 <puts@plt>
   0x000000000040053b <+14>:	mov    eax,0x0
   0x0000000000400540 <+19>:	pop    rbp
   0x0000000000400541 <+20>:	ret    
End of assembler dump.
(gdb) break main                               // Sets a breakpoint to main
Breakpoint 1 at 0x400531: file a.c, line 5.
(gdb) run                                      // runs the app which,but execution stops at breakpoint
Starting program: /tmp/a.out 

Breakpoint 1, main () at a.c:5
5	  printf("Hello world\n");
(gdb) info register rip                        //RIP (Register Instruction Point) 
                                               //shows the current executed instruction
rip            0x400531	0x400531 <main+4>      // 0x400531 is the address stored in RIP
```

### xxx ###
```cpp
```
```assembly

```



# Tips #
If you like to have Intel syntax in GDB just run this.
```
echo "set disassembly-flavor intel" > ~/.gdbinit
```
