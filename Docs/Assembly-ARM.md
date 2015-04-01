Assembly

ARM is RISC (Reduced Instruction Set Computing) standard.
  - has less instructions that CISC (complex) => easy to analize, but slower than RISC

== ARM Registers ==
- temporary placeholders for variables used by
    - the program
    - varius CPU specific data
- ARM has 37 32-bit registers

r0-r12 - General Purpose Registers (GPR)
  - can contain anything

r13 - Stack Pointer (SP)
  - the number in this register points to the top of the memory stack
  - when an instruction is run, the stack holds the last memory address
  - stack overflow => stack accumulates too many memory addresses
                   => the original address get overwritten
                   => program enters in infinite loop

r14 - Link Register (LR)
  - works like the SP, but it's used when a subroutine can't call another one.
    in this case the address is saved in LR and not added to the stack, because faster.
    ARM has a register for this.
    Any GPR can be used for the very same purpuse.

r15 - Program Counter
  - holds the current memory location
  - it's a binary counter. counts up from 0 to 2^30. 2 bits are always 0.

Current Program Status Register (CPSR)
  - register that houses various informations: http://en.wikipedia.org/wiki/ARM_architecture#Registers

Other registers.
ARM has several operation modes. Only some registers can be accesed in each mode. r0-r15 + CPSR are always available.


== ARM Instructions ==
For reference you can find all the ARM instructions here: http://infocenter.arm.com/help/topic/com.arm.doc.qrc0001l/QRC0001_UAL.pdf
