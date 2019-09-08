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
        n_half = int((len(s)+1)/2)-1
       
        for i in range(n_half,0,-1):
            # For "abcdaef"
            if (s[0:i] == s[2*i:i:-1]):
                return s[n:i:-1]+s[i:]
            # For "abbacd"
            elif (s[0:i] == s[2*i-1:i-1:-1]):
                return s[n:2*i-1:-1]+s
        # For "aabcd"
        if (s[0] == s[1]):
            return s[n:1:-1]+s
        else:
        # For "abcdef"
            return s[:0:-1]+s
