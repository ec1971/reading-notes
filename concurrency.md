# concurrency 
## three basic approach for synchronization
  - concurrency with processes
  - concurrency with I/O multiplexing (asynchronous I/O and event-driven programming)
  - concurrency with data parallel programming(e.g. MapReduce)
  - concurrency with thread

## data parallel programming(e.g. MapReduce)
### preliminary
- idea is to apply commputation in parallel across an entire data set at the same time, with each thread operating on independent data elements. 
- The work on every data item must complete before moving onto the next step
- for this scheme to work, we need an efficient way to check whether all n threads have finished their work - synchronization barrier. 
  - one operation: checkin
  - a thread calls checkin when it has completed its work;
  - no thread may return from checkin until all n threas have checked in.

## concurrency with thread
### basic features
- Definition: a single execution sequence that represents a separately schedulable task.
- passes control via context switch - os include a thread scheduler that can switch b/w threads that are running and those that are ready but not running. there are many possible interleavings of a program with multiple threads. should not make assumptions about relative speed or sequence.
- posix threads(Pthreads) is the standard interface
  
### why use thread?
- (1) expressing natural concurrency by writing each logically concurrent tasks as a separate thread (update screen, fetch data, receive new inputs, etc)
- (2) improve user responsiveness: creates threads to perform work in the background, that way user interface can remain responsive to further commands, regardless of the complexity of the user request.
- (3) exploiting multiple processors
- (4) managing i/o devices: when one task is waiting for I/O, the processor can make progress on a different task. 
  - **processors are often much faster than I/O systems** with which they interact, so keeping the processor idle during I/O would waste much of its capacity - the latency to read from disk can be tens of milliseconds, enough to execute more than 10 million instructions on a modern processor.
  
### concept clarifications
- thread v. process
  - related to each other but fundamentally different; a process can be thought of as an instance of a program in execution. it is an independent entity to which system resources are allocated. each process is executed in a separate address space, and one cannot access the variables and data structures of another process. if we'd like to share resources, inter-process communications have to be used - e.g., pipes, files, sockets, etc.
  - a thread exists within a process and share the process's resources. it is a particular execution path of a process. when one thread modifies a process resource, the change is immediately visible to sibling threads.
  
- thread v. interrupt handler
  - share some resemblance as both are single sequence of instructions that executes from beginning to end, but interrupt handler is not independently schedulable - it is triggered by a hardware I/O event.
  
- kernel thread v. process thread
  - we are usually talking about multiple threads per process where each thread can make system calls into the kernel, but kernel itself can also benefit from using multiple threads, each runs with the privileges of the kernel.

### what do threads whare and do not share?
- they all share the entire virtual address space of that process (code, data, heap, shared libraries, open files)
- DO NOT SHARE (TCB - thread control block: each thread has its own separate thread context)
  - thread ID and other thread associated metadata
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
    
  - reader-writer problem (frequent read  + infrequent write)
    - readers may share object with unlimited number of other readers but writers might want to have exclusive access to the object (inspect tickets assignments v. booking tickets)
    - very common in databases where we need to support faster search queries over the database while also supporting less frequent database update.
    - see the server example for reference
### deadlock
- preliminary 
  - occur anytime a thread waits for an event that cannot happen because of a cycle of waiting for a resource held by the first thread (resource shoud be broadly construed)
  - may be caused by improper mutext ordering
  - deadlock is a form of starvation (when a thread fails to make progress for an indefinite period of time);
- dining philosopher 
  - why deadlock occur (if all philosophers pick up the left one at the same time)
    - bounded resources: not enough chopsticks for all philosopher
    - no preemption: once a philosopher picks up a chopstick, she does not release it until she is done eating, even if that means no one will ever eat
    - wait while holding: when a philosopher needs to wait for a chopstick, she continues to hold onto any chopsticks she has already picked up
    - circular waiting: there is a set of waiting threads such that each thread is waiting for a resource held by another (here, every philosopher is waiting for chopstick holding by another)
   
  
  - how to prevent
    - examine why deadlock occur and prevent one of its necessary condition
      - bounded resources: provide sufficient resources
      - no preemption:preempt resources - forcibly reclaim resources held by a thread
      - curcular waiting: in nested waiting, restructure the modlue's code so that no locks are held when calling other modules.
        - identify an ordering among locks and only acquire locks in that order
      - wait-while-holding: wait until all needed resources are available and then to acquire them atomically at the beginning of an operation, rather than incrementally as the operation proceeds.
      
    - allow "undo" actions that take a system into a deadlock.
  - detecting deadlock
    - the detection mechanism can be conservative - it can trigger the repair if we might be in a deadlock state - risks a false positive where a non-deadlocked thread is incorrectly classofied as deadlocked. whether to enforce this conservative rule depends on the overhead of the repair operation.
    - specifically: examine the graph of threads and associated resoucres: 
      - if there are several resources and only one thread can hold each resource at a time, we can consider each thread and resource as node. There is a directed edge from a resource to a thread if the resource is owned by the thread and from a thread to a resource if the thread is waiting for resource ->there is a deadlock if and only if there is a cycle in such a graph.
      - if there are multiple instances of some resources - a cylce is necessary but not sufficient
    - or, a mechanism that's similar to banker's algorithms.
  
  - recovering from deadlock
    - proceed without the resources
    - transactions: rollback and retry
      - choose one or more victim threads, stop them, and undo their actions, and let other threads proceed
      - once the deadlock is broken and other thrads have completed some or all of their work, the victim thread is restarted
    
    
    
    
    
    
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

