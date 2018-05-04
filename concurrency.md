# three basic approach for synchronization
  ## with processes
  ## with I/O multiplexing
  
  ## with thread
- basic features
  - passes control via context switch
  - posix threads(Pthreads) is the standard interface
- all threads share
  - entire virtual address space of that process (code, data, heap, shared libraries, open files)
  - each thread has its own separate thread context
  - thread ID
  - stack, stack pointer, program counter
  - general-purpose register values (never shared)
- synchronizing 
  - why synchronizing error? because there is no way for you to predict whether the operating system will choose a correct ordering of your threads
  - critical section
    - critical section should not be interleaved with the critical section of other thread
    - **mutual exclusion**: want to make sure that each thread has mutually exclusive access to the shared variable while it is executing the instructions in its critical section
  - sychronizing using semaphores
    - semaphore, a global variable with a nonnegative interger value that can only be manipulated by two special operations: P and V
    - how it works
    - P(s): if s is nonzero P decrements s and return immediately; if s is zero, then suspend the thread until s becomes nonzero (s only becomes nonzero when the thread that's running called V); then thread is restarted by that V operation.
    - V(s): increments s by 1 - it restarts exactly one of the threads that's been waiting
    - **Mutex**: when used to protect shared variables it's called **binary** semaphore because its value is always 0 or 
