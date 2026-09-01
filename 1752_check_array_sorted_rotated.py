"""
Problem: 1752. Check if Array Is Sorted and Rotated
Difficulty: Easy
URL: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

Description:
Given an array nums, return true if the array was originally sorted in non-decreasing order, 
then rotated some number of positions (including zero). Otherwise, return false.

Time Complexity: O(N) - Single pass through the array.
Space Complexity: O(1) - In-place comparison using modulo traversal.
"""

class Solution(object):
    def check(self, nums):
        c = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                c += 1
        return c <= 1
