#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        # For palindrome string(including empty), return itself
        if s == s[::-1]:
            return s
        
        n = len(s)

        s_rever = s[::-1]
        i_short = n-1 
        for i in range(n-1):
            s_new = s_rever[0:i+1]+s
            if s_new == s_new[::-1]:
                return s_new
                break


