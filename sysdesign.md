- example language that we may find useful later

>For example, the URL-shortening service could be meant to serve just a few thousand users, but each could be sharing millions of URLs. It could be meant to handle millions of clicks on the shortened URLs, or dozens. The service may have to provide extensive statistics about each shortened URL (which will increase your data size), or statistics may not be a requirement at all.

>Perhaps your system needs a load balancer and many machines behind it to handle the user requests. Or maybe the data is so huge that you need to distribute your database on multiple machines. What are some of the downsides that occur from doing that? Is the database too slow and does it need some in-memory caching?


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
