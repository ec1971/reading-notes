## RANDOM USEFUL NOTES
- many core ideas in modern os have become widely applied throughout computer science.
- Software engineers use many of the same technologies and design patterns as those used in operating systems to build other complex systems. 
- in modern world, nearly everything a user does is distributed, nearly every computer is multi-core, security threads abound

## Themes
- [abstract/general]overall goal is to build system that is
  - reliable
  - secure
  - portable, flexible
  - efficient
  - resilient
- [more specific]design consideration
  - resource management/allocation/sharing
  - communication: data sharing/multi-tasking
  - isolation: securityfailure isolation
  
- key questions to consider
  - how to enable multiple applications to communicate with each other?
  - how does the operating system enable applications to do multiple things at once?
  - how to facilidate sharing? how to synchronize shared data access ? 
  
## core concept
- operating system
  - **ISOLATION**:
    - failure isolation: os isolate applications from each other so that a bug in one application does not corrupt other applications running on the same machine
    - this requires restricting the behavior of applications to less than the full power of the underlying hardware
    - flip side is communication
  
  - **ABSTRACTION**: 
    - provide abstration to simply application design; here, os provdes the **illusion** that each program has infinite memory and the computor's processors entirely to itself.
  
  - **RESOURCE MANAGEMENT**
    - few processors, finite amount of memory, network bandwidth, disk space
    - need to balance needs, separates conflicts, and facilitates sharing
    - one user should not be allowed to monopolize system resources or to access or corrupt another user's files without permission
