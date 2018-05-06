# three basic approach for synchronization
## with processes
## with I/O multiplexing

## concurrency with thread
### basic features
  - passes control via context switch
  - posix threads(Pthreads) is the standard interface
  
### why use thread?
- expressing natural concurrency by writing each logically concurrent tasks as a separate thread (update screen, fetch data, receive new inputs, etc)
- improve user responsiveness: creates threads to perform work in the background, that way user interface can remain responsive to further commands, regardless of the complexity of the user request.
- exploiting multiple processors
- managing i/o devices: when one task is waiting for I/O, the processor can make progress on a different task. 
- **processors are often much faster than I/O systems** with which they interact, so keeping the processor idle during I/O would waste much of its capacity - the latency to read from disk can be tens of milliseconds, enough to execute more than 10 million instructions on a modern processor.
  
### thread v. processes?
- 

### what do threads whare and do not share?
- they all share the entire virtual address space of that process (code, data, heap, shared libraries, open files)
- but each thread has its own separate thread context
  - thread ID
  - stack, stack pointer, program counter
  - general-purpose register values (never shared)
   
### synchronizing 
  -  what is synchronizing error and why does it occur? 
     - when there are multiple concurrent processes or threads, if one thread starts executing certain program segment called critical section when the other thread has not finished yet, the result may be wrong. If not properly synchronized, it may cause race condition where the values of variables may be unpredictable and vary depending on the timings of context switches of the processes or threads.
     - why it occurs: because there is no way for you to predict whether the operating system will choose a correct ordering of your threads
  - critical section
    - critical section should not be interleaved with the critical section of other thread
    - **mutual exclusion**: want to make sure that each thread has mutually exclusive access to the shared variable while it is executing the instructions in its critical section
      - can use lock or semaphore
      
### how to handle mutual exclusion?
  - semaphore, a global variable with a nonnegative interger value that can only be manipulated by two special operations: P and V
  - how it works
  - mutual exclusion (mutex)
    - P(s) - Locking the mutex: if s is nonzero P decrements s and return immediately; if s is zero, then suspend the thread until s becomes nonzero (s only becomes nonzero when the thread that's running called V); then thread is restarted by that V operation.
    - V(s) - unlocking the mutex: increments s by 1 - it restarts exactly one of the threads that's been waiting
    - **Mutex**: when used to protect shared variables it's called **binary** semaphore because its value is always 0 or
    
### what are the classic mechanism to schedule shared resources?

  - producer-consumer problem
    - only ensuring mutual access is not enough - also need to schedule usage (can't insert when buffer is full)
    - usually three semaphores - one mutex, one slots and one items
  - reader-writer problem
    - readers may share object with unlimited number of other readers but writers might want to have exclusive access to the object (inspect tickets assignments v. booking tickets)
    - see the server example for reference
### deadlock
  - when a collection of threads is blocked, waiting for a condition that will never be true
  - may be caused by improper mutext ordering
  
### parallelism
   - a parallel program is a concurrent program running on multiple processors
   - might even be slow as synchronization overhead is expensive and should be avoided
   - in the csapp example, run time linearly decrease until we reach 4 threads ( = number of cores of the machine), then it actually increas - that's because the overhead of context switching multiple threads on the same core - when it's less or equal than four, each thread is running on separate core.
 - thread safe: always produce correct results when called repeatedly from multiple concurrent threads
   - reasons why thread might not be safe:
      - do not protect shared variable?
      - keep state across multiple invocations (the rand example on book)
      - functions that return a pointer to a static variable?
   - reentrant functions (a subset of thread-safe functions): safe because they do not reference any shared data

### implementation 
- design process
  - high level methodology
    - decompose the problem into objects
    - for each object
      - define clean interface
      - identify internal state and invariants to support that interface
      - implement methods to manipulate state
  - specific steps
    - add lock
    - add code to acquire and release the lock
    - identify and add condition variables
    - add loops to wait using the condition variables
    - add signal and broadcast calls
