"""
Problem: 69. Sqrt(x)
Difficulty: Easy
URL: https://leetcode.com/problems/sqrtx/

Description:
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator (e.g., pow(x, 0.5) or x ** 0.5).

Time Complexity: O(log x) - Binary search over the range [0, x].
Space Complexity: O(1) - Constant auxiliary space.
"""

class Solution(object):
    def mySqrt(self,x):
        l,r=0,x
        while l<=r:
            m=(l+r)//2
            if m*m<=x<(m+1)*(m+1):return m
            elif m*m>x:r=m-1
            else:l=m+1
