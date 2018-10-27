### #chapter 1 - 5

**Divide and conquer**
- analyze run-time of recursion 
  - master theorem
    - Create “a” subproblems of x, each having size “n/b”, f(n) is the time to create the subproblems and combine their results
    - T(n) = aT(n/b) + f(n); 
    - three cases : look at f(n) and compare it with n<sup>logb<sup>a - e</sup></sup>; 
      - potential answer: n<sup>logb<sup>a</sup></sup>logn, n<sup>logb<sup>a</sup></sup>, f(n);
    - **case 1** (Work to split/recombine a problem comparable to subproblems):
      - if f(n) = n<sup>logb<sup>a</sup></sup> : **T(n) = n<sup>logb<sup>a</sup></sup>logn**
      - e.g. mergesort-> T(n) = 2T(n/2) + O(n)
        - n<sup>logb<sup>a</sup></sup> = n<sup>log2<sup>2</sup></sup> = n -> T(n) = nlogn
      - e.g. binary search->T(n) = T(n/2) + O(1)
        - n<sup>logb<sup>a</sup></sup> = n<sup>log2<sup>1</sup></sup> = 1; T(n) = 1 * logn
        
    - **case 2** (Work to split/recombine a problem dwarfed by subproblems):
      - if f(n) = O(n<sup>logb<sup>a - e</sup></sup>): **T(n) = n<sup>logb<sup>a</sup></sup>**
             
    - **case 3** (Work to split/recombine a problem dominates subproblems):
      - if f(n) = omega(n<sup>logb<sup>a + e</sup></sup>): **T(n) = f(n)**
      - e.g. partition search(see below)
      - e.g. binary tree traversal 
    
  - common recursions and their run time
    - T(n) = 2T(n/2) + O(n): O(nlogn); //e.g. merge sort
    - T(n) = 2T(n/2) + O(1): O(n);
    - T(n) = T(n/2) + O(n): O(n)--> partition serch;
    
    
    
    
    
    
    
- merge sort
  - T(n) = 2T(n/2) + cn (two sub-problems, each of 1/2 of original size)
  - running time for each merge is O(n) - at most n comparisions
  - merge happens log(n) times (level of the tree)
