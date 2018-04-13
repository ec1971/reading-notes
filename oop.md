- access specifier 
  - access specifier in base class
    - public member
    - private member
      - a derived class may not access private members, like any other ordinary users
    - protected member 
      - derived class can access, but other users can't.
      - plus, a derived class member or friend may access the protected members of the base class ONLY through a derived object.
     
  - access specifier after class derivation list (optional, to control ACCESS users of the derived class have)
    - determine whether users of a derived class are allowed to know that the derived class inherits from its base class
    - public
      - public members of the base class become part of the interface of the derived class as well. 
      - we can bind an object of a publicly derived type to a pointer or reference to the base type (dynamic binding)
      
      
- components of derived class
  - base-class part: members it inherits from its base class
    - must use base-class constructor to initialize its base-class part.
  - members defined by themselves
      
         
      
      
      
- dynamic binding
  - when call virtual function through pointer or reference, the call will be dynamically bound. Resolved at runtime
    - parameter types must be exactly the same
    - return type must be the same
      - unless returns pointers/references itself related to inheritence
        - but, such return types requires that the derived-to-base conversion from D to B is accessible (p613)
  - any nonstatic member function, other than a constructor, may be virtual
  
  
- virtual function dustructor
  - class used as the root of an inheritance hierarchy almost always define a virtual destructor
