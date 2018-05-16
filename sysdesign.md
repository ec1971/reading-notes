## Random notes
- example language that we may find useful later

>For example, the URL-shortening service could be meant to serve just a few thousand users, but each could be sharing millions of URLs. It could be meant to handle millions of clicks on the shortened URLs, or dozens. The service may have to provide extensive statistics about each shortened URL (which will increase your data size), or statistics may not be a requirement at all.

>Perhaps your system needs a load balancer and many machines behind it to handle the user requests. Or maybe the data is so huge that you need to distribute your database on multiple machines. What are some of the downsides that occur from doing that? Is the database too slow and does it need some in-memory caching?
## youtube video

- problems introduced
  - consistency 
  - 
- three topics
  - storage
    - database issues; CAP
  - computation
    - MapReduce
  - messaging
  
- use consistent hashing to assign database + replication

## CS75 notes

- how do you go about scaling?
  - verticle scaling
    - upgrade hardware; simply get more processor, memory, multicore, etc
      - Upgrad disk: SATA, SAS drive...
    - problem: there is a ceiling; exhaust resources or reach state of art
    
  - horizontal scaling
    - use multiple servers instead of keep upgrading one server
    - **LOAD BALANCER**: use load balancer to distribute requests to back end server
      - Mechanism to distribute work
        - based on actual load
        - dedicated server for type of file
        - load balancing with BIND (DNS configuration)
          - load balancer (act as DNS) send out IP address of different servers each time based on round robin
          - problem is that you may have power user clustered in one server
          
    - **Sticky session: using load balance breaks sessions/coockies**
      - sessions typically implemented per server
      - not a problem if you configure LB such that all PHP traffic goes to one server, static goes to another..
        - problem is that hard to balance load this way
      - solution: use cookie to store the ID of server
        - but IP may change
        - also privacy 
      - solution: can factor out session states
        - have a file server - a big external harddrive that is connected to all servers. any time they store session data, they store it there, instead of their own harddrive.

    - **once we have file server, we've introduced another weakness ->what if that server break**
      - before we have very good redundancy in our server model->n server doing similar things
      - but now we've introduced file server (also if we introduce database)
      - how to fix it?
        - could use **RAID** (a data storage technique): assume you have multiple hard dirve 
          - RAID 0: striping->distributing the content among all disks; no data reduncy but nice for performance (can write faster this way)
          - RAID 1: mirror data acrouss harddrive -> a bit performance overhead.
          - RAID 5: striping + distributed parity
            - need at least 3 drives, one can die
          - RAID 6: striping + double distributed parity
            - any two drives can die
          - RAID 10: 4 drives. both striping and mirroring.
        - Replication (see below)
          - making automatic copy of something (MASTER-SLAVE)
       
     - Caching
      - file based caching approach(craiglist)
        - redundancy
       - MYSQL query cache
       - memcached
        - memory cache that store info in ram.
        
      - Replication
          - advantages
            - achiev redundancy by making automatic copy of something (MASTER-SLAVE)
            - good for website that's read heavy
            - even better if you have master-master server ->everytime you write to server 1 it automattically replicated to server 2.
          - apply to webserver and database (e.g. mysql) too
          - can also have a pair of LB (active:active)
      - partitioning
        - e.g. different server for different user group, by surname/school
        - communication problem
      - high availability(HA)
        - applies to LB and database







## scalability for dummies
- load balancer
  - public servers of a scalable web service are hidden behind a load balancer
  - this lb evenly distribute load (request from users) onto your group/cluster of application servers.
  - first golden rule of scalability: every server contains exactly the same codebase and does not store any user-related data, like sessions or profile pictures, on local disc or memory.
  - sessions need to be stored in a centralized data store which is accessible to all application servers.
  - key issue is deployment - to make sure that a code change is sent to all your servers w/o one server still serving old code
- database
  - Using NoSQL instead of scaling a relational database
- cache (in-memory caches like Memcached or Redis)
  - cached databased queries
  - cached objects
  
- asynchronism

- sharding
  - A database shard is a horizontal partition of data in a database or search engine. Each individual partition is referred to as a shard or database shard. Each shard is held on a separate database server instance, to spread load.
  - Database normalization, or simply normalization, is the process of restructuring a relational database in accordance with a series of so-called normal forms in order to reduce data redundancy and improve data integrity.
