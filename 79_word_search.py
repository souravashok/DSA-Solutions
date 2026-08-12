"""
Problem: 79. Word Search
Difficulty: Medium
URL: https://leetcode.com/problems/word-search/

Description:
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are 
horizontally or vertically neighboring. The same letter cell may not be used more than once.

Time Complexity: $O(M \times N \times 4^L)$ - Where M and N are the grid dimensions and L is the length of the word. In the worst case, we explore 4 directions for every character.
Space Complexity: $O(L)$ - The recursion stack will go as deep as the length of the word. Modifying the board in-place saves us from using an external visited set.
"""

class Solution(object):
    def exist(self, board, word):
        R,C=len(board),len(board[0])
        def dfs(r,c,i):
            if i==len(word): return True
            if r<0 or c<0 or r>=R or c>=C or board[r][c]!=word[i]: return False
            tmp=board[r][c]
            board[r][c]="#"
            res=dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
            board[r][c]=tmp
            return res
        for r in range(R):
            for c in range(C):
                if dfs(r,c,0): return True
        return False
