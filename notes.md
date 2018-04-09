### #chapter 1 - 5

**Divide and conquer**
- analyze run-time of recursion 
  - make sure you at least have some idea of what the master theorem is
  - common recursions and their run time
    - T(n) = 2T(n/2) + O(n): O(nlogn); //e.g. merge sort
    - T(n) = 2T(n/2) + O(1): O(n);
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
- slecting the ith smallest number in linear time
  - modeled after quicksort
  - each time partition the array and recursively call the procedure
  
### #chapter 10 - 14
