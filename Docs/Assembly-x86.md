# Assembly Linux-x86 #
In this document we will see how to write a NASM assembly application on linux for X86-32 and maybe quickly showing how it looks like on x86-64 too.
Let's getting started! ÖD

## A minimal NASM app ##
The layout of an ELF NASM app looks like this
```assembly
section .text
    global _start
 
_start:
    ; do something here
section .data
    ; initialized data
 
 
```

## Hello World ##
Let's put some code in such 
```assembly
section	.text
   global_start   ;must be declared for linker (ld)
	
_start:	          ;tells linker entry point
   mov	edx,len   ;message length
   mov	ecx,msg   ;message to write
   mov	ebx,1     ;file descriptor (stdout)
   mov	eax,4     ;system call number (sys_write)
   int	0x80      ;call kernel
	
   mov	eax,1     ;system call number (sys_exit)
   int	0x80      ;call kernel

section	.data
msg db 'Hello, world!', 0xa  ;string + /n 
len equ $ - msg    ;string length
```
## Building NASM code ##
```bash
# Builds a .o Object file
nasm -f elf a.asm
# Links the object to libs
ld -m elf_i386 -s -o a a.o
```

## Reading the generated ELF ##
Readelf shows the sections of the elf layout.
.text section shows the flag AX, where X means it's executable.

```assembly
gnuton@biggoliath:~/ASM$ readelf --all hw
ELF Header:
  Magic:   7f 45 4c 46 01 01 01 00 00 00 00 00 00 00 00 00 
  Class:                             ELF32
  Data:                              2's complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI Version:                       0
  Type:                              EXEC (Executable file)
  Machine:                           Intel 80386
  Version:                           0x1
  Entry point address:               0x8048080
  Start of program headers:          52 (bytes into file)
  Start of section headers:          200 (bytes into file)
  Flags:                             0x0
  Size of this header:               52 (bytes)
  Size of program headers:           32 (bytes)
  Number of program headers:         2
  Size of section headers:           40 (bytes)
  Number of section headers:         4
  Section header string table index: 3

Section Headers:
  [Nr] Name              Type            Addr     Off    Size   ES Flg Lk Inf Al
  [ 0]                   NULL            00000000 000000 000000 00      0   0  0
  [ 1] .text             PROGBITS        08048080 000080 00001d 00  AX  0   0 16
  [ 2] .data             PROGBITS        080490a0 0000a0 00000e 00  WA  0   0  4
  [ 3] .shstrtab         STRTAB          00000000 0000ae 000017 00      0   0  1
Key to Flags:
  W (write), A (alloc), X (execute), M (merge), S (strings)
  I (info), L (link order), G (group), T (TLS), E (exclude), x (unknown)
  O (extra OS processing required) o (OS specific), p (processor specific)

There are no section groups in this file.

Program Headers:
  Type           Offset   VirtAddr   PhysAddr   FileSiz MemSiz  Flg Align
  LOAD           0x000000 0x08048000 0x08048000 0x0009d 0x0009d R E 0x1000
  LOAD           0x0000a0 0x080490a0 0x080490a0 0x0000e 0x0000e RW  0x1000

 Section to Segment mapping:
  Segment Sections...
   00     .text 
   01     .data 

There is no dynamic section in this file.
```

## Let's have a look at how it looks disassembled ##
objectdump  allows us to have a look at it (objdump  -Mintel -D helloworld.o)
```assembly
a.o:     file format elf32-i386


Disassembly of section .text:

00000000 <_start>:
   0:	ba 0e 00 00 00       	mov    edx,0xe
   5:	b9 00 00 00 00       	mov    ecx,0x0
   a:	bb 01 00 00 00       	mov    ebx,0x1
   f:	b8 04 00 00 00       	mov    eax,0x4
  14:	cd 80                	int    0x80
  16:	b8 01 00 00 00       	mov    eax,0x1
  1b:	cd 80                	int    0x80

Disassembly of section .data:

00000000 <msg>:
   0:	48                   	dec    eax
   1:	65                   	gs
   2:	6c                   	ins    BYTE PTR es:[edi],dx
   3:	6c                   	ins    BYTE PTR es:[edi],dx
   4:	6f                   	outs   dx,DWORD PTR ds:[esi]
   5:	2c 20                	sub    al,0x20
   7:	77 6f                	ja     78 <len+0x6a>
   9:	72 6c                	jb     77 <len+0x69>
   b:	64 21 0a             	and    DWORD PTR fs:[edx],ecx
```

