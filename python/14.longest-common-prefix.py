#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
# Note: Vertical scanning

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if (len(strs)==0 or "" in strs):
            return ""

        if (len(strs)==1):
            return strs[0]
        
        for i in range(len(strs[0])):
            comnPre = strs[0][0:i+1]
            for str in strs:
                if comnPre != str[0:i+1]:
                    return comnPre[0:i]
        return comnPre


