"""
Problem: 51. N-Queens
Difficulty: Hard
URL: https://leetcode.com/problems/n-queens/

Description:
The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.

Time Complexity: O(N!) - We place one queen per row, with decreasing options.
Space Complexity: O(N^2) - To maintain the board state and the recursion stack.
"""
class Solution(object):
    def solveNQueens(self, n):
        cols=set()
        pos_diag=set()
        neg_diag=set()
        res=[]
        board=[["."]*n for _ in range(n)]
        def backtrack(r):
            if r==n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in cols or (r+c) in pos_diag or (r-c) in neg_diag: continue
                cols.add(c); pos_diag.add(r+c); neg_diag.add(r-c)
                board[r][c]="Q"
                backtrack(r+1)
                cols.remove(c); pos_diag.remove(r+c); neg_diag.remove(r-c)
                board[r][c]="."
        backtrack(0)
        return res