- maximum-subarray problem
  - brute-force sulution: iterate each element and calculate all possible pairs, O(n^2)
  - DP(see leetcode #53)
    - DP[i] denotes the maxSum of the array A[0...i]
    - DP[i] is either DP[i - 1] + A[i] or 0 + A[i]
    - total maxSum is the max of the maxSums along the way.

      ```cpp
        int maxSubArray(vector<int>& nums) {
          int curSum = 0, ans = nums[0];             /* the maxSum from A[0...i) */
          for (int i = 0; i < nums.size(); i++){
              curSum = max(curSum, 0) + nums[i];
              ans = max(ans, curSum);
          }
          return ans;
        }
      ```
    - since we only need the max of the maxSums, there is no need to keep DP[]. 
  - divide and conquer(CLRS)
    - seems pretty intuitive and straightforward, but subtle to implement.
    - the solution in CLRS run in nlog(n) time
      - T(n) = 2(T(n/2)) + O(n)
    - the one in leetcode runs only in O(n) time (a different approach in calculating crossing subarray)
      - T(n) = 2(T(n/2)) + O(1)
       ```cpp
         void maxSubArray(vector<int>& nums, int l, int r, int& mx, int& lmx, int& rmx, int& sum) {
                if (l == r) {
                    mx = lmx = rmx = sum = nums[l];
                }
                else {
                    int m = (l + r) / 2;
                    int mx1, lmx1, rmx1, sum1;
                    int mx2, lmx2, rmx2, sum2;
                    maxSubArray(nums, l, m, mx1, lmx1, rmx1, sum1);
                    maxSubArray(nums, m + 1, r, mx2, lmx2, rmx2, sum2);
                    mx = max(max(mx1, mx2), rmx1 + lmx2);
                    lmx = max(lmx1, sum1 + lmx2);
                    rmx = max(rmx2, sum2 + rmx1);
                    sum = sum1 + sum2;
                }
           }
          int maxSubArray(vector<int>& nums) {
              if (nums.size() == 0) {
                  return 0;
              }
              int mx, lmx, rmx, sum;
              maxSubArray(nums, 0, nums.size() - 1, mx, lmx, rmx, sum);
              return mx;
          }
       ```
### #chapter 6 - 9
**Comparison Sort** 
  - Insertion sort, O(n^2)
    - an efficient algorithm for sorting a small number of elements
    - sort in place
  - Merge sort, O(nlogn)
    - faster, but the merge place does not operate in place.
  - Heap sort(see heap section)
  - Quick sort
    - O(nlogn) expected running time, O(n^2) worse case.
      - depend on whether the partition is balanced. we can then use randomized technique to make sure partition is balanced, i.e., get a random number as index, and exchange that number with the pivot number.
    - has tight code like insertion sort, so the hidden constant factor in its running time is small (access to array more closely packed?
    - sort in place
    - has tight code like insertion sort, so the hidden constant factor in its running time is small (access to array more closely packed?
    
**Heap & Priority queue**

- Heap structure
  - maxheap - parent greater than children.
  - height of a "node" ->longest simple path from that node to a leaf.
  - operations
    - max-heapify(O(logn))
      - when called on i, assumes the binary trees rooted at left(i) and right(i) are max-heaps.
      - i.e. can only swap down.
    - build-max-heap(O(n))
      - only need to call max-heapify from A.length()/2 down to 1. 
    
- heapsort
  ```cpp
  build max heap
  for (i = A.length down to 2)
          excahnge A[0] with A[n - 1]
          heapsize = heapsize - 1       //basically ignore the last element
          max-heapify(A, 0);            //need this because we've placed a random number on the top
  ```     
  - sort in place
  
- Priority queue
  - use min-heaps.
  - operations
    - heap-maximum(A)(O(1))
    - max-heap-insert(O(logn))
    - heap-extract-max(O(logn))
      - similar to heapsort operation
    - heap-increase-key(O(logn))

**sorting in linear time(non-comparison sort)**
- the nlogn lower lower bound only applies to comparison sort. If we can gather information about the sorted order of the input by means other than comparing elements, we can beat the lower bound.
- Counting sort
  - assumes that imput are in the set {0, 1, ..., k}
    - iterate the array and count how many elements less than or equal to {0, ..., k} and place the elements accordingly.
  - sort n numbers in O(k + n) time
    - stable sort.
    - when k = O(n), counting sort runs in linear time
- Radix sort
- Bucket sort
  - assume that the input is drawn from a uniform distribution

**The ith order statistic**
- simultaneous minimum and maximum
  - maintaining both min and max seen thus far and process elements in pairs, 3(n/2) comparisons in total.
- slecting the ith smallest number 
  - random unsorted array: O(n) linear time 
    - modeled after quicksort
    - each time partition the array and recursively call the procedure
  - for array mentained in data structure
    - heap/BST - keep aksing for successor
    - augmented rb-tree: keep size info and search(logn)
 
  
### #chapter 10 - 14
- Hash Tables
  - Performance: insert, search and delete
    - worst case O(n), O(1) expected case.
  - direct addressing
    - feasible when we can afford to allocate an array that has one position for every possible key
    - when the number of possible keys is huge, storing a table T of that size may be impractical and wasteful. In this case, a hash table requires much less storage than a direct address table - we hashes an element with K to slot h(k), in which h(k) is the hash value of k.
  - How to deal with collision (when more than one key maps to the same array index)
    - because |U| > m, there must be at least two keys that have the same hash value, thus avoiding collisions altogether is impossible, but **a well-designed, random looking hash function can minimize the number of collisions**.
    - hashing with chaining
      - place all the elements that hash to the same slot into the same linked list.
    - open addrssing(all elements occupy the hash table itself)
      - we successively examine (probe) the hash table until we find an empty slot in which to put the key. The sequence to probe depends upon the key being inserted.
      - linear probing
      - quatratic probing
      - double hashing
- Binary Seartch Tree (BST)
  - Tree walk - O(n)
    - recursive traversal takes O(n) time since after initial call, the procedure call itself recursively exactly twice for each node in the tree - once for its left child and once for its right child.
  - Querying, Tree_Min, Tree_Max(O(h))
  - Successor of node x (the smallest key greater than x.key) - (O(h))
    
    (1) x has right tree.
    ```cpp
    if x.right != NIL
        return Tree_Min(x.right)
    ```
    
    (2) x does not has right tree. 
    ```cpp
    go up the tree from x until we find a node that is the left child of its parent. 
      return the parent.
    ```
    
    In this case, the successor Y is the lowest ancestor of x whose left child is also an ancestor of x.
  - deletion, insertion(O(h))
- rb-tree
  - How it ensures the balance?
    - by constraining the node colors on any simple path from the root to leaf, it ensures that no such path is more than twice as long as any other.
    
- trie
  - intuition
    - if we store each key in binary tree ->need MlogN to search for a particular key
      - M length of each key
      - N = numbers of key
    - with trie, however, we can do the search in O(M) times
  - features
    - position in the tree defines the key with which it is associated
    - all descendants have a common prefix
    - root is associated with empty string
  - structure
    - array of pointers to its children(max=26)
    - bool indicating the end of the word


### #chapter 15 (Dynamic Programing)
- key features
  - differ from ordinary divide conquer in that it's not just combining solutions to subproblems. __*it applies when SUBPROBLEMS OVERLAPS - that is, when subproblems does more work than necessary, repeatedly solving the common subproblems.*__ A DP algorithm thus avoiding recomputing by saving itr answer in a table.

- top-down with memoization
  - write the procedure recursively in a natural manner, but modified to save the result of each subproblem(array).
  - **essentially a "depth-first search" of the subproblem graph.**
- bottom-up method
  - we sort the subproblems by size and solve them in size order, so solving any particular subproblem depends only on solving smaller subproblem.
  - **essentially a reverse topological sort of the subproblems.**

- longest common subsequence
  - a classic DP problem similar to those on leetcode
- code optimization
  - do we really need to keep full table of info? perhaps we only need to maintain the immediately preceding values.


### #chapter 16 (Greedy Algorithms)
- intro
  - make a locally optimal choice in the hope that it will lead to a globally optimal solution
  - classic application: Minimum-spanning-tree, Dijkstra's algorithm for shortest paths from a single source
- dp v. greedy
  - dp is good, but sometimes it might be an overkill
  - greedy works better when it is possible to reach optimal solution without having to first solve all subproblem.
  - can usually transform recursive structure to iterative one.

### #chapter 21 (Graph Algorithms)
- BFS
  - how it works
    - computes the distance from s to each reachable vertices and produces a BF-tree.
    - discovers all vertices at distance k from s before discovering any vertices at distances k+1.
    - works for both directed and undirected graph
  - performace
    - O(V + E): total time devoted to queue is O(V) and the time devoted to scanning the list is O(E). 
  - Application: (1) Prim's minimum-spanning tree, (2) Dijkstra's single-source shortest-paths
  
- DFS
  - how it works
    - search deeper whenever possible
    - explores edges out of the most recently discovered vertex that still has unexplored edges leaving it. Once all of v's edges have been explored, the search backtracks to explore edges leaving the vertex from which v was discovered
    - performance also O(V + E). 
  - application
    - topological sort
    - strongly connected components
   
- Topological sort of DAG
  - a linear ordering of all its vertices such that if G contains an edge(u, v), then u appears before v in the ordering.
  - only applies to DAG becuase no ordering is possible if the graph has cycle.
    ```cpp
    call DFS to compute finishing times v.f for each vertex v
    as each vertex is finished, insert it onto the front of a linked list
    return the linked list.
    ```
  - remember to detect if there is cycle
    - color the nodes in three state: -1, 0, 1: there is a cycle when you visit a node when it is 0 (in progress)
   
- Miminum Spanning Tree(MST)
  - definition
    - find a subset of T among E that connects all vertices and the W(T) is minimized.
    - applis to CONNECTED, UNDIRECTED graph.
  - Algorithms
    - both algorithms use greedy approach. They differs in specific method used to find safe edge.
    - general approach
      - grow one edge at a time.
      - prior to each iteration, A is a subset of some MST.
      - at each step, we determine an edge that we can add to A "a safe edge" such that A and {u, v} is also a subset of minimum spanning tree. 
      - key is how we can find the safe edge: let A be a subset of E that is included in some minimum spanning tree for G, let (S, V - S) be any cut of G that respects A, and let (u, v) be a light edge (i.e. its weight is the minimum of any edge crossing the cut) crossing (S, V - S), then (u, v) is a safe for A.
  - Kruskal's algorithm
    - O(ElgV) using ordinary binary heap.
    - make each vertex a unique set (individual trees)
    - sort the edges by its weight (ElogE)
    - find the safe dge by finding, of all edges that connect any two trees in the forest, an edge (u, v) of least weight.
    - union the trees connected by the newly established edge after each step.
  - Prim's algorithm (BFS)
    - O(ElgV) using ordinary binary heap, O(E + VlogV) using Fibonacci heap, which improves over binary heap if V is much smaller than E.
    - resembles Dijkstra's shortest-paths algorithm.
    - edges in set A always form a single tree (unlike individual tress in K's algorithm)
    - at each step, vertices not in the tree reside in a min-priority queue based on the key. Key is the minimum weight of any edge connecting v to a vertex in the tree.
    - running time depends on how we implement the priority queue.

- Single-source shortest Paths
  - intro
    - basic idea is we relax edges at each step. keep track of the shortest-path estimate from source s to v.
    - algorithms differ in how many times it relaxes each edges and in what order.
  - unweighted graph - BFS
  - Weighted, directed acyclic graph (DAG)
    - topologically sort the vertices and relax each accordingly.
  - Weighted, directed cyclic graph 
    - Floyd-Warshall (DP)
      - can detect whether a negative-weight cycle is reachable from the source
    - Dijkstra's (greedy)
      - assumes that no negative weights input.
      - maitain a set S of vertices whose final shortest-path weights from the source s have already been determined. The algorithm repeatedly selects the vertex u among V - S with the minimum shortest-path estimate, adds u to S, and relax all edges leaving u.