## LOCK DESIGN & IMPLEMENTATION  
### DESIGN PATTERN
- **high level methodology**
  - consideration
    - safe
    - efficiency
    - prevent startving (e.g. FIFO scheme)
    - deadlock
    
  - decompose the problem into objects
    - in particular, what's the shared shared object?
  - for each object
    - define clean interface
    - identify internal state and invariants to support that interface
    - implement methods to manipulate state
    
- **DESIGN PROCESS**
  - add lock
    - start with the most simple design - each shared object includes exactly one lock
  - [WHEN TO ACQUIRE/RELEASE LOCK?]
    - common design is to acquire the lock at the start of each public method and release it at the end of each public method
      - two advantages: (1) easy to reason about state of lock(2) ensure that the lock is already called when each private method is called
      - other design may speed up the program (e.g. avoid acquiring lock in some or acquiring only in parts of some methods), but it's error prone - until you are absolutely sure you are right, don't do it 
      
  - [HOW MANY CONDITION VARIABLES YOU NEED?]
    - consider each method and ask, "when can this method wait?" 
    - a common approach is to add a condition variable for each situation in which the method must wait
    - there is no single right answer. you can usually do it multiple ways
    
  - add loops to wait using the condition variables
    - might wake up even w/o signal, or condition no longer true when the waiting thread resumes execution; this is to ensure that a thread always check condition before preceeding
    ```CPP
    while(!workAvailable()){
      cond.wait(&lock);
    }
    assert(workAvailable());
    ```
  - add signal and broadcast calls
  
### CASE STUDIES
- RWLock
  - mutual exclusion = readers v. writers & writers v. writers
  - need to decided whether reader-preferred or writer-preferre

- synchronization barrier for MapReduce(checkin)
  - simple design
    - one lock for checkin();
    - one condition variable - all checkin
    - key is to include both wait & broadcast in a single function
    - problem is that it can't revert back to its initual state, thus can't be re-used.
  - **re-useable design**
    - one lock + two condition variable - all checkin & all leaving
    - the nth thread to leave reset the allcheckedin variable; the nth thread to checkin reset the allLeft varible.

- bounded queue
  - how do we prevent starving by implementing FIFO scheme?
    - create one condition variable for each waiting thread
    
### MULTIPLE LOCKS
- Consideration
  - performance/efficiency
    - avoid bottleneck
  - startving
  - deadlock
- strategy for using multiple locks to decrease lock contention 
  - fine-grained locking:
    - partition an object's state into different subsets and each protected by a different lock
    - e.g. one lock per bucket; partition heap to separate memory region
      
  - pre-processor data structure
    - partition based on number of processor
  - ownership design patter
  - staged architecture
- RCU (read-copy-update) locks
  - for read heavy database - frequently read but ocassionally update
  - cf. RWlock
    - because of the serial access of the readers/writers control structure, the synchronization process can be a bottleneck (esp when the critical section is short - synchronization overhead is huge)
    - RCU solves this by reducing overhead for read at the cost of overhead for write
    
# SCHEDULING
- overview
  - key is to form an analytic framework to think about scheduling problems
  - applies to any scare resoucres
  - most scheduling scheme combines aspects of different schudling policies.
- Consideration  
  - throughput
  - response time
  - scheduling overhead
  - fairness
  - starvation
  - predictability
  - cache reuse
    - scheduled on this processor and have content cached on it but scheduled on another next time?
- scheduling policy
  - FIFO
    - strengths
      - minimizes overhead - switching between tasks only when each one completes
      - great throughput since overhead is minimized
      - fair
    - weakness
      - but response time might be huge if short tasks happen to arive after a long one (no such issue if all requests are for small amounts of data)
        - cf. SJF
    - application
      - memcached of webservices
  - shortest-job-first (SJF)
    - strengths
      - minimized average response time
    - weakness
      - not practical->usually do not have info about how much time each task needs
      - variance of response time can be huge
        - trade off of average response time v. variance of response time
        - starving and frequent context switch
    - application
      - web service for static content - where you are able to predict bandwidth
    
  - round robin
    - idea is to assigned to each process in equal portions and in circular order, handling all processes without priority
    - strengths
      - best to achieve predictable, stable rate of progress
    - weak
      - tricky to decide time slice ->minimize overhead
    - application
      - web service for static content - where you are able to predict bandwidth
 
 
  - Multi-level feedback
    - extention of round robin: tasks of high priority preempt that of low ones, but tasks of same priority are scheduled based on round robin

- what if there are multiple processors
  - maximize cache efficiency
    - **affinity scheduling**: once a thread is scheduled on a processor, it is returned to the same one when it is re-scheduled, maximizing cache reuse









