- example language that we may find useful later

>For example, the URL-shortening service could be meant to serve just a few thousand users, but each could be sharing millions of URLs. It could be meant to handle millions of clicks on the shortened URLs, or dozens. The service may have to provide extensive statistics about each shortened URL (which will increase your data size), or statistics may not be a requirement at all.

>Perhaps your system needs a load balancer and many machines behind it to handle the user requests. Or maybe the data is so huge that you need to distribute your database on multiple machines. What are some of the downsides that occur from doing that? Is the database too slow and does it need some in-memory caching?