You can build your assembly code using the 64 bit registers too
```
# Builds a .o Object file
nasm -f elf64 a.asm
# Links the object to libs
ld -o a a.o

```
## Memory segments ##
The memory is devided into indipendent segments.
* DATA - stores data used by the program
	* .data - Contains initialized data (costants)
	 	- instruction used EQU, DB, DW, DD, DQ and DT
	* .bss - Stores uninitialized data (vars)
	       - RESB, RESW, RESD, RESQ and REST reserve uninitialized space in memory for your variables
* TEXT - stores the instruction codes

And here how the sections looks like in the source code
```assembly
section .data
	message:    db 'Hello world!'     ; message = 'Hello world!' as Bytes
	msglength:  equ 12                ; msglength  = 12 as constant
	
section .bss
	number:     resb    1             ; Reserves 1 byte
	bignum:     resw    1             ; Reserves 1 word (1 word = 2 bytes)
	realarray:  resq    10            ; Reserves an array of 10 reals
	
section .text
	global _start
_start:
	pop    ebx        ; Here is the where the program actually begins	
```

### Registers ###
A register is a small amount of data storage inside a processor which makes it fast to access to data.

#### X86 register ####

* GENERAL PURPOSE (There are 16 types in 64 bit and )
	* DATA REGISTERs (64 bit R*X, 32-bit E*X, 16-bit *X, 8-bit *L, where * is A,B,C,D)
		* AX - Accumulator - usually contains the syscall number
		* BX - Base
		* CX - Counter
		* DX - Data - 
	* POINTER REGISTERs (32-bit EIP/ESP/BSP, 16-bit IP/SP/BP)
		* IP - Instruction Pointer - stores offset address of the next instruction to be executed
		* SP - Stack Pointer -address of top of the stack. Data is added and removed only from the top. So it changes everytime a word or address is pushed or popped off the stack.
		* BP - Base/Frame Pointer - points to ESP when a function starts. 
	* INDEX REGISTERs
		* SI - Source Index -
		* DI - Destination Index -
* CONTROL
	* OF - Overflow flag
	* DF - Direction flag
	* IF - Interrupt flag
	* TF - Trap flag
	* SF - Sign flag
	* ZF - Zero flag
	* AF - Auxiliary carry flag
	* PF - Parity flag
	* CF - Carry flag
* SEGMENT
	* CS - Code Segment - starting address of the code segment
	* DS - Data Segment - starting address of the data segment
	* SS - Stack Segment -starting address of the stack
	* ES - Extra Segment
	* FS - Additional segment to store data
	* GS - Additional segment to store data

64-bit processor have etra registers:  r8, r9, r10, r11, r12, r13, r14, r15

Note that in order to reference any memory location in a segment, the processor combines the segment address in the segment register with the offset value of the location.

