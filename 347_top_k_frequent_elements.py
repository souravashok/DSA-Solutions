"""
Problem: 347. Top K Frequent Elements
Difficulty: Medium
URL: https://leetcode.com/problems/top-k-frequent-elements/

Description:
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Time Complexity: O(N) - Linear time using bucket sort.
Space Complexity: O(N) - Frequency map and bucket array storage.
"""


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for _ in range (len(nums)+1)]
        for n in nums :
            count[n]=count.get(n,0)+1
        for n,c in count.items():
            freq[c].append(n)
        res=[]
        for i in range (len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
