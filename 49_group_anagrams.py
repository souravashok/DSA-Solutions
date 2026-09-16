"""
Problem: 49. Group Anagrams
Difficulty: Medium
URL: https://leetcode.com/problems/group-anagrams/

Description:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Time Complexity: O(N * K) - Where N is the number of strings and K is the maximum length of a string.
Space Complexity: O(N * K) - Storing strings in the hash map.
"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for  s in strs:
            count = [0] * 26
            for c in s :   
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())