### SYSTEM CALLS ###
Are APIs that expose some kernel function to  user space.
A good list with registers used by these syscall can be found [here] (https://filippo.io/linux-syscall-table/)
You can find the name of the syscalls in /usr/include/asm/unistd_32.h and /usr/include/asm/unistd_64.h

In order to use them:
1. Insert the syscall number into the EAX/RAX register
2. Insert the arguments data into some specific registers (see link above)
3. call the kernel using generating a software interrupt using the instruction int 80h 
```assembly
; In this example we call the syscall sys_write in a i32 system
; ssize_t sys_write(unsigned int fd, const char * buf, size_t count)

; Step 1
mov	eax,4     ;system call number (sys_write)
; Step 2
mov	ebx,1     ;file descriptor (stdout)
mov	ecx,msg   ;message to write
mov	edx,len   ;message length

; Step 3
int	0x80      ;call kernel
```
Another examples
```assembly
; Using syscalls. testing execve see man 2 execve

section .data
  filename: db "/bin/bash"

section .text
  global _start

_start:
  ;int execve(const char *filename, char *const argv[], char *const envp[]);
  ; according to man 2 syscall
  ; arch/ABI   arg1   arg2   arg3   arg4   arg5   arg6   arg7
  ; i386       ebx    ecx    edx    esi    edi    ebp    -
  ; execve = 11 according to  /usr/include/asm/unistd_32.h
  mov eax, 0xb ; set ebx to 11
  mov ebx, filename
  xor ecx, ecx ; null pointer 
  xor edx, edx ; null pointer
  int 0x80
```

### Data types ###
The following are used to declare initialized data
* DB - Bytes (1Byte - 8bit)
* DW - Words   (2 Byte -16bit)
* DD - Double word (4B)
* DQ - Quad word(8B)
* DO - Octo word (16B)
* DY - (32B)
* DZ - (64B)
```assembly
; Initiliaze 3 bytes
db 0x01,0x02,0x03
dw 0x1234
```
unitialized data is declred using the RES* pseudo-istructions
* RESB - Declares uninitaliazed byte
* RESW - Declares uninitaliazed word
* RESD ...
* RESQ
* REST
* RESO
* RESY
* RESZ

Costants are declared using 
* EQU
```assembly
mycost equ 3 ; decleare mycost = 3
```

you can include a binary file
* INCBIN

you can repeat instruction or data
* TIMES

### Memory Addressing ###
Every programming language has functions that take arguments.
In assembly OPERANDS are the arguments of this "functions".

Those can be passed in several ways
```assembly
; 1 Direct offset addressing
wordarr dw 'A', 66, 'C'
mov	ecx, wordarr+3; mov C to ECX

; 2 Direct memory addressing or displacement-only - specifies the address
mov    ecx,0x80490a0; by default this is the offset into the data segment
                    ; for offset in a different segment use segment_name:[0xoffset] 

; 3 Indirect memory addressing

```

# Examples #
## Read and write from console #
```assembly
section	.text
   global_start   ;must be declared for linker (ld)
	
_start:	          ;tells linker entry point
   ; Writes insert a number
   mov	eax,4     ;sys_write
   mov	ebx,1     ;stdout
   mov	ecx,msg   ;message to write
   mov	edx,len   ;message length
   int	0x80

   ; Reads in the 3 chars
   mov eax, 3     ;sys_read
   mov ebx, 0     
   mov ecx, mstr
   mov edx, mstrl  
   int	0x80      ;call kernel
   
   ; Writes out the char
   mov	eax,4     ;sys_write
   mov	ebx,1     ;stdout
   mov	ecx,mstr   ;message to write
   mov	edx,mstrl   ;message length
   int	0x80

   ; exit
   mov	eax,1     ;system call number (sys_exit)
   mov  ebx,0
   int	0x80      ;call kernel

section .bss
mstr resb mstrl     ;preallocate 128 bytes

section	.data
msg db 'Insert a number', 0xa  ;our dear string
len equ $ - msg    ;length of our dear string
mstrl equ 3        ; length of the buffer to read
```

## Disassembling an array #
```assembly
section	.text
   global_start   ;must be declared for linker (ld)
	
_start:	          ;tells linker entry point

   mov	edx,2   ;message length
   mov	ecx, wordarr   ;message to write
   mov	ebx,1     ;file descriptor (stdout)
   mov	eax,4     ;system call number (sys_write)
   int	0x80      ;call kernel
	
   mov	eax,1     ;system call number (sys_exit)
   int	0x80      ;call kernel

section	.data
wordarr dw 'A', 66, 'C', 'D','F','G','H','I'
```

```assembly
gnuton@biggoliath:~/ASM/HelloWorld$objdump -D b -Mintel

b:     file format elf32-i386
Disassembly of section .text:

08048080 <.text>:
 8048080:	ba 02 00 00 00       	mov    edx,0x2
 8048085:	b9 a0 90 04 08       	mov    ecx,0x80490a0
 804808a:	bb 01 00 00 00       	mov    ebx,0x1
 804808f:	b8 04 00 00 00       	mov    eax,0x4
 8048094:	cd 80                	int    0x80
 8048096:	b8 01 00 00 00       	mov    eax,0x1
 804809b:	cd 80                	int    0x80

Disassembly of section .data:

080490a0 <.data>:
 80490a0:	41                   	inc    ecx ; A
 80490a1:	00 42 00             	add    BYTE PTR [edx+0x0],al ; B
 80490a4:	43                   	inc    ebx ; C
 80490a5:	00 44 00 46          	add    BYTE PTR [eax+eax*1+0x46],al; D F 
 80490a9:	00 47 00             	add    BYTE PTR [edi+0x0],al; G 
 80490ac:	48                   	dec    eax; H
 80490ad:	00 49 00             	add    BYTE PTR [ecx+0x0],cl; I
```
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

More info about function prologue and epilogue can be found [here ](https://en.wikipedia.org/wiki/Function_prologue).

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
(gdb) disas main
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

# Analizing Function prologue #
```assembly

Function Prologue
Goes from 0 to the offset +6.
Saves the base pointer EBP in the stack (PUSH EBP).


Memory management in Linux (x86-32)

+-----------------+ 0xFFFFFFFF
|  Kernel Space   |              1GB 
+-----------------+ 0xC0000000 
|                 |              3GB <-- ESP
|                 |
|                 |
|   User Space    |            
|                 |
|                 |
|                 |
|                 |
|                 |
+-----------------+ 0x00000000        <--EBP

gdb a.out
(gdb) disas main
Dump of assembler code for function main:
   0x0804844d <+0>:	push   ebp
   0x0804844e <+1>:	mov    ebp,esp
   0x08048450 <+3>:	and    esp,0xfffffff0
   0x08048453 <+6>:	sub    esp,0x20
   0x08048456 <+9>:	mov    DWORD PTR [esp+0x1c],0x96
   0x0804845e <+17>:	cmp    DWORD PTR [ebp+0x8],0x1
   0x08048462 <+21>:	jg     0x8048470 <main+35>
   0x08048464 <+23>:	mov    DWORD PTR [esp],0x8048540
   0x0804846b <+30>:	call   0x8048310 <printf@plt>
   0x08048470 <+35>:	mov    eax,DWORD PTR [ebp+0xc]
   0x08048473 <+38>:	add    eax,0x4
   0x08048476 <+41>:	mov    eax,DWORD PTR [eax]
   0x08048478 <+43>:	mov    DWORD PTR [esp],eax
   0x0804847b <+46>:	call   0x8048340 <atoi@plt>
   0x08048480 <+51>:	add    DWORD PTR [esp+0x1c],eax
   0x08048484 <+55>:	mov    eax,DWORD PTR [ebp+0xc]
   0x08048487 <+58>:	add    eax,0x4
   0x0804848a <+61>:	mov    eax,DWORD PTR [eax]
   0x0804848c <+63>:	mov    edx,DWORD PTR [esp+0x1c]
   0x08048490 <+67>:	mov    DWORD PTR [esp+0x8],edx
   0x08048494 <+71>:	mov    DWORD PTR [esp+0x4],eax
   0x08048498 <+75>:	mov    DWORD PTR [esp],0x8048559
   0x0804849f <+82>:	call   0x8048310 <printf@plt>
   0x080484a4 <+87>:	mov    eax,0x0
   0x080484a9 <+92>:	leave  
   0x080484aa <+93>:	ret    
End of assembler dump.
(gdb) break *0x0804844d
Breakpoint 1 at 0x804844d
(gdb) define hook-stop
Type commands for definition of "hook-stop".
End with a line saying just "end".
>disas
>end
(gdb) set step-mode on
(gdb) step 1
The program is not being run.
(gdb) run 10
Starting program: /home/gnuton/ASM/a.out 10
Dump of assembler code for function main:
=> 0x0804844d <+0>:	push   ebp
   0x0804844e <+1>:	mov    ebp,esp
   0x08048450 <+3>:	and    esp,0xfffffff0
   0x08048453 <+6>:	sub    esp,0x20
   ...    
End of assembler dump.

Breakpoint 1, 0x0804844d in main ()
(gdb) info registers
eax            0x2	2
ecx            0x6ab3210f	1790124303
edx            0xffffd024	-12252
ebx            0xf7fb0000	-134545408    
esp            0xffffcffc	0xffffcffc    <+++ STACK POINTER high ~ 0xffffcffc * 1 Byte ~ 4 GB
ebp            0x0	0x0                   <--- BASE POINTER low 
esi            0x0	0
edi            0x0	0
eip            0x804844d	0x804844d <main>
eflags         0x246	[ PF ZF IF ]  <-- ParityFlag, ZeroFlag, InterruptEnableFlag
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) step 1
Dump of assembler code for function main:
   0x0804844d <+0>:	push   ebp
=> 0x0804844e <+1>:	mov    ebp,esp
   0x08048450 <+3>:	and    esp,0xfffffff0
   0x08048453 <+6>:	sub    esp,0x20
   ...

0x0804844e in main ()
(gdb) info registers
eax            0x2	2
ecx            0x6ab3210f	1790124303
edx            0xffffd024	-12252
ebx            0xf7fb0000	-134545408
esp            0xffffcff8	0xffffcff8 <+++ push ebp, increased esp of +4 (4*8 Byte)
ebp            0x0	0x0
esi            0x0	0
edi            0x0	0
eip            0x804844e	0x804844e <main+1> <=== Istruction pointer +1
eflags         0x246	[ PF ZF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) step 1
Dump of assembler code for function main:
   0x0804844d <+0>:	push   ebp
   0x0804844e <+1>:	mov    ebp,esp
=> 0x08048450 <+3>:	and    esp,0xfffffff0
   0x08048453 <+6>:	sub    esp,0x20
   ...  
End of assembler dump.
0x08048450 in main ()
(gdb) info registers
eax            0x2	2
ecx            0x6ab3210f	1790124303
edx            0xffffd024	-12252
ebx            0xf7fb0000	-134545408
esp            0xffffcff8	0xffffcff8
ebp            0xffffcff8	0xffffcff8  <-- EBX points to ESP memory address
esi            0x0	0
edi            0x0	0
eip            0x8048450	0x8048450 <main+3>
eflags         0x246	[ PF ZF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) step 1
Dump of assembler code for function main:
   0x0804844d <+0>:	push   ebp
   0x0804844e <+1>:	mov    ebp,esp
   0x08048450 <+3>:	and    esp,0xfffffff0
=> 0x08048453 <+6>:	sub    esp,0x20
   0x08048456 <+9>:	mov    DWORD PTR [esp+0x1c],0x96
   ....
(gdb) info registers
eax            0x2	2
ecx            0x6ab3210f	1790124303
edx            0xffffd024	-12252
ebx            0xf7fb0000	-134545408
esp            0xffffcff0	0xffffcff0  <++++ the AND has moved ESP of -8
ebp            0xffffcff8	0xffffcff8
esi            0x0	0
edi            0x0	0
eip            0x8048453	0x8048453 <main+6>
eflags         0x286	[ PF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) step 1
Dump of assembler code for function main:
   0x0804844d <+0>:	push   ebp
   0x0804844e <+1>:	mov    ebp,esp
   0x08048450 <+3>:	and    esp,0xfffffff0
   0x08048453 <+6>:	sub    esp,0x20
=> 0x08048456 <+9>:	mov    DWORD PTR [esp+0x1c],0x96
   0x0804845e <+17>:	cmp    DWORD PTR [ebp+0x8],0x1
   ....
(gdb) info registers
eax            0x2	2
ecx            0x6ab3210f	1790124303
edx            0xffffd024	-12252
ebx            0xf7fb0000	-134545408
esp            0xffffcfd0	0xffffcfd0  <++++ the SUB has moved ESP of -32 bytes 
ebp            0xffffcff8	0xffffcff8
esi            0x0	0
edi            0x0	0
eip            0x8048456	0x8048456 <main+9>
eflags         0x282	[ SF IF ]           <------ PF Parity Flag is gone because the 
cs             0x23	35                          result of the previous operation 
ss             0x2b	43                          (SUB) returned a 0xffffcfd0 which 
ds             0x2b	43                          is a pair number
es             0x2b	43                          PF is usually used for conditional jumps
fs             0x0	0
gs             0x63	99

(gdb) step 1
Dump of assembler code for function main:
   0x0804844d <+0>:	push   ebp
   0x0804844e <+1>:	mov    ebp,esp
   0x08048450 <+3>:	and    esp,0xfffffff0
   0x08048453 <+6>:	sub    esp,0x20
   0x08048456 <+9>:	mov    DWORD PTR [esp+0x1c],0x96  <--
=> 0x0804845e <+17>:	cmp    DWORD PTR [ebp+0x8],0x1
   0x08048462 <+21>:	jg     0x8048470 <main+35>
   ....
(gdb) info registers
eax            0x2	2
ecx            0x6ab3210f	1790124303
edx            0xffffd024	-12252
ebx            0xf7fb0000	-134545408
esp            0xffffcfd0	0xffffcfd0  <+++ 
ebp            0xffffcff8	0xffffcff8
esi            0x0	0
edi            0x0	0
eip            0x804845e	0x804845e <main+17>
eflags         0x282	[ SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99

(gdb) info frame
Stack level 0, frame at 0xffffd000:
 eip = 0x8048462 in main; saved eip = 0xf7e1fa83
 Arglist at 0xffffcff8, args: 
 Locals at 0xffffcff8, Previous frame's sp is 0xffffd000
 Saved registers:
  ebp at 0xffffcff8, eip at 0xffffcffc
```

# Tips #
* If you like to have Intel syntax in GDB just run this.
```
echo "set disassembly-flavor intel" > ~/.gdbinit
```
* To convert integers to hex use python hex(11) and to go back int(hex(11),16)

# GDB cheatsheet #
http://www.cs.berkeley.edu/~mavam/teaching/cs161-sp11/gdb-refcard.pdf

# Reference #
https://en.wikibooks.org/wiki/X86_Assembly

