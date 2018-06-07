**bits/bytes/ascii**
- most computer systems represent text characters using ASCII standard that represents each charater with a unique byte-size interger value (a byte = 8 bit, ranging from 0 to 255)
  
**compilation system**
- preprocessor
- compiler
- assembler
- linker

**caches**
- the processor can read data from register file 100 times faster than from memory
- cache memories are storage devices that serve as temporary staging areas for information that the processor is likely to need in the near future
- can get the effect of both a very large memory and a very fast one by exploiting locality - the tendancy for programs to access data and code in localized regions

**operating systems**
- can think of it as a layer of software interposed between the application program and the hardware
- three central ideas
  - processes
    - a process is the op's abstraction for a running program
    - provide the illusion that (1) the program is the only one running on the system; (2) the program appear to have exclusive use of both the processor, main memory, and the I/O devices; (3) the processor appears to execute the instruction in the program one after the other without interruption. (4) code and data of the program appear to be the only objects in the system's memory.
    - run concurrently means instructions of one process are interleaved with instructions of another. the OP performs this by context switching.
    - thread
      - see thread chapter
      
  - virtual memory
    - the abstraction that provide the illusion that each process has exclusive use of the main memory
  - files
    - a sequence of bytes. a lot of things are modeled as file.
    - provide applications with a uniform view of all the varied I/O devices that might be contained in the system.
    
**network**
 - can be seen as just another I/O device to copy information from one machine to another via network.
 
