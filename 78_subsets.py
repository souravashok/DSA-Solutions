"""
Problem: 78. Subsets
Difficulty: Medium
URL: https://leetcode.com/problems/subsets/

Description:
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique.

Time Complexity: $O(N \times 2^N)$ - There are $2^N$ possible subsets, and creating a deep copy of 'path' takes $O(N)$ time.
Space Complexity: $O(N)$ - The recursion stack and the 'path' array use at most $O(N)$ space (excluding the output array).
"""
class Solution(object):
    def subsets(self, nums):
        res=[]
        def backtrack(i,path):
            if i==len(nums):
                res.append(list(path))
                return
            path.append(nums[i])
            backtrack(i+1,path)
            path.pop()
            backtrack(i+1,path)
        backtrack(0,[])
        return res
