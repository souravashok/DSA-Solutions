"""
Problem: 283. Move Zeroes
Difficulty: Easy
URL: https://leetcode.com/problems/move-zeroes/

Description:
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Time Complexity: O(N) - Single pass through the array.
Space Complexity: O(1) - Done in-place with two pointers.
"""


class Solution(object):
    def moveZeroes(self, nums):
        l=0
        for r in range(len(nums)):
            if nums[r]!=0:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1

        
