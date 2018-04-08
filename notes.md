### #chapter 1 - 4
* Insertion sort
  - an efficient algorithm for sorting a small number of elements
  - sort in place
  
* Divide and conquer
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
### #chapter 6
    
