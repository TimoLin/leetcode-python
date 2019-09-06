#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if (needle == ""):
            return 0
        if (haystack == "" or len(haystack) < len(needle)) :
            return -1

        for i in range(0,len(haystack)-len(needle)+1):
            if (haystack[i:i+len(needle)] == needle):
                return i
        
        return -1
            


