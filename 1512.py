#Number of good pairs
"""Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100"""

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
    # the 0-indexing, start counting the array from [0,1,2,3,4,5] for the indexes 
        #x = nums[i]
        #y = nums[i+1]
        counter = 0 
        for i in range(1,len(nums)-1):
            if nums[i] == nums[i-1]:
                #print(nums[i],nums[i+1])
                counter += 1 
                print(counter)
            