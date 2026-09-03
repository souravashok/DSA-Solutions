"""
Problem: 238. Product of Array Except Self
Difficulty: Medium
URL: https://leetcode.com/problems/product-of-array-except-self/

Description:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Time Complexity: $O(N)$ - Two linear passes over the array.
Space Complexity: $O(1)$ - The output array does not count as extra space for complexity analysis.
"""


class Solution(object):
    def productExceptSelf(self, nums):
        n=len(nums)
        res=[1]*n
        left = 1
        for i in range(n):
            res[i]=left
            left*=nums[i]
        right = 1
        for i in range(n-1,-1,-1):
            res[i]*=right
            right*=nums[i]
        return res
